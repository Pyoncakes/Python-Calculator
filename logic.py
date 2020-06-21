"""Handles all the calculations for the calculator."""


def calc(button, memory):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    operators = {'+': 1, '-': 2, '×': 3, '÷': 4}

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

    elif button == '⌫':
        memory['display'] = memory['display'][:-1]
        if memory['display'] in ['', '0']:
            memory['display'] = '0'
            memory['override'] = True

    elif button in ['CE', 'C']:
        memory['display'] = '0'
        memory['override'] = True
        if button == 'C':
            memory['stored'] = 0.0
            memory['operator'] = 0

    elif button in operators.keys():
        if not memory['operator'] or not memory['override']:
            if memory['operator']:
                memory['display'] = maths(memory['stored'],
                                          float(memory['display']),
                                          memory['operator'])
            memory['operator'] = operators[button]
            memory['stored'] = float(memory['display'])
            memory['display'] += button
            memory['override'] = True
        else:
            memory['operator'] = operators[button]
            memory['display'] = memory['display'][:-1] + button
            memory['override'] = True
            memory['stored'] = 0.0

    elif button == '=':
        memory['display'] = maths(memory['stored'], float(memory['display']),
                                  memory['operator'])
        memory['operator'] = 0
        memory['override'] = True
        memory['stored'] = 0.0

    return memory


def maths(a, b, o):
    if o == 1:
        result = a + b
    elif o == 2:
        result = a - b
    elif o == 3:
        result = a * b
    elif o == 4:
        result = a / b

    if not result % 1:
        return str(int(result))
    else:
        return str(result)
