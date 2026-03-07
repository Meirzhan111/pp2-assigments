import os

os.makedirs("test_dir/sub_dir", exist_ok=True)

print("Directories created")

items = os.listdir(".")
print("Files and directories:")
for i in items:
    print(i)