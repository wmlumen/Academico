$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$workbook = $excel.Workbooks.Open("C:\Users\HP 250 G10\Documents\MEC\DIAGNOSTICO MOLINAS\PLANILLA DE DIAGNOSTICO I MM I 2026.xlsx")

$sheetCount = $workbook.Sheets.Count

for ($s = 1; $s -le $sheetCount; $s++) {
    $sheet = $workbook.Sheets.Item($s)
    $sheetName = $sheet.Name -replace '[\\/:*?"<>|]', '_'
    $usedRange = $sheet.UsedRange
    $rows = $usedRange.Rows.Count
    $cols = $usedRange.Columns.Count
    
    $output = @()
    
    for ($r = 1; $r -le $rows; $r++) {
        $rowData = @()
        for ($c = 1; $c -le $cols; $c++) {
            $cell = $sheet.Cells.Item($r, $c)
            $rowData += $cell.Text
        }
        $output += $rowData -join "|"
    }
    
    $output -join "`n" | Out-File -FilePath "C:\Users\HP 250 G10\Documents\MEC\DIAGNOSTICO MOLINAS\Sheet_$s`_$sheetName.txt" -Encoding UTF8
    Write-Host "Exported Sheet $s : $sheetName"
}

$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null