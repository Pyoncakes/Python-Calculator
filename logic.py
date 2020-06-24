"""Handles all the calculations for the calculator."""


class Logic:
    def __init__(self, calc, display):
        self.calc = calc
        self.display = display
        self.input_num = None
        self.stored = None
        self.operator = None

    def button_press(self, button):
        print(button.text())
