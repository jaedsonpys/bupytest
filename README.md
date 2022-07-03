# BuPyTest - Unit Tests

BuPyTest is a library to perform **unit tests** on your code by classes. You can create tests using classes and run them together in a single file.

In version `0.2.0` you can:

- [x] Test **multiple classes** in one file;
- [x] Test using command line;
- [x] Test only one file using **command line**;
- [X] Test multiple files using **command line**;

You can install the **latest version** of BuPyTest using the `pip` package manager:

```commandline
pip install bupytest
```

## How to use

Here's a simple tutorial on how to use `bupytest` in your tests:

> In the base class `bupytest.BaseTest` all tests are executed in the order they were defined (sequential).

```python
import bupytest


class TestFoo(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

    def test_1(self):
        self.assert_true(True, message='A error ocurred')

    def test_2(self):
        false_value = ''
        self.assert_false(false_value, message='Empty string')


if __name__ == '__main__':
    bupytest.this()
```

With `bupytest`, you define test classes and the methods, which will be tested. To test a value, you can use the following methods of the `bupytest.UnitTest` class:

- `UnitTest.assert_true`: asserts a true value;
- `UnitTest.assert_false`: asserts a false value;
- `UnitTest.assert_expected`: asserts an expected value.

All test classes must **start with "Test"**, and all test class methods must **start with "test_"**.

At the end of the file, the `bupytest.this` method runs the test **in this** file. That is, all test classes in this file will be executed.

You can also define several other classes in the same file for testing:

```python
import bupytest


class TestFoo(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

    def test_1(self):
        self.assert_true(True, message='A error ocurred')

    def test_2(self):
        false_value = ''
        self.assert_false(false_value, message='Empty string')


class TestBar(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

    def test_1(self):
        self.assert_expected('hello', 'hello')


if __name__ == '__main__':
    bupytest.this()
```

### Command Line

`bupytest` also has a **command line** application available to run tests, the script is called `bupytest`, see some **commands** and **flags** (use `--help` to get help):

- `test`: this command tells you that a test will be run;
- `-m`: this flag informs that the test is a python module;
- `-d`: this flag informs that the test is a directory of test modules.

With the `-d` flag, each of the files starting with "test_" will be executed. See an example of testing a module:

```commandline
bupytest test -m test_cookiedb.py
```

Now testing multiple test modules inside a directory:

```commandline
bupytest test -d tests/
```

> The `-m` and `-d` flags require the module or directory name.

## License

```text
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
```

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.