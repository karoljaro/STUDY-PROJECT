"""
JSON Parser module - Task2: JSON file reading and validation

This module provides functionality to read from JSON files
with proper error handling and validation.
"""

import json
from pathlib import Path
from typing import Any, Dict, Union


class JSONParser:
    """Parser for JSON file operations - Task2: Loading and validation only."""
    
    @staticmethod
    def load(file_path: Path) -> Dict[str, Any]:
        """
        Load data from a JSON file.
        
        Args:
            file_path: Path to the JSON file to read
            
        Returns:
            Dictionary containing the parsed JSON data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the JSON is invalid or malformed
            PermissionError: If there's no permission to read the file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                loaded_data: Any = json.load(file)
                if not isinstance(loaded_data, dict):
                    data: Dict[str, Any] = {"data": loaded_data}
                else:
                    data = loaded_data
                return data
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {file_path}: {e}")
        except PermissionError:
            raise PermissionError(f"No permission to read file: {file_path}")
        except Exception as e:
            raise ValueError(f"Error reading JSON file {file_path}: {e}")
    
    @staticmethod
    def validate(file_path: Path) -> bool:
        """
        Validate if a file contains valid JSON.
        
        Args:
            file_path: Path to the JSON file to validate
            
        Returns:
            True if the JSON is valid, False otherwise
        """
        try:
            JSONParser.load(file_path)
            return True
        except (ValueError, FileNotFoundError, PermissionError):
            return False
    
    @staticmethod
    def get_file_info(file_path: Path) -> Dict[str, Any]:
        """
        Get information about a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            Dictionary with file information
        """
        try:
            data = JSONParser.load(file_path)
            return {
                "format": "JSON",
                "valid": True,
                "size_bytes": file_path.stat().st_size,
                "keys_count": len(data) if isinstance(data, dict) else 1,
                "encoding": "utf-8"
            }
        except Exception as e:
            return {
                "format": "JSON",
                "valid": False,
                "error": str(e),
                "size_bytes": file_path.stat().st_size if file_path.exists() else 0
            }
