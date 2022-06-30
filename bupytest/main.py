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
            print(f'\033[32m{module_name}.{cls_test_name}.{name}: {info["time"]} OK\033[m')

        if has_error:
            failed_test = test.failed_test
            method_test_name = failed_test['function']
            error_message = failed_test['message']

            print('-' * 30)
            print(f'\033[31mAssertion error:')
            print(f'\ttest: {module_name}.{cls_test_name}.{method_test_name}')
            print(f'\tmessage: {error_message}\033[m')
            return False

    return True


def main():
    stack = inspect.stack()

    _test_name = stack[1].function
    _test_file = stack[1].filename.replace('.py', '')
    _test_file_module = os.path.basename(_test_file)
