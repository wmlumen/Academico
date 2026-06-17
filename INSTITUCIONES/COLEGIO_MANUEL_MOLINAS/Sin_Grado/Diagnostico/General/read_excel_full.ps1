$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$workbook = $excel.Workbooks.Open("C:\Users\HP 250 G10\Documents\MEC\DIAGNOSTICO MOLINAS\PLANILLA DE DIAGNOSTICO I MM I 2026.xlsx")
$sheet = $workbook.Sheets.Item(1)
$usedRange = $sheet.UsedRange
$rows = $usedRange.Rows.Count
$cols = $usedRange.Columns.Count

for ($r = 1; $r -le $rows; $r++) {
    $rowData = @()
    for ($c = 1; $c -le $cols; $c++) {
        $cell = $sheet.Cells.Item($r, $c)
        $rowData += $cell.Text
    }
    $rowData -join "|"
}
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null