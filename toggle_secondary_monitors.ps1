# Define the path to the state file
$stateFilePath = "$env:USERPROFILE\Desktop\displayState.txt"

# Define the process names

# Check if the state file exists, if not create it and set initial state to 'extend'
if (-Not (Test-Path $stateFilePath)) {
"extend" | Out-File $stateFilePath
$currentState = "extend"
} else {
# Read the current state from the file
$currentState = Get-Content $stateFilePath
}

# Output current state for debugging
Write-Host "Current display state is: $currentState"

# Switch the display state based on the current state in the file
if ($currentState -eq "extend") {
DisplaySwitch.exe /internal
"internal" | Out-File $stateFilePath

#disable real-time protection
Set-MpPreference -DisableRealtimeMonitoring $true

$processNames = @("SearchApp", "TextInputHost", "StartMenuExperienceHost", "ShellExperienceHost")
#"explorer",   removed

# Stop the processes
foreach ($processName in $processNames) {
    Stop-Process -Name $processName -Force -ErrorAction SilentlyContinue
}



Write-Host "Switched to internal. Updating state to 'internal'."
} else {
DisplaySwitch.exe /extend
"extend" | Out-File $stateFilePath

#enable real-time protection
Set-MpPreference -DisableRealtimeMonitoring $false

Write-Host "Switched to extend. Updating state to 'extend'."
}

# Optional: Add a pause to see the output when running the script
#Read-Host -Prompt "Press Enter to exit"