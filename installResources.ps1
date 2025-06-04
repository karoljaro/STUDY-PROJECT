# Installation script for project dependencies
# Run this script to install all required Python packages for the converter project

Write-Host "Installing project dependencies..." -ForegroundColor Green

# Install from requirements.txt if exists
if (Test-Path "requirements.txt") {
    Write-Host "Installing from requirements.txt..." -ForegroundColor Yellow
    pip install -r requirements.txt
} else {
    Write-Host "requirements.txt not found, installing individual packages..." -ForegroundColor Yellow
    
    # Testing dependencies
    Write-Host "Installing testing dependencies..." -ForegroundColor Yellow
    pip install pytest
    pip install pytest-cov
    
    # YAML support
    Write-Host "Installing YAML support..." -ForegroundColor Yellow  
    pip install PyYAML
    
    # Type checking
    Write-Host "Installing type checking tools..." -ForegroundColor Yellow
    pip install mypy
    pip install types-PyYAML
}

# Build tool for creating executable
Write-Host "Installing build tools..." -ForegroundColor Yellow
pip install pyinstaller

Write-Host "All dependencies installed successfully!" -ForegroundColor Green
Write-Host "You can now run the converter program." -ForegroundColor Cyan

# Display installed packages
Write-Host "`nInstalled packages:" -ForegroundColor Cyan
pip list | Select-String "pytest|PyYAML|mypy|pyinstaller"
