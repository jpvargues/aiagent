import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from functions.run_python_file import run_python_file


def test_main_py_no_args():
    """Test running main.py without arguments"""
    result = run_python_file("calculator", "main.py")
    print("✓ Test run main.py (no args):")
    print(result)
    print()


def test_main_py_with_args():
    """Test running main.py with calculator expression"""
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("✓ Test run main.py with args ['3 + 5']:")
    print(result)
    print()


def test_tests_py():
    """Test running tests.py"""
    result = run_python_file("calculator", "tests.py")
    print("✓ Test run tests.py:")
    print(result)
    print()


def test_relative_path_outside():
    """Test that relative path outside the directory returns an error"""
    result = run_python_file("calculator", "../main.py")
    print("✓ Test run ../main.py (outside directory):")
    print(result)
    print()
    assert result.startswith("Error:"), "Expected error message"


def test_nonexistent_file():
    """Test that nonexistent file returns an error"""
    result = run_python_file("calculator", "nonexistent.py")
    print("✓ Test run nonexistent.py:")
    print(result)
    print()
    assert result.startswith("Error:"), "Expected error message"


def test_non_python_file():
    """Test that non-Python file returns an error"""
    result = run_python_file("calculator", "lorem.txt")
    print("✓ Test run lorem.txt (not a Python file):")
    print(result)
    print()
    assert result.startswith("Error:"), "Expected error message"


if __name__ == "__main__":
    print("Running run_python_file tests...\n")
    test_main_py_no_args()
    test_main_py_with_args()
    test_tests_py()
    test_relative_path_outside()
    test_nonexistent_file()
    test_non_python_file()
    print("All tests completed!")
