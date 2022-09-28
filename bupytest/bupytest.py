# BuPyTest
# Copyright (C) 2022  Jaedson Silva
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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

            if self.failed_test:
                return True

            second_time = str(finished_time.second - start_time.second)
            microseconds_time = str(finished_time.microsecond - start_time.microsecond)

            if len(second_time) == 1:
                second_time = '0' + second_time

            self._finished_tests[method_name] = {
                'time': f'{second_time}.{microseconds_time[:2]}'
            }

        return False


class UnitTest(BaseTest):
    def __init__(self):
        super().__init__()

    def assert_true(self, value: Any, message: str = None):
        if message:
            error_msg = message
        else:
            error_msg = f'{value} is not true'

        stack = inspect.stack()
        _test_name = stack[1].function
        _test_file = stack[1].filename

        if not value:
            self.failed_test = {
                'function': _test_name,
                'file': _test_file,
                'message': error_msg
            }

            raise AssertionError(error_msg)

    def assert_false(self, value: Any, message: str = None):
        if message:
            error_msg = message
        else:
            error_msg = f'{value} is not true'

        stack = inspect.stack()
        _test_name = stack[1].function
        _test_file = stack[1].filename

        if value:
            self.failed_test = {
                'function': _test_name,
                'file': _test_file,
                'message': error_msg
            }

            raise AssertionError(error_msg)

    def assert_expected(self, value: Any, expected: Any, message: str = None):
        if message:
            error_msg = message
        else:
            error_msg = f'"{value}" is not "{expected}"'

        stack = inspect.stack()
        _test_name = stack[1].function
        _test_file = stack[1].filename

        if value != expected:
            self.failed_test = {
                'function': _test_name,
                'file': _test_file,
                'message': error_msg
            }

            raise AssertionError(error_msg)
