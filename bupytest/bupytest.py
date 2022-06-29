class UnitTest:
    def __init__(self):
        self.test_methods = []
        self.failed_test = {}

    def _get_test_methods(self) -> list:
        test_methods = []
        for attr in self.__dir__():
            attr_obj = self.__getattribute__(attr)
            if attr.startswith('test_') and callable(attr_obj):
                test_methods.append(attr_obj)

        return test_methods


if __name__ == '__main__':
    u = UnitTest()
