"""Handles all the calculations for the calculator."""


def calc(button, memory):
    """Processes the information supplied by the calculator."""
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    operators = {'+': 1, '-': 2, '×': 3, '÷': 4}  # Number saved in memory

    if button in numbers:
        if memory['override']:  # Typing a number in this case, will overwrite
            memory['override'] = False
            if button == '.':
                memory['display'] = '0.'  # Shouldn't write '.' without the 0
            else:
                memory['display'] = button  # Sets display to the first input
        elif button != '.' or '.' not in memory['display']:  # No double '.'
            memory['display'] += button  # If not overwrite, appends the input

    elif button == '⌫' and not memory['override']:
        memory['display'] = memory['display'][:-1]  # Removes one char
        if memory['display'] in ['', '0']:  # Marks when nothing is left
            memory['display'] = '0'
            memory['override'] = True

    elif button in ['CE', 'C']:
        # Clear Entry (CE) only clears display
        memory['display'] = '0'
        memory['override'] = True
        if button == 'C':
            # Clear Global (C) also clears the stored memory
            memory['stored'] = 0.0
            memory['operator'] = 0

    elif button == '+/-' and not memory['override']:
        if memory['display'][0] == '-':  # Changes to positive
            memory['display'] = memory['display'][1:]
        else:  # Changes to negative
            memory['display'] = '-' + memory['display']

    elif button in operators.keys():
        if not memory['operator'] or not memory['override']:
            if memory['operator']:  # When typing a new operation after 2nd num
                memory['display'] = maths(memory['stored'],
                                          float(memory['display']),
                                          memory['operator'])  # Calculates
            memory['operator'] = operators[button]  # Saves the operator as int
            memory['stored'] = float(memory['display'])  # Stores displayed num
            memory['display'] += button  # Displays the operator
            memory['override'] = True  # Next number clears display
        else:  # Changing the operation
            memory['operator'] = operators[button]  # Updates stored operator
            memory['display'] = memory['display'][:-1] + button  # Change disp.

    elif button == '=':
        memory['display'] = maths(memory['stored'], float(memory['display']),
                                  memory['operator'])  # Calculates
        # Clearing memory
        memory['operator'] = 0
        memory['override'] = True
        memory['stored'] = 0.0

    return memory  # Returns the modified memory back to the calculator


def maths(a, b, o):
    """Calculates operations."""
    if o == 1:  # plus operator
        result = a + b
    elif o == 2:  # minus operator
        result = a - b
    elif o == 3:  # mulitiplication operator
        result = a * b
    elif o == 4:  # division operator
        result = a / b

    # Checks if string displayed, needs to be an int or float
    if not result % 1:
        return str(int(result))
    else:
        return str(result)
