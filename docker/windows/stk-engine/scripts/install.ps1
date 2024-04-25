Param([Parameter(Mandatory=$false)] [String] $agreeToLicense)

if ($agreeToLicense -ne 'yes') {
    Write-Error "You must agree to accept the STK User License by setting the 'agreeToLicense' build-arg."
    exit 1
}

Write-Host "Installing STK ZIPs"

# Find all ZIPs
$zipFiles = Get-ChildItem -Path C:/Users/STK/dist/ 'STK*.zip'
foreach ($zipFile in $zipFiles) {

    # Extract the current ZIP
    Write-Host "Extracting $zipFile"
    $zipFile -match "(?<archive>.*)\.zip" | Out-Null
    $dirname = $matches['archive']
    Expand-Archive -Path "C:/Users/STK/dist/$zipFile" -DestinationPath C:/Users/STK/dist/
    Write-Host "Extracted $zipFile"

    # Install current ZIP using setup.exe
    Write-Host "Installing $zipFile"
    $setup = Get-ChildItem -Path "C:/Users/STK/dist/$dirname" -Recurse 'setup.exe' | Select-Object -ExpandProperty FullName
    Start-Process $setup -Wait -ArgumentList @('/S', '/V"/qn /L*v C:/Users/STK/dist/install.log AgreeToLicense=Yes"')
    Write-Host "Installed $zipFile"

    # Remove processed files/directories
    Remove-Item "C:/Users/STK/dist/$zipFile"
    Remove-Item -Path "C:/Users/STK/dist/$dirname" -Force -Recurse
}

Remove-Item -Path C:/Users/STK/dist/ -Force -Recurse