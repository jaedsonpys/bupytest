from datetime import datetime
from typing import Any

import inspect


class BaseTest:
    def __init__(self):
        self._test_methods = []
        self._finished_tests = {}
        self.failed_test = {}

    def _get_test_methods(self) -> list:
        test_methods = []
        for attr in self.__dir__():
            attr_obj = self.__getattribute__(attr)
            if attr.startswith('test_') and callable(attr_obj):
                test_methods.append(attr_obj)

        return test_methods

    def get_finished_tests(self) -> dict:
        return self._finished_tests

    def run(self) -> bool:
        self._test_methods = self._get_test_methods()
        for test in self._test_methods:
            method_name = test.__name__
            start_time = datetime.now()
            test.__call__()
            finished_time = datetime.now()

            self._finished_tests[method_name] = {
                'time': finished_time - start_time
            }

            if self.failed_test:
                return True

        return False


class UnitTest(BaseTest):
    def __init__(self):
        super().__init__()

    def assert_true(self, value: Any, message: str):
        error_msg = f'{value} is not true : {message}'
        stack = inspect.stack()
        _test_name = stack[1].function
        _test_file = stack[1].filename

        if not value:
            self.failed_test = {
                'function': _test_name,
                'file': _test_file,
                'message': error_msg
            }

    def assert_false(self, value: Any, message: str):
        error_msg = f'{value} is not false : {message}'
        stack = inspect.stack()
        _test_name = stack[1].function
        _test_file = stack[1].filename

        if value:
            self.failed_test = {
                'function': _test_name,
                'file': _test_file,
                'message': error_msg
            }

    def assert_expected(self, value: Any, expected: Any, message: str):
        error_msg = f'{value} is not {expected} : {message}'
        stack = inspect.stack()
        _test_name = stack[1].function
        _test_file = stack[1].filename

        if value != expected:
            self.failed_test = {
                'function': _test_name,
                'file': _test_file,
                'message': error_msg
            }


if __name__ == '__main__':
    pass
