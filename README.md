# Data Format Converter - STUDY PROJECT

A comprehensive data format converter supporting XML, JSON, and YAML formats with both CLI and GUI interfaces.

## Features

### Core Functionality (Tasks 0-7)
- ✅ **Bidirectional conversion** between JSON, YAML, and XML formats
- ✅ **Command-line interface** with argument parsing
- ✅ **Robust error handling** and file validation
- ✅ **Format auto-detection** based on file extensions
- ✅ **Structured parser architecture** with consistent interfaces

### GUI Application (Task 8-9)
- ✅ **PyQt5-based graphical interface** for easy file conversion
- ✅ **File browser dialogs** for input/output selection
- ✅ **Real-time progress tracking** with progress bars
- ✅ **Threaded conversion** to prevent UI blocking
- ✅ **Conversion logging** and status updates
- ✅ **Asynchronous file operations** with DateTime support

## Installation

### For Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run PowerShell setup (optional):
```powershell
.\installResources.ps1
```

### For End Users - Download Executable
**No Python installation required!** Download ready-to-use executable:

1. Go to [GitHub Actions](../../actions) 
2. Click on latest successful workflow run
3. Download `DataFormatConverter-CLI-Windows` artifact
4. Extract `DataFormatConverter-CLI.exe`
5. Use directly from command line!

## Usage

### Command Line Interface - Python
```bash
# Convert JSON to YAML
python main.py input.json output.yaml --format yaml

# Convert XML to JSON  
python main.py data.xml result.json --format json

# Convert YAML to XML
python main.py config.yaml settings.xml --format xml
```

### Command Line Interface - Executable (.exe)
Download and use without Python installation:

```cmd
# Basic usage
DataFormatConverter-CLI.exe input.json output.yaml --format yaml

# Examples with different formats
DataFormatConverter-CLI.exe data.xml result.json --format json
DataFormatConverter-CLI.exe config.yaml settings.xml --format xml

# Test with provided test files
DataFormatConverter-CLI.exe tests\simple_test.json output.yaml --format yaml
DataFormatConverter-CLI.exe tests\test_input.xml output.json --format json
```

**Command Structure:**
```
DataFormatConverter-CLI.exe [input_file] [output_file] --format [yaml|json|xml]
```

### Graphical User Interface (For Development)
```bash
# Launch GUI application (requires Python)
python gui.py
# or
python run_gui.py
```

## Supported Formats

| Format | Extensions | Read | Write |
|--------|------------|------|-------|
| JSON   | `.json`    | ✅   | ✅    |
| YAML   | `.yaml`, `.yml` | ✅   | ✅    |
| XML    | `.xml`     | ✅   | ✅    |

## Project Structure

```
├── main.py              # CLI application
├── gui.py               # GUI application  
├── run_gui.py           # GUI launcher
├── requirements.txt     # Dependencies
├── installResources.ps1 # Setup script
├── parsers/            # Parser modules
│   ├── __init__.py
│   ├── json_parser.py   # JSON handling
│   ├── yaml_parser.py   # YAML handling
│   └── xml_parser.py    # XML handling
└── tests/              # Test files
    ├── simple_test.*    # Basic test files (JSON, YAML, XML)
    └── test_input.*     # Complex test files (JSON, YAML, XML)
```

## Testing

The `tests/` directory contains sample files for testing conversions:

- **Simple test files**: Basic data structures for quick testing
- **Complex test files**: Nested structures with arrays and objects

### Test with CLI:
```bash
python main.py tests/simple_test.json output.yaml --format yaml
python main.py tests/test_input.xml output.json --format json
```

### Test with GUI:
1. Run `python run_gui.py`
2. Browse and select files from `tests/` directory
3. Choose output format and convert

## Development Tasks

- [x] **Task 0**: Environment setup and dependencies
- [x] **Task 1**: Argument parsing and file validation  
- [x] **Task 2**: JSON parser implementation
- [x] **Task 3**: JSON saving functionality
- [x] **Task 4**: YAML parser implementation
- [x] **Task 5**: YAML saving functionality
- [x] **Task 6**: XML parser implementation
- [x] **Task 7**: XML saving functionality
- [x] **Task 8**: GUI implementation with PyQt5
- [x] **Task 9**: Asynchronous file operations with DateTime support

## Local Building (For Developers)

### Creating .exe Files Manually

If you want to build the executable files locally instead of downloading from GitHub Actions:

#### Prerequisites
1. **Install Python 3.7+** on your system
2. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd STUDY-PROJECT
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or use PowerShell script:
   ```powershell
   .\installResources.ps1
   ```

#### Quick Test - Local Files Available
The project already contains pre-built executables in the `dist/` folder:

```cmd
# Test the existing CLI executable
dist\DataFormatConverter-CLI.exe --help

# Convert a test file
dist\DataFormatConverter-CLI.exe tests\simple_test.json test_output.yaml --format yaml
```

**Note**: Local executables are built with current Python environment and may differ from GitHub Actions builds.

#### Building CLI Executable
```bash
# Install PyInstaller if not already installed
pip install pyinstaller

# Build CLI executable (single file)
pyinstaller --onefile --name="DataFormatConverter-CLI" main.py

# The .exe will be created in dist/ folder
# File: dist/DataFormatConverter-CLI.exe
```

#### Building GUI Executable (Optional)
```bash
# Build GUI executable (windowed, no console)
pyinstaller --onefile --windowed --name="DataFormatConverter-GUI" gui.py

# The .exe will be created in dist/ folder  
# File: dist/DataFormatConverter-GUI.exe
```

#### Testing Your Built Executable
```cmd
# Test CLI executable
dist\DataFormatConverter-CLI.exe --help

# Test with sample files
dist\DataFormatConverter-CLI.exe tests\simple_test.json output.yaml --format yaml
```

#### Build Options Explained
- `--onefile` - Creates a single executable file (easier to distribute)
- `--windowed` - For GUI apps, hides the console window
- `--name="CustomName"` - Sets the name of the output executable
- `main.py` / `gui.py` - The entry point script to build

#### Typical File Sizes
- **CLI executable**: ~9MB
- **GUI executable**: ~15-20MB (includes PyQt5 libraries)

#### Troubleshooting Build Issues
- **Missing modules**: Make sure all dependencies are installed with `pip install -r requirements.txt`
- **Antivirus warnings**: Some antivirus software may flag PyInstaller executables as suspicious
- **Large file size**: This is normal for PyInstaller - it bundles Python and all dependencies
- **Slow startup**: First run may be slower as Windows scans the executable

## GitHub Actions - Automated Building

The project includes automated building workflow that:

- **Builds Windows executable** automatically using PyInstaller
- **Triggers on**:
  - Every Monday at 9:00 AM UTC (weekly)
  - Push to main/master branch  
  - Manual dispatch by user
- **Creates CLI executable**:
  - `DataFormatConverter-CLI.exe` - Command line interface
- **Uploads artifacts** to GitHub repository for download
- **Includes documentation** and test files in release package

### Downloading Built Executables

1. Go to repository's **Actions** tab
2. Select latest successful workflow run
3. Download artifacts:
   - `DataFormatConverter-CLI-Windows` - CLI executable only
   - `DataFormatConverter-Complete-Package` - Full package with docs and tests

### Using the Downloaded Executable

1. **Download** the artifact from GitHub Actions
2. **Extract** `DataFormatConverter-CLI.exe` to any folder
3. **Open Command Prompt** in that folder
4. **Use directly** without installing Python:

```cmd
# Get help
DataFormatConverter-CLI.exe --help

# Convert files
DataFormatConverter-CLI.exe input.json output.yaml --format yaml
DataFormatConverter-CLI.exe config.xml data.json --format json
```

**Features of the .exe:**
- ✅ **No Python required** - runs on any Windows machine
- ✅ **Single file** - easy to distribute and use
- ✅ **All formats supported** - JSON, YAML, XML conversion
- ✅ **Same functionality** as Python version
- ✅ **Small size** - approximately 8.6MB

### Step-by-Step Guide for .exe Usage

#### 1. Download the Executable
1. Visit the [GitHub Actions page](../../actions)
2. Click on the latest successful workflow run (green checkmark ✅)
3. Scroll down to "Artifacts" section
4. Download `DataFormatConverter-CLI-Windows`
5. Extract the ZIP file to get `DataFormatConverter-CLI.exe`

#### 2. Basic Usage
Place the `.exe` file in any folder and open Command Prompt in that location:

```cmd
# Show help and all available options
DataFormatConverter-CLI.exe --help

# Basic conversion syntax
DataFormatConverter-CLI.exe [input_file] [output_file] --format [target_format]
```

#### 3. Conversion Examples

**JSON to YAML:**
```cmd
DataFormatConverter-CLI.exe data.json output.yaml --format yaml
```

**XML to JSON:**
```cmd
DataFormatConverter-CLI.exe config.xml result.json --format json
```

**YAML to XML:**
```cmd
DataFormatConverter-CLI.exe settings.yaml config.xml --format xml
```

#### 4. Working with Paths
```cmd
# Absolute paths
DataFormatConverter-CLI.exe C:\data\input.json C:\output\result.yaml --format yaml

# Relative paths (files in same folder)
DataFormatConverter-CLI.exe input.json output.xml --format xml

# Different folders
DataFormatConverter-CLI.exe ..\input\data.xml output\result.json --format json
```

#### 5. Error Handling
The executable provides clear error messages:
- ✅ **File validation** - checks if input file exists
- ✅ **Format detection** - automatically detects input format
- ✅ **Conversion status** - shows progress and results
- ✅ **Error reporting** - detailed error messages if something goes wrong

#### 6. Example Output
When you run the executable, you'll see detailed progress information:

```cmd
C:\> DataFormatConverter-CLI.exe input.json output.yaml --format yaml
✓ Input file: input.json
✓ Detected input format: JSON
✓ Output file: output.yaml
✓ Target output format: YAML
Reading JSON file...
Successfully loaded JSON with 4 top-level keys
File size: 145 bytes
Saving as YAML...
✓ YAML file saved successfully to: output.yaml
```

**Help Output:**
```cmd
C:\> DataFormatConverter-CLI.exe --help
usage: DataFormatConverter-CLI.exe [-h] --format {yaml,xml,json} input_file output_file

YAML, XML, JSON format converter

positional arguments:
  input_file            Input file path
  output_file           Output file path

options:
  -h, --help            show this help message and exit
  --format {yaml,xml,json}
                        Output format

Example: DataFormatConverter-CLI.exe input.json output.yaml --format yaml
```

#### 7. Testing with Sample Files
The project includes test files that you can use to verify the executable works correctly:

```cmd
# Download the complete package (includes tests/ folder)
# Extract and navigate to the folder, then:

# Test JSON to YAML conversion
DataFormatConverter-CLI.exe tests\simple_test.json test_result.yaml --format yaml

# Test XML to JSON conversion  
DataFormatConverter-CLI.exe tests\test_input.xml test_result.json --format json

# Test YAML to XML conversion
DataFormatConverter-CLI.exe tests\simple_test.yaml test_result.xml --format xml
```

**Sample test files included:**
- `tests\simple_test.json` - Basic JSON structure
- `tests\simple_test.yaml` - Basic YAML structure  
- `tests\simple_test.xml` - Basic XML structure
- `tests\test_input.*` - More complex nested structures

## Requirements

- Python 3.7+
- PyYAML
- PyQt5 (for GUI)
- PyInstaller (for building executables)
- pytest (for testing)
- mypy (for type checking)
