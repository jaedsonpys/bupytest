from datetime import datetime
from typing import Any

import inspect


class BaseTest:
    def __init__(self):
        self._test_methods = []
        self._finished_tests = {}
        self._failed_test = {}

    def _get_test_methods(self) -> list:
        test_methods = []
        for attr in self.__dir__():
            attr_obj = self.__getattribute__(attr)
            if attr.startswith('test_') and callable(attr_obj):
                test_methods.append(attr_obj)

        return test_methods

    def run(self):
        self._test_methods = self._get_test_methods()
        for test in self._test_methods:
            method_name = test.__name__
            start_time = datetime.now()
            test.__call__()
            finished_time = datetime.now()

            self._finished_tests[method_name] = {
                'start': start_time,
                'finish': finished_time
            }


class UnitTest(BaseTest):
    def __init__(self):
        super().__init__()

    def assert_true(self, value: Any, message: str):
        error_msg = f'{value} is not true : {message}'
        stack = inspect.stack()
        _test_name = stack[1].function
        _test_file = stack[1].filename

        if not value:
            self._failed_test[_test_name] = {
                'function': _test_name,
                'file': _test_file,
                'message': error_msg
            }


if __name__ == '__main__':
    pass
