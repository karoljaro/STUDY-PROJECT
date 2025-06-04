"""
GUI application for data format converter - Task9
PyQt5-based graphical user interface with asynchronous file operations
"""

import sys
from pathlib import Path
from typing import Optional
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QFileDialog,
    QMessageBox, QProgressBar, QGroupBox, QGridLayout, QSplitter
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont
from parsers.json_parser import JSONParser
from parsers.yaml_parser import YAMLParser
from parsers.xml_parser import XMLParser


class ConversionWorker(QThread):
    """Worker thread for file conversion to avoid blocking the UI."""
    
    finished = pyqtSignal(str)  # Success message
    error = pyqtSignal(str)     # Error message
    progress = pyqtSignal(int)  # Progress update
    
    def __init__(self, input_file: str, output_file: str, output_format: str):
        super().__init__()
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        self.output_format = output_format
        
    def run(self):
        """Run the conversion in a separate thread."""
        try:
            self.progress.emit(25)
            
            # Detect input format
            input_format = self._detect_format(self.input_file)
            if input_format == 'unknown':
                self.error.emit(f"Unsupported input file format: {self.input_file.suffix}")
                return
                
            self.progress.emit(50)
            
            # Load data based on input format
            if input_format == 'json':
                data = JSONParser.load(self.input_file)
            elif input_format == 'yaml':
                data = YAMLParser.load(self.input_file)
            elif input_format == 'xml':
                data = XMLParser.load(self.input_file)
            else:
                self.error.emit(f"Unsupported input format: {input_format}")
                return
                
            self.progress.emit(75)
            
            # Save data in output format
            if self.output_format == 'json':
                JSONParser.save(data, self.output_file)
            elif self.output_format == 'yaml':
                YAMLParser.save(data, self.output_file)
            elif self.output_format == 'xml':
                XMLParser.save(data, self.output_file)
            else:
                self.error.emit(f"Unsupported output format: {self.output_format}")
                return
                
            self.progress.emit(100)
            self.finished.emit(f"Successfully converted {self.input_file.name} to {self.output_file.name}")
            
        except Exception as e:
            self.error.emit(f"Conversion failed: {str(e)}")
    
    def _detect_format(self, file_path: Path) -> str:
        """Detect file format based on extension."""
        extension = file_path.suffix.lower()
        format_map = {
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.xml': 'xml'
        }
        return format_map.get(extension, 'unknown')


class FormatConverterGUI(QMainWindow):
    """Main GUI window for the format converter application."""
    
    def __init__(self) -> None:
        super().__init__()
        self.conversion_worker: Optional[ConversionWorker] = None
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Data Format Converter - Task9")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Title
        title_label = QLabel("Data Format Converter")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # File selection group
        file_group = QGroupBox("File Selection")
        file_layout = QGridLayout(file_group)
        
        # Input file selection
        file_layout.addWidget(QLabel("Input File:"), 0, 0)
        self.input_file_edit = QLineEdit()
        self.input_file_edit.setPlaceholderText("Select input file...")
        file_layout.addWidget(self.input_file_edit, 0, 1)
        
        self.browse_input_btn = QPushButton("Browse...")
        self.browse_input_btn.clicked.connect(self.browse_input_file)
        file_layout.addWidget(self.browse_input_btn, 0, 2)
        
        # Output file selection
        file_layout.addWidget(QLabel("Output File:"), 1, 0)
        self.output_file_edit = QLineEdit()
        self.output_file_edit.setPlaceholderText("Select output file...")
        file_layout.addWidget(self.output_file_edit, 1, 1)
        
        self.browse_output_btn = QPushButton("Browse...")
        self.browse_output_btn.clicked.connect(self.browse_output_file)
        file_layout.addWidget(self.browse_output_btn, 1, 2)
        
        # Output format selection
        file_layout.addWidget(QLabel("Output Format:"), 2, 0)
        self.format_combo = QComboBox()
        self.format_combo.addItems(["json", "yaml", "xml"])
        file_layout.addWidget(self.format_combo, 2, 1)
        
        main_layout.addWidget(file_group)
        
        # Conversion controls
        controls_layout = QHBoxLayout()
        
        self.convert_btn = QPushButton("Convert")
        self.convert_btn.clicked.connect(self.start_conversion)
        self.convert_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")
        controls_layout.addWidget(self.convert_btn)
        
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_fields)
        controls_layout.addWidget(self.clear_btn)
        
        controls_layout.addStretch()
        main_layout.addLayout(controls_layout)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)
        
        # Output/Log area
        log_group = QGroupBox("Conversion Log")
        log_layout = QVBoxLayout(log_group)
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(200)
        log_layout.addWidget(self.log_text)
        
        main_layout.addWidget(log_group)
        
        # Status bar
        self.statusBar().showMessage("Ready to convert files")
        
        # Initial log message
        self.log_message("Welcome to Data Format Converter!")
        self.log_message("Supported formats: JSON, YAML, XML")
        
    def browse_input_file(self):
        """Open file dialog to select input file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Input File",
            "",
            "All Supported (*.json *.yaml *.yml *.xml);;JSON files (*.json);;YAML files (*.yaml *.yml);;XML files (*.xml)"
        )
        if file_path:
            self.input_file_edit.setText(file_path)
            self.log_message(f"Selected input file: {Path(file_path).name}")
            
    def browse_output_file(self):
        """Open file dialog to select output file."""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Output File",
            "",
            "JSON files (*.json);;YAML files (*.yaml);;XML files (*.xml)"
        )
        if file_path:
            self.output_file_edit.setText(file_path)
            self.log_message(f"Selected output file: {Path(file_path).name}")
            
    def clear_fields(self):
        """Clear all input fields."""
        self.input_file_edit.clear()
        self.output_file_edit.clear()
        self.format_combo.setCurrentIndex(0)
        self.log_text.clear()
        self.log_message("Fields cleared")
        self.statusBar().showMessage("Ready to convert files")
    def start_conversion(self):
        """Start the file conversion process."""
        input_file = self.input_file_edit.text().strip()
        output_file = self.output_file_edit.text().strip()
        output_format = self.format_combo.currentText()
        
        # Validation
        if not input_file:
            self.show_error("Please select an input file")
            return
            
        if not output_file:
            self.show_error("Please select an output file")
            return
            
        if not Path(input_file).exists():
            self.show_error("Input file does not exist")
            return
            
        # Fix output file extension based on selected format
        output_file = self._fix_output_extension(output_file, output_format)
        self.output_file_edit.setText(output_file)  # Update display
            
        # Start conversion in worker thread
        self.conversion_worker = ConversionWorker(input_file, output_file, output_format)
        self.conversion_worker.finished.connect(self.on_conversion_finished)
        self.conversion_worker.error.connect(self.on_conversion_error)
        self.conversion_worker.progress.connect(self.update_progress)
        
        # UI updates
        self.convert_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.statusBar().showMessage("Converting...")
        
        self.log_message(f"Starting conversion: {Path(input_file).name} → {output_format.upper()}")
        
        self.conversion_worker.start()
        
    def update_progress(self, value: int):
        """Update the progress bar."""
        self.progress_bar.setValue(value)
        
    def on_conversion_finished(self, message: str):
        """Handle successful conversion completion."""
        self.log_message(f"✓ {message}")
        self.show_success(message)
        self.reset_ui()
        
    def on_conversion_error(self, error_message: str):
        """Handle conversion error."""
        self.log_message(f"✗ {error_message}")
        self.show_error(error_message)
        self.reset_ui()
        
    def reset_ui(self):
        """Reset UI elements after conversion."""
        self.convert_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
        self.statusBar().showMessage("Ready to convert files")
        
    def log_message(self, message: str):
        """Add a message to the log area."""
        self.log_text.append(f"[{self.get_timestamp()}] {message}")
        
    def get_timestamp(self):
        """Get current timestamp for logging."""
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
        
    def show_success(self, message: str):
        """Show success message dialog."""
        QMessageBox.information(self, "Success", message)
    def show_error(self, message: str):
        """Show error message dialog."""
        QMessageBox.critical(self, "Error", message)
    
    def _fix_output_extension(self, output_file: str, output_format: str) -> str:
        """Fix output file extension based on selected format."""
        output_path = Path(output_file)
        
        # Map format to extension
        format_extensions = {
            'json': '.json',
            'yaml': '.yaml', 
            'xml': '.xml'
        }
        
        correct_extension = format_extensions.get(output_format, '.txt')
        
        # If extension doesn't match format, change it
        if output_path.suffix.lower() != correct_extension:
            # Remove current extension and add correct one
            name_without_ext = output_path.stem
            new_path = output_path.parent / f"{name_without_ext}{correct_extension}"
            return str(new_path)
        
        return output_file


def main():
    """Main function to run the GUI application."""
    app = QApplication(sys.argv)
    app.setApplicationName("Data Format Converter")
    
    # Create and show the main window
    window = FormatConverterGUI()
    window.show()
    
    # Run the application
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
