from . import execution
from argeasy import ArgEasy

import os
import sys


def main():
    parser = ArgEasy(
        project_name='BuPyTest',
        description='Perform fast and detailed unit tests with BuPyTest.',
        version='0.2.0'
    )

    parser.add_argument('test', 'Tests a module or a module directory', action='store_true')
    parser.add_flag('-d', 'Specifies that the path of "test" is a directory')
    parser.add_flag('-m', 'Specifies that the path of "test" is a module')

    args = parser.get_args()

    if args.test:
        sys.path.insert(0, './')

        file = args.m
        directory = args.d

        if file:
            if os.path.isfile(file):
                file = file.replace('.py', '')
                execution.execute_module(file)
            else:
                print(f'\033[31merror: file "{file}" not found\033[m')
                return True
        elif directory:
            if os.path.isdir(directory):
                execution.execute_modules_dir(directory)
            else:
                print(f'\033[31merror: directory "{directory}" not found\033[m')
                return True
