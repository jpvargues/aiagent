import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from functions.write_file import write_file


def test_overwrite_lorem():
    """Test overwriting the lorem.txt file"""
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("✓ Test overwrite lorem.txt:")
    print(f"  Result: {result}\n")


def test_create_new_file_in_subdirectory():
    """Test creating a new file in a subdirectory"""
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("✓ Test create pkg/morelorem.txt:")
    print(f"  Result: {result}\n")


def test_write_outside_directory():
    """Test that writing outside the permitted directory returns an error"""
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("✓ Test write outside directory:")
    print(f"  Result: {result}\n")
    assert result.startswith("Error:"), "Expected error message"


if __name__ == "__main__":
    print("Running write_file tests...\n")
    test_overwrite_lorem()
    test_create_new_file_in_subdirectory()
    test_write_outside_directory()
    print("All tests passed!")
