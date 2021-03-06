#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*(float(tip_percent)/100)
    tax = meal_cost*(float(tax_percent)/100)
    total = meal_cost + tip + tax
    print(int(round(total)))

if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    solve(meal_cost, tip_percent, tax_percent)
