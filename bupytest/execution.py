import inspect
import importlib
import os


def get_class_test(module_name: str) -> list:
    module = importlib.import_module(module_name)
    module_dir = module.__dir__()
    class_list = []

    for obj in module_dir:
        if obj.startswith('Test'):
            class_list.append(module.__getattribute__(obj))

    return class_list


def run_tests(module_name: str) -> bool:
    test_list = get_class_test(module_name)

    for test in test_list:
        test = test()
        has_error = test.run()

        cls_test_name = test.__class__.__name__
        finished_tests = test.get_finished_tests()

        for name, info in finished_tests.items():
            print(f'\033[32m{cls_test_name}.{name}: {info["time"]} | OK\033[m')

        if has_error:
            failed_test = test.failed_test
            method_test_name = failed_test['function']
            error_msg = failed_test['message']

            print('-' * 30)
            print(f'\033[31m{cls_test_name}.{method_test_name}: {error_msg} | FAILED\033[m')
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
