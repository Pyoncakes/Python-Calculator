"""Creates a simple calculator with a GUI."""
from interface import Calculator
import sys
from PySide2.QtWidgets import QApplication


def main():
    """Initialise the calculator application with the Calculator widget."""
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    calc.setFixedSize(calc.size())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
