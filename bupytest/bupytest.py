from datetime import datetime


class UnitTest:
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


if __name__ == '__main__':
    u = UnitTest()
