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

import importlib
import inspect
import os
import sys
from typing import Tuple


def _print_successful_test(
    info: dict, cls_test_name: str,
    name: str, module_name: str = None,
):
    if module_name:
        print(f'(\033[32m{info["time"]:.3f}\033[m) \033[30m{module_name}.{cls_test_name}.{name}\033[m')
    else:
        print(f'(\033[32m{info["time"]:.3f}\033[m) \033[30m{cls_test_name}.{name}\033[m')


def _print_test_finish(time: float, success: bool):
    if success:
        print(f'\n\033[1;32mEverything working!\033[m (\033[33mfinished in \033[1;4m{time:.3f}\033[m)')
    else:
        print(f'\n\033[1;31mSomething is wrong...\033[m (\033[33mfinished in \033[1;4m{time:.3f}\033[m)')


def get_class_test(module_name: str, package: str = None) -> list:
    module = importlib.import_module(module_name, package)
    module_dir = module.__dir__()
    class_list = []

    for obj in module_dir:
        if obj.startswith('Test'):
            class_list.append(module.__getattribute__(obj))

    return class_list


def run_tests(module_name: str, package: str = None, print_module: bool = False) -> Tuple[bool, float]:
    test_list = get_class_test(module_name, package)
    total_time = 0

    for test in test_list:
        test = test()
        cls_test_name = test.__class__.__name__

        try:
            for _test in test.run():
                name = _test['function']
                total_time += _test['time']
                if print_module:
                    _print_successful_test(_test, cls_test_name, name, module_name)
                else:
                    _print_successful_test(_test, cls_test_name, name)
        except AssertionError:
            failed_test = test.failed_test
            name = failed_test['function']
            error_msg = failed_test['message']
            assert_line = failed_test['line_number']
            assert_test = failed_test['assertion']

            print()

            if print_module:
                print(f'(\033[1;31mFAILED\033[m) "{error_msg}" in \033[30m{module_name}.{cls_test_name}.{name}\033[m')
                print(f'    \033[30m{assert_line} |\033[m \033[31m{assert_test}\033[m')
            else:
                print(f'(\033[1;31mFAILED\033[m) "{error_msg}" in \033[30m{cls_test_name}.{name}\033[m')
                print(f'    \033[30m{assert_line} |\033[m \033[31m{assert_test}\033[m')

            return False, total_time

    return True, total_time


def this():
    stack = inspect.stack()
    _test_file = stack[1].filename.replace('.py', '')
    _test_file_module = os.path.basename(_test_file)
    result, time = run_tests(_test_file_module)
    _print_test_finish(time, result)


def execute_module(module_name: str) -> bool:
    result, time = run_tests(module_name)
    _print_test_finish(time, result)
    return False


def execute_modules_dir(modules_dir: str):
    dirs = os.listdir(modules_dir)
    sys.path.insert(0, modules_dir)
    total_time = 0

    for i in dirs:
        if i.startswith('test_') and i.endswith('.py'):
            i = i.replace('.py', '')
            result, time = run_tests(i, package='.', print_module=True)
            total_time += time
            if not result:
                _print_test_finish(total_time, result)
                return True

    _print_test_finish(total_time, True)
    return False
