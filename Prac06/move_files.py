import shutil
import os

os.makedirs("folder1", exist_ok=True)
os.makedirs("folder2", exist_ok=True)

with open("folder1/test.txt", "w") as f:
    f.write("Example file")

shutil.copy("folder1/test.txt", "folder2/test_copy.txt")

shutil.move("folder1/test.txt", "folder2/test_moved.txt")

print("Files copied and moved")