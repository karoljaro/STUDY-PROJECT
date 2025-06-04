"""
YAML Parser module - Task4: YAML file reading and validation

This module provides functionality to read from YAML files
with proper error handling and validation.
"""

import yaml
from pathlib import Path
from typing import Any, Dict


class YAMLParser:
    """Parser for YAML file operations - Task4: Loading and validation."""
    
    @staticmethod
    def load(file_path: Path) -> Dict[str, Any]:
        """
        Load data from a YAML file with validation.
        
        Args:
            file_path: Path to the YAML file to read
            
        Returns:
            Dictionary containing the parsed YAML data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the YAML is invalid or malformed
            PermissionError: If there's no permission to read the file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                loaded_data: Any = yaml.safe_load(file)
                
                # Ensure we always return a dictionary
                if not isinstance(loaded_data, dict):
                    data: Dict[str, Any] = {"data": loaded_data}
                else:
                    data = loaded_data
                    
                return data
                
        except FileNotFoundError:
            raise FileNotFoundError(f"YAML file not found: {file_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format in {file_path}: {e}")
        except PermissionError:
            raise PermissionError(f"No permission to read file: {file_path}")
        except Exception as e:
            raise ValueError(f"Error reading YAML file {file_path}: {e}")
    
    @staticmethod
    def validate(file_path: Path) -> bool:
        """
        Validate if a file contains valid YAML.
        
        Args:
            file_path: Path to the YAML file to validate
            
        Returns:
            True if the YAML is valid, False otherwise
        """
        try:
            YAMLParser.load(file_path)
            return True
        except (ValueError, FileNotFoundError, PermissionError):
            return False
    
    @staticmethod
    def get_file_info(file_path: Path) -> Dict[str, Any]:
        """
        Get information about a YAML file.
        
        Args:
            file_path: Path to the YAML file
            
        Returns:
            Dictionary with file information
        """
        try:
            data = YAMLParser.load(file_path)
            return {
                "format": "YAML",
                "valid": True,
                "size_bytes": file_path.stat().st_size,
                "keys_count": len(data) if isinstance(data, dict) else 1,
                "encoding": "utf-8"
            }
        except Exception as e:
            return {
                "format": "YAML",
                "valid": False,
                "error": str(e),
                "size_bytes": file_path.stat().st_size if file_path.exists() else 0
            }
