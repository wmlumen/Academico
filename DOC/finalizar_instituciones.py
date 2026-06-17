import hashlib
import json
import os
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(r"C:\Users\HP 250 G10\Documents\GITHUT\MEC\INSTITUCIONES")
REPORT = ROOT / "00_FINALIZACION_INSTITUCIONES.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def score_path(path: Path) -> tuple:
    name = path.name.lower()
    parts = [part.lower() for part in path.parts]
    penalty = 0
    if "__tmp_" in name:
        penalty += 100
    if re.search(r"__v\d+", name):
        penalty += 50
    if "__combinado.md" in name:
        penalty += 20
    if "sin_grado" in parts:
        penalty += 10
    if "sin_asignatura" in parts:
        penalty += 10
    depth = len(path.parts)
    return (penalty, depth, len(name), str(path).lower())


def remove_conflict_versions(report):
    deleted = []
    for dirpath, _, filenames in os.walk(ROOT):
        names = set(filenames)
        for filename in list(filenames):
            lower = filename.lower()
            if "__combinado" not in lower:
                continue

            base = re.sub(r"__combinado(\.[^.]+)$", "", filename, flags=re.I)
            pattern = re.compile(re.escape(base) + r"__v\d+\.[^.]+$", re.I)
            for candidate in names:
                if pattern.match(candidate):
                    path = Path(dirpath) / candidate
                    path.unlink(missing_ok=True)
                    deleted.append(str(path))

    report["deleted_conflict_versions"] = deleted


def remove_tmp_files(report):
    deleted = []
    for path in ROOT.rglob("*__TMP_*"):
        if path.is_file():
            path.unlink(missing_ok=True)
            deleted.append(str(path))
    report["deleted_tmp_files"] = deleted


def deduplicate_exact_files(report):
    by_hash = defaultdict(list)
    for path in ROOT.rglob("*"):
        if path.is_file() and path.name != REPORT.name:
            by_hash[sha256_file(path)].append(path)

    kept = []
    removed = []
    for _, paths in by_hash.items():
        if len(paths) < 2:
            continue
        ordered = sorted(paths, key=score_path)
        keep = ordered[0]
        kept.append(str(keep))
        for duplicate in ordered[1:]:
            duplicate.unlink(missing_ok=True)
            removed.append({"kept": str(keep), "removed": str(duplicate)})

    report["kept_duplicate_representatives"] = kept
    report["removed_exact_duplicates"] = removed


def main():
    report = {}
    remove_conflict_versions(report)
    remove_tmp_files(report)
    deduplicate_exact_files(report)
    report["remaining_files"] = sum(1 for path in ROOT.rglob("*") if path.is_file())
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
