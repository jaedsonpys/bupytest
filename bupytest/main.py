from .bupytest import UnitTest

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
