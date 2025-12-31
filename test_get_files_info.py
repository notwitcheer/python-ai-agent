from functions.get_files_info import get_files_info

print("get_files_info(\"calculator\", \".\"):")
result = get_files_info("calculator", ".")
print("Result for current directory:")
for line in result.split("\n"):
    print(f"  {line}")

print("\nget_files_info(\"calculator\", \"pkg\"):")
result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
for line in result.split("\n"):
    print(f"  {line}")

print("\nget_files_info(\"calculator\", \"/bin\"):")
result = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(f"    {result}")

print("\nget_files_info(\"calculator\", \"../\"):")
result = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(f"    {result}")
