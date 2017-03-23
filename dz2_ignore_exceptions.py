def ignore_exceptions(exception):

    '''Exception handler decorator'''

    def decorator(func):

        def wrapped(*args, **kwargs):

            '''When exception occures, this function sets the error_flag
               so the result will be None. Otherwise, the result will be
               a normal value returned by decorated function '''

            error_flag = False
            try:
                result = func(*args, **kwargs)
            except exception:
                error_flag = True
            return result if not error_flag else None

        return wrapped

    return decorator


@ignore_exceptions(IndexError)
def test_function():

    '''Get the value of list element that index is 5
       It will raise IndexError exception'''

    test_list = [1, 2, 3, 4, 5]
    some_element_value = test_list[5]
    return some_element_value


if __name__ == '__main__':
    check_value = test_function()
    print(check_value)
