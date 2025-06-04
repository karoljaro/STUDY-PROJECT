"""
Data format converter - Task4: YAML parsing added
Supports XML, JSON, and YAML format conversion
"""

import argparse
from pathlib import Path
import sys
from parsers.json_parser import JSONParser
from parsers.yaml_parser import YAMLParser


def validate_files(input_path: Path, output_path: Path) -> None:
    """Validate input and output file paths."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")
    
    if not input_path.is_file():
        raise ValueError(f"Input path is not a file: {input_path}")
    
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        raise PermissionError(f"No write permission for: {output_path.parent}")


def detect_input_format(file_path: Path) -> str:
    """Detect input file format based on extension."""
    extension = file_path.suffix.lower()
    format_map = {
        '.json': 'json',
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.xml': 'xml'
    }
    return format_map.get(extension, 'unknown')


def main() -> None:
    """Main function - Task3: Added JSON saving."""
    parser = argparse.ArgumentParser(
        description="YAML, XML, JSON format converter",
        epilog=r"Example: python main.py input.json output.yaml --format yaml"
    )
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    parser.add_argument("--format", choices=["yaml", "xml", "json"], help="Output format", required=True)

    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    try:
        validate_files(input_path=input_path, output_path=output_path)
        
        input_format = detect_input_format(input_path)
        if input_format == 'unknown':
            raise ValueError(f"Unsupported input file format: {input_path.suffix}")
        
        print(f"✓ Input file: {input_path}")
        print(f"✓ Detected input format: {input_format.upper()}")
        print(f"✓ Output file: {output_path}")
        print(f"✓ Target output format: {args.format.upper()}")        # Task2: JSON loading implementation
        if input_format == 'json':
            print("Reading JSON file...")
            data = JSONParser.load(input_path)
            print(f"Successfully loaded JSON with {len(data)} top-level keys")
            
            # Show some info about the loaded data
            file_info = JSONParser.get_file_info(input_path)
            print(f"File size: {file_info['size_bytes']} bytes")
        # Task4: YAML loading implementation
        elif input_format == 'yaml':
            print("Reading YAML file...")
            data = YAMLParser.load(input_path)
            print(f"Successfully loaded YAML with {len(data)} top-level keys")
            
            # Show some info about the loaded data
            file_info = YAMLParser.get_file_info(input_path)
            print(f"File size: {file_info['size_bytes']} bytes")
        else:
            print(f"Note: {input_format.upper()} parsing not yet implemented - will be added in Task6-7")
            return
        
        # Task3: JSON saving implementation
        if args.format == 'json':
            print("Saving as JSON...")
            JSONParser.save(data, output_path)
            print(f"✓ JSON file saved successfully to: {output_path}")
        else:
            print(f"Note: {args.format.upper()} output not yet implemented - will be added in Task4-7")
        
    except (FileNotFoundError, ValueError, PermissionError) as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()