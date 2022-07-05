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

from . import execution
from argeasy import ArgEasy

import os
import sys


def main():
    parser = ArgEasy(
        project_name='BuPyTest',
        description='Perform fast and detailed unit tests with BuPyTest.',
        version='0.3.1'
    )

    parser.add_argument('test', 'Tests a module or a module directory', action='store_true')
    parser.add_flag('-d', 'Specifies that the path of "test" is a directory')
    parser.add_flag('-m', 'Specifies that the path of "test" is a module')

    args = parser.get_args()
    result = False

    if args.test:
        sys.path.insert(0, './')

        file = args.m
        directory = args.d

        if file:
            if os.path.isfile(file):
                file = file.replace('.py', '')
                result = execution.execute_module(file)
            else:
                print(f'\033[31merror: file "{file}" not found\033[m')
                return True
        elif directory:
            if os.path.isdir(directory):
                result = execution.execute_modules_dir(directory)
            else:
                print(f'\033[31merror: directory "{directory}" not found\033[m')
                return True

    return result
