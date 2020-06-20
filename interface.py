"""The program creating the main GUI acting as the interface."""
import sys
from PySide2 import QtWidgets as QW


class Calculator(QW.QWidget):  # The Calculator class is a custom QT Widget
    """The calculator widget, containing the actual calculator GUI."""

    def __init__(self, parent=None):
        QW.QWidget.__init__(self, parent)
        self.display = ''  # The string that the LCD displays (0 if empty)

        # The display, using LCDNumber to get a classic calculator feel
        self.lcd = QW.QLCDNumber(20)
        self.lcd.display(0)  # Initially sets the display to 0

        # Creating all the buttons in the calculator
        self.button_0 = QW.QPushButton('0')
        self.button_1 = QW.QPushButton('1')
        self.button_2 = QW.QPushButton('2')
        self.button_3 = QW.QPushButton('3')
        self.button_4 = QW.QPushButton('4')
        self.button_5 = QW.QPushButton('5')
        self.button_7 = QW.QPushButton('7')
        self.button_6 = QW.QPushButton('6')
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

        # Connects the buttons to their individual functions
        # Only using numbers for now, to showcase the simple concept
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

        # Using the Grid Layout, as the calculator buttons are nicely in a grid
        grid = QW.QGridLayout()
        grid.setRowMinimumHeight(1, 75)
        grid.addWidget(self.lcd, 1, 1, 1, -1)
        self.setLayout(grid)

        # A list of all the buttons, simplifying iterating through them
        # Put into sublist based on rows, to make it clearer where buttons are
        button_list = [
            [self.button_clear_entry, self.button_global_clear,
             self.button_backspace, self.button_divide],
            [self.button_7, self.button_8, self.button_9,
             self.button_multiply],
            [self.button_4, self.button_5, self.button_6, self.button_minus],
            [self.button_1, self.button_2, self.button_3, self.button_plus],
            [self.button_negative, self.button_0,
             self.button_decimal_point, self.button_equal]
        ]

        # Iterates through all the buttons
        for row, sublist in enumerate(button_list, 2):
            for column, button in enumerate(sublist, 1):
                button.setFixedHeight(50)
                # Puts buttons on the grid, based on positions in button_list
                grid.addWidget(button, row, column)

    def change_display(self, text):
        # Extends the lcd display, based on the number button pressed
        """Updates the display after button press."""
        self.display += text
        self.lcd.display(self.display)

    # Button handlers for the number buttons
    # Points to change_display with the button pressed as arg, extends display
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
