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
        name='BuPyTest',
        description='Perform fast and detailed unit tests with BuPyTest.',
        version='1.0.2'
    )

    parser.add_argument('test', 'Tests a module or a module directory')

    args = parser.parse()
    result = 0

    if args.test:
        sys.path.insert(0, './')
        filepath = args.test

        if os.path.isfile(filepath):
            filedir = os.path.dirname(filepath)
            filepath = filepath.replace('.py', '')

            if os.path.isdir(filedir):
                sys.path.insert(0, os.path.join('.', filedir))
                filepath = os.path.basename(filepath)

            result = execution.execute_module(filepath)
        elif os.path.isdir(filepath):
            result = execution.execute_modules_dir(filepath)
        else:
            print(f'\033[31merror: file or directory "{filepath}" not found\033[m')
            return 1

    return result
