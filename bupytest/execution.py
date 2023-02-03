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

import inspect
import importlib

import sys
import os


def _print_successful_test(
    info: dict, cls_test_name: str,
    name: str, module_name: str = None,
):
    if module_name:
        print(f'(\033[32m{info["time"]:.3f}\033[m) \033[30m{module_name}.{cls_test_name}.{name}\033[m')
    else:
        print(f'(\033[32m{info["time"]:.3f}\033[m) \033[30m{cls_test_name}.{name}\033[m')


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
        cls_test_name = test.__class__.__name__
        total_time = 0

        try:
            for _test in test.run():
                name = _test['function']
                total_time += _test['time']
                if print_module:
                    _print_successful_test(_test, cls_test_name, name, module_name)
                else:
                    _print_successful_test(_test, cls_test_name, name)

            print(f'\n\033[1;32mEverything working!\033[m (\033[33mfinished in \033[1;4m{total_time:.3f}\033[m)')
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

            print(f'\n\033[1;31mSomething is wrong...\033[m (\033[33mfinished in \033[1;4m{total_time:.3f}\033[m)')
            return False

    return True


def this():
    stack = inspect.stack()
    _test_file = stack[1].filename.replace('.py', '')
    _test_file_module = os.path.basename(_test_file)
    run_tests(_test_file_module)


def execute_module(module_name: str) -> bool:
    run_tests(module_name)
    return False


def execute_modules_dir(modules_dir: str):
    dirs = os.listdir(modules_dir)
    sys.path.insert(0, modules_dir)

    for i in dirs:
        if i.startswith('test_') and i.endswith('.py'):
            i = i.replace('.py', '')
            result = run_tests(i, package='.', print_module=True)
            if not result:
                return True

    return False
