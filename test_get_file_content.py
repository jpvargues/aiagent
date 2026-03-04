import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from functions.get_file_content import get_file_content
from config import MAX_CHARS


def test_lorem_truncation():
    """Test that lorem.txt is properly truncated at MAX_CHARS"""
    result = get_file_content("calculator", "lorem.txt")
    
    # Check that the content is truncated to MAX_CHARS
    assert len(result) > MAX_CHARS, f"Expected content longer than {MAX_CHARS}, got {len(result)}"
    
    # Check for truncation message
    assert "[...File" in result and "truncated at" in result, "Truncation message not found"
    
    print(f"✓ Lorem truncation test passed")
    print(f"  Content length: {len(result)} characters")
    print(f"  Last 100 characters: ...{result[-100:]}")


def test_main_py():
    """Test reading calculator/main.py"""
    result = get_file_content("calculator", "main.py")
    print(f"✓ Read calculator/main.py")
    print(f"  Content length: {len(result)} characters")
    print(f"  First 200 characters: {result[:200]}...\n")


def test_calculator_py():
    """Test reading calculator/pkg/calculator.py"""
    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"✓ Read calculator/pkg/calculator.py")
    print(f"  Content length: {len(result)} characters")
    print(result)


def test_bin_cat_error():
    """Test that accessing /bin/cat returns an error"""
    result = get_file_content("calculator", "/bin/cat")
    print(f"✓ Test /bin/cat error:")
    print(f"  Result: {result}\n")
    assert result.startswith("Error:"), "Expected error message"


def test_nonexistent_file_error():
    """Test that accessing non-existent file returns an error"""
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"✓ Test non-existent file error:")
    print(f"  Result: {result}\n")
    assert result.startswith("Error:"), "Expected error message"


if __name__ == "__main__":
    print("Running get_file_content tests...\n")
    test_lorem_truncation()
    print()
    test_main_py()
    test_calculator_py()
    test_bin_cat_error()
    test_nonexistent_file_error()
    print("All tests passed!")
