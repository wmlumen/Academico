$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
Write-Host "Iniciando BTCC en http://127.0.0.1:8080"
node .\server.js
