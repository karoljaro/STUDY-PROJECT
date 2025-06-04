"""
XML Parser module - Task6: XML file reading and validation

This module provides functionality to read from XML files
with proper error handling and validation.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict


class XMLParser:
    """Parser for XML file operations - Task6: Loading and validation."""
    
    @staticmethod
    def load(file_path: Path) -> Dict[str, Any]:
        """
        Load data from an XML file.
        
        Args:
            file_path: Path to the XML file to read
            
        Returns:
            Dictionary containing the parsed XML data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the XML is invalid or malformed
            PermissionError: If there's no permission to read the file
        """
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = XMLParser._element_to_dict(root)
            
            if root.tag:
                return {root.tag: data}
            else:
                return data if isinstance(data, dict) else {"data": data}
                
        except FileNotFoundError:
            raise FileNotFoundError(f"XML file not found: {file_path}")
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML format in {file_path}: {e}")
        except PermissionError:
            raise PermissionError(f"No permission to read file: {file_path}")
        except Exception as e:
            raise ValueError(f"Error reading XML file {file_path}: {e}")
    
    @staticmethod
    def validate(file_path: Path) -> bool:
        """
        Validate if a file contains valid XML.
        
        Args:
            file_path: Path to the XML file to validate
            
        Returns:
            True if the XML is valid, False otherwise
        """
        try:
            XMLParser.load(file_path)
            return True
        except (ValueError, FileNotFoundError, PermissionError):
            return False
    
    @staticmethod
    def get_file_info(file_path: Path) -> Dict[str, Any]:
        """
        Get information about an XML file.
        
        Args:
            file_path: Path to the XML file
            
        Returns:
            Dictionary with file information
        """
        try:
            data = XMLParser.load(file_path)
            
            def count_elements(obj: Any) -> int:
                if isinstance(obj, dict):
                    return sum(count_elements(v) for v in obj.values()) + len(obj)
                elif isinstance(obj, list):
                    return sum(count_elements(item) for item in obj)
                else:
                    return 1
            
            return {
                "format": "XML",
                "valid": True,
                "size_bytes": file_path.stat().st_size,
                "elements_count": count_elements(data),
                "encoding": "utf-8"
            }
        except Exception as e:            
            return {
                "format": "XML",
                "valid": False,
                "error": str(e),
                "size_bytes": file_path.stat().st_size if file_path.exists() else 0
            }
    
    @staticmethod
    def _element_to_dict(element: ET.Element) -> Any:
        """
        Convert XML element to dictionary.
        
        Args:
            element: XML element to convert
            
        Returns:
            Dictionary representation of the element
        """
        result: Dict[str, Any] = {}
        if element.attrib:
            for attr, value in element.attrib.items():
                result[f"@{attr}"] = value
        
        # Handle text content
        if element.text and element.text.strip():
            if len(element) == 0 and not element.attrib:
                return element.text.strip()
            else:
                result["#text"] = element.text.strip()
          # Handle child elements
        children: Dict[str, Any] = {}
        for child in element:
            child_data = XMLParser._element_to_dict(child)
            
            if child.tag in children:
                if not isinstance(children[child.tag], list):
                    children[child.tag] = [children[child.tag]]
                children[child.tag].append(child_data)            
            else:
                children[child.tag] = child_data
        result.update(children)
        
        if (len(result) == 1 and 
            not any(k.startswith('@') or k == '#text' for k in result.keys()) and
            not element.attrib and
            not isinstance(list(result.values())[0], list)):
            return list(result.values())[0]
        
        return result if result else None
