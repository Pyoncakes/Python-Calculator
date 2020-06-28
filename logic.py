"""Handles all the calculations for the calculator."""
from decimal import Decimal as dec


class Logic:
    """The brain of the calculator, and all functions in this class."""

    def __init__(self, display):
        """Initialise the Logic."""
        self.display = display  # The display of the calculator, to be updated
        self.input_num = dec(0)  # The number currently being typed
        self.decimal = None  # nr. of decimals, None if no decimal point
        self.stored_num = None  # The other number being stored in memory
        self.operator = None  # The operator to be used
        self.button = None  # The button that was pressed

    def button_press(self, button):
        """Handle the button press."""
        try:
            self.button = button.text()  # The button pressed
            # Subdefining the buttons into different functions
            if self.button in ['0', '1', '2', '3', '4', '5', '6', '7',
                               '8', '9']:
                self.number_button()
            elif self.button == '.':
                self.decimal_button()
            elif self.button == '+/-':
                self.negative_button()
            elif self.button in ['+', '-', '×', '÷']:
                self.operator_button()
            elif self.button in ['x²', '√x', '1/x']:
                self.operator_single_input()  # Calculates right away
            elif self.button == '%':
                self.percent_button()  # Similar to single input op
            elif self.button in ['⌫', 'CE', 'C']:
                self.clear_button()
            elif self.button == '=':
                if None not in [self.input_num, self.stored_num,
                                self.operator]:
                    # If any of the 3 are not defined, can't do the calculation
                    self.calculate()
        except ZeroDivisionError:
            self.display.setText('ERROR: divide by 0')

    def calculate(self):
        """Calculate with operators using 2 numbers as input."""
        # Processing the different operators
        if self.operator == '+':
            self.stored_num = self.stored_num + self.input_num
        elif self.operator == '-':
            self.stored_num = self.stored_num - self.input_num
        elif self.operator == '×':
            self.stored_num = self.stored_num * self.input_num
        elif self.operator == '÷':
            self.stored_num = self.stored_num / self.input_num
        # Result being stored in stored_num and input_num getting cleared
        self.stored_num = self.stored_num.normalize()
        self.input_num = dec(0)
        self.operator = None
        # Displaying the newly calculated result
        self.display.setText(str(self.stored_num))

    def number_button(self):
        """Pressing a number button, appends the input number."""
        number = int(self.button)  # Number to be appended
        input = self.input_num.as_tuple()  # input_num as a named tuple
        if self.input_num.is_zero() and self.decimal is None:
            # When no number is typed yet, sets the number to the typed one
            input = input._replace(digits=(number,))
            if self.operator is None and self.stored_num is not None:
                # When typing a new number, after using equals on another calc
                self.stored_num = None
        else:
            # Appends the button pressed to the existing number
            input = input._replace(digits=input.digits + (number,))
            if self.decimal is not None:
                # Moves the decimal if needed
                self.decimal += 1
                input = input._replace(exponent=-self.decimal)
        # Updates the input number
        self.input_num = dec(input)
        # Displays the number currently being typed
        self.display.setText(str(self.input_num))

    def decimal_button(self):
        """Pressing the decimal button, converts input to decimal."""
        if self.decimal is None:
            self.decimal = 0
            self.display.setText(str(str(self.input_num) + '.'))

    def negative_button(self):
        """Pressing the negative toggle button, toggles negative/positive."""
        input = self.input_num.as_tuple()
        input = input._replace(sign=not input.sign)
        self.input_num = dec(input)
        self.display.setText(str(self.input_num))

    def operator_button(self):
        """Pressing an operator button, that uses two numbers."""
        if self.stored_num is None:
            # Moving the input number to storage, to allow new input
            self.stored_num = self.input_num
            self.input_num = dec(0)
            self.decimal = None
        else:
            # When you click an operator after putting in a full equation
            self.calculate()  # Will calculate previous calculation first
        # Assigns the new operator, or reassigns it when you change operator
        self.operator = self.button
        # Updates the display, to show both the number and the operator
        self.display.setText(str(self.stored_num) + self.operator)

    def operator_single_input(self):
        """Pressing an operator button, that uses one number, giving result."""
        def calc(num, operator=self.button):
            # Processes the different operations
            if operator == 'x²':
                # Squares the number
                result = num ** 2
            elif operator == '√x':
                # Squareroots the number
                result = num.sqrt()  # Decimal module functionality
            elif operator == '1/x':
                # Inverses the number (1 divided by the number)
                result = 1 / num
            return result.normalize()
        if self.input_num.is_zero():
            if self.stored_num is None:
                # Only input_num is defined, will put answer in stored
                self.stored_num = calc(self.input_num, self.button)
                # Displaying result
                self.display.setText(str(self.stored_num))
            else:
                # Both are defined, will calculate first
                self.calculate()
                self.stored_num = calc(self.stored_num, self.button)
                self.display.setText(str(self.stored_num))
        elif self.stored_num is not None and self.operator is None:
            # Calculates on a previous result
            self.stored_num = calc(self.stored_num, self.button)
            self.display.setText(str(self.stored_num))
        # Any other case, won't work (including no number defined, or mid calc)

    def percent_button(self):
        """Pressing the percent button, lot's of features, calculates."""
        if self.input_num.is_zero():
            if self.stored_num is not None and self.operator is None:
                # Converts previous result to percent
                self.stored_num = self.stored_num / 100
                self.display.setText(str(self.stored_num))
            # Any other case without input number, won't do anything
        else:
            # There is an input number
            if self.operator is None:
                # If no operator shown, will just display percent of input num
                self.stored_num = self.input_num / 100
                self.input_num = dec(0)
                self.display.setText(str(self.stored_num))
            else:
                # When there is an operator, does the calculation
                if self.operator in ['+', '-']:
                    # Adds or subtracts a percentage (inp) of the num (stored)
                    self.input_num = self.stored_num * (self.input_num / 100)
                    self.calculate()
                elif self.operator in ['×', '÷']:
                    # Finds the percentage (inp) of the number (stored)
                    # Or divides by the percentage, not sure if feature needed
                    self.input_num = self.input_num / 100
                    self.calculate()

    def clear_button(self):
        """Pressing a clearing button(backspace, clear entry, global clear)."""
        if self.button == '⌫':
            # Backspace, delete one char
            if self.input_num is None:
                # Can only affect input_num
                return
            self.input_num = self.input_num[:-1]  # Deletes the char
            if self.input_num in ['', '0', '-0']:
                # Any of these are effectively having deleted the whole number
                self.input_num = None
                self.display.setText('0')  # Displaying 0 (resetting)
            else:
                self.display.setText(self.input_num)  # Displaying the new num
        elif self.button == 'CE':
            # Clear entry, erases the current input number
            self.input_num = None
            self.display.setText('0')  # Displaying 0 (resseting)
        elif self.button == 'C':
            # Clear global, erasing entire memory
            self.input_num = None
            self.stored_num = None
            self.operator = None
            self.display.setText('0')  # Displaying 0 (resseting)


def float_check(n):
    """Check if the number is a float or int, and returns the correct type."""
    if float(n) % 1 == 0:
        return int(n)
    else:
        return float(n)
