"""Creates a simple calculator with a GUI"""
from interface import Calculator
import sys
from PySide2.QtWidgets import QApplication

# Initialising the calculator application with the Calculator widget
app = QApplication(sys.argv)
calc = Calculator()
calc.show()
sys.exit(app.exec_())
