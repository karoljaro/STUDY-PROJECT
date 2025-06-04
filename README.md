# Data Format Converter - STUDY PROJECT

A comprehensive data format converter supporting XML, JSON, and YAML formats with both CLI and GUI interfaces.

## Features

### Core Functionality (Tasks 0-7)
- ✅ **Bidirectional conversion** between JSON, YAML, and XML formats
- ✅ **Command-line interface** with argument parsing
- ✅ **Robust error handling** and file validation
- ✅ **Format auto-detection** based on file extensions
- ✅ **Structured parser architecture** with consistent interfaces

### GUI Application (Task 8)
- ✅ **PyQt5-based graphical interface** for easy file conversion
- ✅ **File browser dialogs** for input/output selection
- ✅ **Real-time progress tracking** with progress bars
- ✅ **Threaded conversion** to prevent UI blocking
- ✅ **Conversion logging** and status updates

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run PowerShell setup (optional):
```powershell
.\installResources.ps1
```

## Usage

### Command Line Interface
```bash
# Convert JSON to YAML
python main.py input.json output.yaml --format yaml

# Convert XML to JSON  
python main.py data.xml result.json --format json

# Convert YAML to XML
python main.py config.yaml settings.xml --format xml
```

### Graphical User Interface
```bash
# Launch GUI application
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
- [ ] **Task 9**: Asynchronous file operations (Coming Soon)

## Requirements

- Python 3.7+
- PyYAML
- PyQt5 (for GUI)
- pytest (for testing)
- mypy (for type checking)
