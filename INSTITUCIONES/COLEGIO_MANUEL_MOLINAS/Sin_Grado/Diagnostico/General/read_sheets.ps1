$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$workbook = $excel.Workbooks.Open("C:\Users\HP 250 G10\Documents\MEC\DIAGNOSTICO MOLINAS\PLANILLA DE DIAGNOSTICO I MM I 2026.xlsx")
$sheetCount = $workbook.Sheets.Count
Write-Host "Sheets: $sheetCount"
for ($i = 1; $i -le $sheetCount; $i++) {
    $sheet = $workbook.Sheets.Item($i)
    Write-Host "Sheet $i : $($sheet.Name)"
}
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null