"""The program creating the main GUI acting as the interface."""

# Imports
import sys
from PySide2.QtWidgets import QApplication

app = QApplication(sys.argv)
sys.exit(app.exec_())
