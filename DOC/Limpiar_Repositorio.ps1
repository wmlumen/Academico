# MEC PRO 2026: Script de Limpieza y Organización Final
# Ejecución: En la raíz del repositorio (PowerShell)

Write-Host "Iniciando limpieza de estructura v19..." -ForegroundColor Cyan

# 1. Asegurar Carpeta Maestra
if (!(Test-Path "Recursos")) {
    New-Item -ItemType Directory -Path "Recursos"
    Write-Host "[+] Carpeta Recursos creada."
}

# 2. Carpetas a Eliminar (Redundantes tras migración)
$carpetasViejas = @(
    "7_Grado",
    "8_Grado",
    "Educacion_Media",
    "Materiales_Organizados",
    "Documentacion_Proyecto"
)

foreach ($carpeta in $carpetasViejas) {
    if (Test-Path $carpeta) {
        Remove-Item -Recurse -Force $carpeta
        Write-Host "[-] Eliminada carpeta obsoleta: $carpeta" -ForegroundColor Yellow
    }
}

# 3. Finalización
Write-Host "¡Repositorio Organizado con Éxito!" -ForegroundColor Green
Write-Host "Próximo paso: Abrir Dashboard_Docente.html"
