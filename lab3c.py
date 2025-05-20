#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: cshin9

def operate(number1, number2, operator):
    if operator == 'add':
        return int(number1) + int(number2)
    elif operator == 'subtract':
        return int(number1) - int(number2)
    elif operator == 'multiply':
        return int(number1) * int(number2)
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'
