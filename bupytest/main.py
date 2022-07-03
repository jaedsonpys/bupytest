from .execution import execute_module, execute_modules_dir
from argeasy import ArgEasy

import os


def main():
    parser = ArgEasy(
        project_name='BuPyTest',
        description='Perform fast and detailed unit tests with BuPyTest.',
        version='0.2.0'
    )

    parser.add_argument('test', 'Tests a module or a module directory', action='store_true')
    parser.add_flag('-d', 'Specifies that the path of "test" is a directory')
    parser.add_flag('-m', 'Specifies that the path of "test" is a module')
