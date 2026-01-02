from functions.get_file_content import get_file_content

# Test 1: lorem.txt (should be truncated)
print("get_file_content(\"calculator\", \"lorem.txt\"):")
result = get_file_content("calculator", "lorem.txt")
print(f"Length: {len(result)} characters")
if "truncated" in result:
    print("File was truncated (as expected)")
    print(f"Last 100 characters: ...{result[-100:]}")
else:
    print("ERROR: File should have been truncated!")
print()

# Test 2: main.py
print("get_file_content(\"calculator\", \"main.py\"):")
result = get_file_content("calculator", "main.py")
print(result)
print()

# Test 3: pkg/calculator.py
print("get_file_content(\"calculator\", \"pkg/calculator.py\"):")
result = get_file_content("calculator", "pkg/calculator.py")
print(result)
print()

# Test 4: /bin/cat (should error)
print("get_file_content(\"calculator\", \"/bin/cat\"):")
result = get_file_content("calculator", "/bin/cat")
print(result)
print()

# Test 5: non-existent file (should error)
print("get_file_content(\"calculator\", \"pkg/does_not_exist.py\"):")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(result)
