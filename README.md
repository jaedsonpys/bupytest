# BuPyTest - Unit Tests

BuPyTest is a library to perform **unit tests** on your code by classes. You can create tests using classes and run them together in a single file.

With `bupytest`, you can implement [**git hooks**](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) to automatically run tests using [Command Line](#command-line).

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

## Command Line

`bupytest` also has a **command line** application available to run tests, the script is called `bupytest`, see some **commands** and **flags** (use `--help` to get help):

Just use the `test` command to test one module or a directory with multiple modules. Here is an example:

```commandline
bupytest test test_cookiedb.py
```

Now testing multiple test modules inside a directory:

```commandline
bupytest test tests/
```

To test multiple modules from a directory, as in the example above, the name of the modules to be tested **must** start with `test_`, otherwise the test **will not run. 

## License

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.