"""Handles all the calculations for the calculator."""


class Logic:
    """The brain of the calculator, and all functions in this class."""

    def __init__(self, display):
        """Initialise the Logic."""
        self.display = display  # The display of the calculator, to be updated
        self.input_num = None  # The number currently being typed
        self.stored_num = None  # The other number being stored in memory
        self.operator = None  # The operator to be used
        self.button = None  # The button that was pressed

    def button_press(self, button):
        """Handle the button press."""
        self.button = button.text()  # The button pressed
        # Subdefining the buttons into different functions
        if self.button in ['0', '1', '2', '3', '4', '5', '6', '7',
                           '8', '9', '.']:
            self.number_button()
        if self.button in ['+', '-', '×', '÷']:
            self.operator_button()
        if self.button in ['+/-', 'x²', '√x', '1/x']:
            self.operator_single_input()  # Calculates right away
        if self.button in ['⌫', 'CE', 'C']:
            self.clear_button()
        if self.button == '=':
            if None not in [self.input_num, self.stored_num, self.operator]:
                # If any of the 3 are not defined, can't do the calculation
                self.calculate()
                # Displaying the newly calculated result
                self.display.setText(str(self.stored_num))

    def calculate(self):
        """Calculate with operators using 2 numbers as input."""
        self.input_num = float_check(self.input_num)  # Convert input to number
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
        self.stored_num = float_check(self.stored_num)
        self.input_num = None
        self.operator = None

    def number_button(self):
        """Pressing a number button, or a comma button."""
        if self.input_num is None:
            # When no number is typed yet
            if self.operator is None and self.stored_num is not None:
                # When typing a new number, after using equals on another calc
                self.stored_num = None
            if self.button == '0':
                # Can't have 0 at the start
                self.display.setText('0')  # Does reset display
                return
            elif self.button == '.':
                # Can't have a decimal point without anything in front
                self.input_num = '0.'
            else:
                # Sets the number to the typed one
                self.input_num = self.button
        elif self.button == '.' and '.' in self.input_num:
            # Can't have multiple decimal points
            return
        else:
            # Appends the button pressed to the existing number
            self.input_num += self.button
        # Displays the number currently being typed
        self.display.setText(self.input_num)

    def operator_button(self):
        """Pressing an operator button, that uses two numbers."""
        if self.input_num is None and self.stored_num is None:
            # The opertor can't be the first thing you type
            return
        elif self.input_num is not None:
            if self.stored_num is None:
                # Moving the input number to storage, to allow new input
                self.stored_num = float_check(self.input_num)
                self.input_num = None
            else:
                # When you click an operator after putting in a full equation
                self.calculate()  # Will calculate previous calculation first
        # Assigns the new operator, or reassigns it when you change operator
        self.operator = self.button
        # Updates the display, to show both the number and the operator
        self.display.setText(str(self.stored_num) + self.operator)

    def operator_single_input(self):
        """Pressing an operator button, that uses one number, giving result."""
        def operations(num, operator):
            # Processes the different operations
            if operator == '+/-':
                # Toggles between negative and positive
                result = num * -1
            elif operator == 'x²':
                # Squares the number
                result = num ** 2
            elif operator == '√x':
                # Squareroots the number
                result = num ** 0.5
            elif operator == '1/x':
                # Inverses the number (1 divided by the number)
                result = 1 / num
            return float_check(result)
        if self.input_num is not None:
            # Runs the operation on the input number as a priority
            # Converts to number for the functions, then back to string
            self.input_num = float_check(self.input_num)
            self.input_num = str(operations(self.input_num, self.button))
            self.display.setText(self.input_num)
        elif self.stored_num is not None and self.operator is None:
            # If the input number isn't defined, will use stored instead
            # Only if result of previous calc, so not if a new operator is used
            self.stored_num = operations(self.stored_num, self.button)
            self.display.setText(str(self.stored_num))
        # If neither is defined, won't do anything

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
