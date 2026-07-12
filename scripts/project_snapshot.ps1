$outputDir = "output"
$outputFile = "output\project_snapshot.md"

New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

"# Project Snapshot" | Set-Content $outputFile
"" | Add-Content $outputFile
"Generated report" | Add-Content $outputFile
"" | Add-Content $outputFile

"## Current Branch" | Add-Content $outputFile
git branch --show-current | Add-Content $outputFile
"" | Add-Content $outputFile

"## Git Status" | Add-Content $outputFile
git status | Add-Content $outputFile
"" | Add-Content $outputFile

"## Recent Commits" | Add-Content $outputFile
git log --oneline -n 10 | Add-Content $outputFile
"" | Add-Content $outputFile

"## App Files" | Add-Content $outputFile
Get-ChildItem app -Recurse -File -ErrorAction SilentlyContinue |
ForEach-Object { $_.FullName } |
Add-Content $outputFile
"" | Add-Content $outputFile

"## Test Files" | Add-Content $outputFile
Get-ChildItem tests -Recurse -File -ErrorAction SilentlyContinue |
ForEach-Object { $_.FullName } |
Add-Content $outputFile
"" | Add-Content $outputFile

"## Python Version" | Add-Content $outputFile
python --version | Add-Content $outputFile
"" | Add-Content $outputFile

"## Pytest Version" | Add-Content $outputFile
pytest --version | Add-Content $outputFile
"" | Add-Content $outputFile

Write-Host "Done"