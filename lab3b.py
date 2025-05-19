#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: cshin9

def sum_numbers(number1, number2):
    total = int(number1) + int(number2)
    return total

def subtract_numbers(number1, number2):
    total = int(number1) - int(number2)
    return total

def multiply_numbers(number1, number2):
    total = int(number1) * int(number2)
    return total

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
