"""Handles all the calculations for the calculator."""


class Logic:
    def __init__(self, display):
        self.display = display
        self.input_num = None
        self.stored = None
        self.operator = None
        self.button = None

    def button_press(self, button):
        self.button = button.text()  # The button pressed
        if button in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.number_button()

    def number_button(self):
        pass
