import shutil
import os

shutil.copy("sample.txt", "sample_copy.txt")

shutil.copy("sample.txt", "sample_backup.txt")
print("File copied and backup created")

if os.path.exists("sample_copy.txt"):
    os.remove("sample_copy.txt")
    print("sample_copy.txt deleted")
else:
    print("File not found")