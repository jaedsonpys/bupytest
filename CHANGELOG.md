# Change log of BuPyTest versions

# 0.1.0

- [BuPyTest 0.1.0 in PyPi](https://pypi.org/project/bupytest/0.1.0/)
- [BuPyTest 0.1.0 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/0.1.0)

## Additions

- `bupytest.UnitTest`: Test **multiple classes** in one file;
- `bupytest.BaseTest`: Sequential testing of **test methods**.

# 0.2.0

- [BuPyTest 0.2.0 in PyPi](https://pypi.org/project/bupytest/0.2.0/)
- [BuPyTest 0.2.0 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/0.2.0)

## Additions

- [`1a87f20`](https://github.com/jaedsonpys/bupytest/commit/1a87f20): Creating function to run tests from module;
- [`93fa68e`](https://github.com/jaedsonpys/bupytest/commit/93fa68e): Creating function to run all tests in a directory;
- [`17fadd0`](https://github.com/jaedsonpys/bupytest/commit/17fadd0): Adding argument parser.

## Fix

- [`0adf5f9`](https://github.com/jaedsonpys/bupytest/commit/0adf5f9): Insert "./" path in sys.path list

# 0.3.0

- [BuPyTest 0.3.0 in PyPi](https://pypi.org/project/bupytest/0.3.0/)
- [BuPyTest 0.3.0 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v0.3.0)

## Additions

- [`2400d4f`](https://github.com/jaedsonpys/bupytest/commit/2400d4f): Returning test result exit code;

## Fix

- [`19f2619`](https://github.com/jaedsonpys/bupytest/commit/19f2619): Adding GPL license to source code.

# 0.3.1

- [BuPyTest 0.3.1 in PyPi](https://pypi.org/project/bupytest/0.3.1/)
- [BuPyTest 0.3.1 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v0.3.1)
  
## Fix

- [`8540874`](https://github.com/jaedsonpys/bupytest/commit/8540874): Fixing "UnboundLocalError" exception by setting a default value to "result" variable.

# 1.0.0

- [BuPyTest 1.0.0 in PyPi](https://pypi.org/project/bupytest/1.0.0/)
- [BuPyTest 1.0.0 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.0.0)
  
## Improvements

- [`dd702e2`](https://github.com/jaedsonpys/bupytest/commit/dd702e2): Removing `-d` and `-m` flags from parser.

# 1.0.1

- [BuPyTest 1.0.1 in PyPi](https://pypi.org/project/bupytest/1.0.1/)
- [BuPyTest 1.0.1 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.0.1)
  
## Fix

- [`daf9415`](https://github.com/jaedsonpys/bupytest/commit/daf9415): Fixing error when testing module inside a directory.

# 1.0.2

- [BuPyTest 1.0.2 in PyPi](https://pypi.org/project/bupytest/1.0.2/)
- [BuPyTest 1.0.2 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.0.2)
  
## Fix

- [`2d9184b`](https://github.com/jaedsonpys/bupytest/commit/2d9184b): Updating dependencies in requirements.txt and setup script.

# 1.0.3

- [BuPyTest 1.0.3 in PyPi](https://pypi.org/project/bupytest/1.0.3/)
- [BuPyTest 1.0.3 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.0.3)
  
## Fix

- [`e5905e2`](https://github.com/jaedsonpys/bupytest/commit/e5905e2): Passing "." package in `run_tests` function.

# 1.1.0

- [BuPyTest 1.1.0 in PyPi](https://pypi.org/project/bupytest/1.1.0/)
- [BuPyTest 1.1.0 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.1.0)
  
## Fix

- [`15dfb35`](https://github.com/jaedsonpys/bupytest/commit/15dfb35): Raise `AssertionError` exception in assert methods;
- [`193021e`](https://github.com/jaedsonpys/bupytest/commit/193021e): Stop test when assert is wrong.

# 1.1.1

- [BuPyTest 1.1.1 in PyPi](https://pypi.org/project/bupytest/1.1.1/)
- [BuPyTest 1.1.1 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.1.1)
  
## Fix

- [`8e3da01`](https://github.com/jaedsonpys/bupytest/commit/8e3da01): Updating project requirements;
- [`f3fc341`](https://github.com/jaedsonpys/bupytest/commit/f3fc341): Updating requirements version.

# 1.2.0

- [BuPyTest 1.2.0 in PyPi](https://pypi.org/project/bupytest/1.2.0/)
- [BuPyTest 1.2.0 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.2.0)
  
## Improvements

- [`c7f4384`](https://github.com/jaedsonpys/bupytest/commit/c7f4384): Changing error and success log;
- [`3f8b10d`](https://github.com/jaedsonpys/bupytest/commit/3f8b10d): Changing final message;
- [`4c087a7`](https://github.com/jaedsonpys/bupytest/commit/4c087a7): Adding function to print successful tests;
- [`b57a2ab`](https://github.com/jaedsonpys/bupytest/commit/b57a2ab): Using `time.time()` function to get test time;
- [`bf02622`](https://github.com/jaedsonpys/bupytest/commit/bf02622): Removing unnecessary variable;
- [`2e161f4`](https://github.com/jaedsonpys/bupytest/commit/2e161f4): Print test time in failed test;
- [`49bac1f`](https://github.com/jaedsonpys/bupytest/commit/49bac1f): Handling `AssertionError` exception in `BaseTest.run`.

# 1.3.0

- [BuPyTest 1.3.0 in PyPi](https://pypi.org/project/bupytest/1.3.0/)
- [BuPyTest 1.3.0 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.3.0)
  
## Improvements

- [`84b6d11`](https://github.com/jaedsonpys/bupytest/commit/84b6d11): Use `_assert_error()` method in all assert methods;
- [`9394bce`](https://github.com/jaedsonpys/bupytest/commit/9394bce): Print just 3 decimal numbers in test time;
- [`dd634ea`](https://github.com/jaedsonpys/bupytest/commit/dd634ea): Print each finished test in real time;
- [`bc2c736`](https://github.com/jaedsonpys/bupytest/commit/bc2c736): Remove time from failed unit test;
- [`215a3e7`](https://github.com/jaedsonpys/bupytest/commit/215a3e7): Move assert methods to `BaseTest` class;
- [`0404118`](https://github.com/jaedsonpys/bupytest/commit/0404118): Improve `error_msg` condition;
- [`cc27cd6`](https://github.com/jaedsonpys/bupytest/commit/cc27cd6): Improve tests log;
- [`1a07f80`](https://github.com/jaedsonpys/bupytest/commit/1a07f80): Print total unit test time.

# 1.3.1

- [BuPyTest 1.3.1 in PyPi](https://pypi.org/project/bupytest/1.3.1/)
- [BuPyTest 1.3.1 in GitHub Release](https://github.com/jaedsonpys/bupytest/releases/tag/v1.3.1)
  
## Fixes

- [`dfc3d75`](https://github.com/jaedsonpys/bupytest/commit/dfc3d75): Rename main script file name;
- [`5c62b02`](https://github.com/jaedsonpys/bupytest/commit/5c62b02): Update project keywords and console scripts;
- [`42403ba`](https://github.com/jaedsonpys/bupytest/commit/42403ba): Print test total time if all tests are finished;
- [`528fc4d`](https://github.com/jaedsonpys/bupytest/commit/528fc4d): Update license copyright year.