#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(raw_input())
    if N%2==0:
        if N>=2 and N <=5:
            print("Not Weird")
        elif N > 5 and N <=20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
