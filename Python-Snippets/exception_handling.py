"""
Exception handling in Python is a crucial programming concept that allows developers to gracefully manage, 
respond to unexpected errors or exceptional situations that may occur during program execution. 
It involves the use of try, except, else, and finally blocks to control the flow of code, 
ensure that the program continues to run even in the presence of errors.

Wikipedia: https://en.wikipedia.org/wiki/Exception_handling
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print('Division by zero is not allowed.')
except Exception as e:
    print(f'An error occurred: {e}')
else:
    print(f'Result: {result}')
finally:
    print('Execution completed.')
