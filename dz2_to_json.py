import json


def to_json(func):

    '''Decorator converts the return value of 'func' to JSON if it's a dict'''

    def decorated(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Return type in {} is {}'.format(func.__name__, type(result)))
        if isinstance(result, dict):
            with open('log_to_json.txt', 'w') as wf:
                result = json.dump(result, wf, indent=4, sort_keys=True)
        return result

    return decorated


@to_json
def test_dict_func():

    '''This function returns dict'''

    test_dict = {'key_2': 'value_1', 'key_3': 2, 'key_1': ('hello', 'world')}
    return test_dict


@to_json
def test_nondict_func():

    '''This function returns some types except dict'''

    test_list = [1, 2, 3, 4, 5]
    return test_list


if __name__ == '__main__':
    result_in_json = test_dict_func()
    default_result = test_nondict_func()
    print('After invokings:')
    print("Type of 'result_in_json' is {}".format(type(result_in_json)))
    print("Type of 'default_result' is {}".format(type(default_result)))
