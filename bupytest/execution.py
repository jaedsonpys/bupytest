import inspect
import importlib

import sys
import os


def get_class_test(module_name: str, package: str = None) -> list:
    module = importlib.import_module(module_name, package)
    module_dir = module.__dir__()
    class_list = []

    for obj in module_dir:
        if obj.startswith('Test'):
            class_list.append(module.__getattribute__(obj))

    return class_list


def run_tests(module_name: str, package: str = None, print_module: bool = False) -> bool:
    test_list = get_class_test(module_name, package)

    for test in test_list:
        test = test()
        has_error = test.run()

        cls_test_name = test.__class__.__name__
        finished_tests = test.get_finished_tests()

        for name, info in finished_tests.items():
            if print_module:
                print(f'\033[32m{module_name}.{cls_test_name}.{name}: {info["time"]} | OK\033[m')
            else:
                print(f'\033[32m{cls_test_name}.{name}: {info["time"]} | OK\033[m')

        if has_error:
            failed_test = test.failed_test
            name = failed_test['function']
            error_msg = failed_test['message']

            print('-' * 30)
            if print_module:
                print(f'\033[31m{module_name}.{cls_test_name}.{name}: {error_msg} | FAILED\033[m')
            else:
                print(f'\033[31m{cls_test_name}.{name}: {error_msg} | FAILED\033[m')
            return False

        print('-' * 30)

    return True


def this():
    stack = inspect.stack()

    _test_name = stack[1].function
    _test_file = stack[1].filename.replace('.py', '')
    _test_file_module = os.path.basename(_test_file)

    result = run_tests(_test_file_module)
    print('-' * 30)
    if not result:
        print('\033[1;31mFAILED.\033[m')
    else:
        print('\033[1;32mSUCCESS.\033[m')


def execute_module(module_name: str, msg: bool = True) -> bool:
    result = run_tests(module_name)
    if msg:
        print('-' * 30)
        if not result:
            print('\033[1;31mFAILED.\033[m')
        else:
            print('\033[1;32mSUCCESS.\033[m')

    return result


def execute_modules_dir(modules_dir: str):
    dirs = os.listdir(modules_dir)
    sys.path.insert(0, modules_dir)

    for i in dirs:
        if i.startswith('test_') and i.endswith('.py'):
            i = i.replace('.py', '')
            result = run_tests(i, package='.tests', print_module=True)
            if not result:
                print('-' * 30)
                print('\033[1;31mFAILED.\033[m')
                return None

    print('-' * 30)
    print('\033[1;32mSUCCESS\033[m')
