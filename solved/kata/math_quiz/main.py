# coding=utf-8
"""
Goals
Ask user randomly generated questions for each of the 4 operations.
exit on q
Keep score.

Advanced
- Use lambdas
- Deal with divide by 0 (i.e. don't let the game end, instead do a suitable recovery)
- Limit division to questions with whole number answers
- Deal with q, Q, Quit, "", quit, etc.
"""
#
#
# THIS IS A SOLVED SOLUTION. DON'T EDIT.
#
# If this is an interview, don't read this until you've solved your version.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import random

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

# level 1.5
def run():
    print("Math practice time")
    ops = [add,subtract,multiply,divide]
    a = random.randint(0,10)
    b = random.randint(0, 10)
    current_op = ops[random.randint(0,3)]
    answer = input( current_op.__name__ + " " + str(a) + " and " + str(b) +"?")
    if len(answer) ==0 or answer[0].upper()=="Q":
        return
    if int(answer) == current_op(a,b):
        print("right!")
    else:
        print("wrong! " + str(current_op(a,b)))
run()
