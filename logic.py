"""Handles all the calculations for the calculator."""


def calc(button, memory):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

    if button in numbers:
        if memory['override']:
            memory['override'] = False
            if button == '.':
                memory['display'] = '0.'
            else:
                memory['display'] = button
        else:
            if button != '.' or '.' not in memory['display']:
                memory['display'] += button

    return memory
