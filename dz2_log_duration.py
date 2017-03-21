from datetime import datetime
from functools import wraps


def log_duration(func):

    '''It's a decorator that prints the time of executing other functions'''

    @wraps(func)
    def decorated(*args, **kwargs):
        with open('function_execution_log.txt', 'w') as wf:
            log_string = 'File: ' + __file__ + '\n'
            log_string += 'Invoking function: ' + func.__name__ + '\n'
            log_string += 'Time of invoking: ' + datetime.now().__str__()
            wf.write(log_string)
        func(*args, **kwargs)

    return decorated


@log_duration
def test_function(name):

    '''This function is just for testing decorator'''

    print('Hello, {}!'.format(name))


if __name__ == '__main__':
    first_name = input('Enter your name here: ')
    test_function(first_name)
