"""The program creating the main GUI acting as the interface."""

# Imports
import sys
from PySide2 import QtWidgets as QW


class Calculator(QW.QWidget):
    """The calculator widget, containing the actual calculator GUI."""

    def __init__(self, parent=None):
        QW.QWidget.__init__(self, parent)
        self.display = ''

        self.lcd = QW.QLCDNumber(20)
        self.lcd.display(0)

        self.button_0 = QW.QPushButton('0')
        self.button_1 = QW.QPushButton('1')
        self.button_2 = QW.QPushButton('2')
        self.button_3 = QW.QPushButton('3')
        self.button_4 = QW.QPushButton('4')
        self.button_5 = QW.QPushButton('5')
        self.button_6 = QW.QPushButton('6')
        self.button_7 = QW.QPushButton('7')
        self.button_8 = QW.QPushButton('8')
        self.button_9 = QW.QPushButton('9')
        self.button_negative = QW.QPushButton('+/-')
        self.button_decimal_point = QW.QPushButton('.')
        self.button_equal = QW.QPushButton('=')
        self.button_plus = QW.QPushButton('+')
        self.button_minus = QW.QPushButton('-')
        self.button_multiply = QW.QPushButton('×')
        self.button_divide = QW.QPushButton('÷')
        self.button_clear_entry = QW.QPushButton('CE')
        self.button_global_clear = QW.QPushButton('C')
        self.button_backspace = QW.QPushButton('⌫')
        self.button_0.clicked.connect(self.button_handler_0)
        self.button_1.clicked.connect(self.button_handler_1)
        self.button_2.clicked.connect(self.button_handler_2)
        self.button_3.clicked.connect(self.button_handler_3)
        self.button_4.clicked.connect(self.button_handler_4)
        self.button_5.clicked.connect(self.button_handler_5)
        self.button_6.clicked.connect(self.button_handler_6)
        self.button_7.clicked.connect(self.button_handler_7)
        self.button_8.clicked.connect(self.button_handler_8)
        self.button_9.clicked.connect(self.button_handler_9)

        grid = QW.QGridLayout()
        grid.addWidget(self.button_clear_entry, 2, 1)
        grid.addWidget(self.button_global_clear, 2, 2)
        grid.addWidget(self.button_backspace, 2, 3)
        grid.addWidget(self.button_divide, 2, 4)
        grid.addWidget(self.button_7, 3, 1)
        grid.addWidget(self.button_8, 3, 2)
        grid.addWidget(self.button_9, 3, 3)
        grid.addWidget(self.button_multiply, 3, 4)
        grid.addWidget(self.button_4, 4, 1)
        grid.addWidget(self.button_5, 4, 2)
        grid.addWidget(self.button_6, 4, 3)
        grid.addWidget(self.button_minus, 4, 4)
        grid.addWidget(self.button_1, 5, 1)
        grid.addWidget(self.button_2, 5, 2)
        grid.addWidget(self.button_3, 5, 3)
        grid.addWidget(self.button_plus, 5, 4)
        grid.addWidget(self.button_negative, 6, 1)
        grid.addWidget(self.button_0, 6, 2)
        grid.addWidget(self.button_decimal_point, 6, 3)
        grid.addWidget(self.button_equal, 6, 4)
        layout = QW.QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addLayout(grid)
        self.setLayout(layout)

    def change_display(self, text):
        """Updates the display after button press."""
        self.display += text
        self.lcd.display(self.display)

    def button_handler_0(self):
        self.change_display('0')

    def button_handler_1(self):
        self.change_display('1')

    def button_handler_2(self):
        self.change_display('2')

    def button_handler_3(self):
        self.change_display('3')

    def button_handler_4(self):
        self.change_display('4')

    def button_handler_5(self):
        self.change_display('5')

    def button_handler_6(self):
        self.change_display('6')

    def button_handler_7(self):
        self.change_display('7')

    def button_handler_8(self):
        self.change_display('8')

    def button_handler_9(self):
        self.change_display('9')


app = QW.QApplication(sys.argv)
calc = Calculator()
calc.resize(500, 250)
calc.show()
sys.exit(app.exec_())
