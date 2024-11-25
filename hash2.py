import os
import hashlib
my_first_sha = "5e8546e5d3ec006d7c2b7ed9cd862ef525815aa9878dc6081caafff4c53253f5"
#this my_first_sha is the constant hash for my file to check 
def generate_sha256(file_path):
    """Generate SHA-256 hash for a file."""
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()  
# List of files to check
files_to_check = ["money.txt"]

for file_path in files_to_check:
    if os.path.isfile(file_path):
        print(f"{file_path}: {generate_sha256(file_path)}")
        if my_first_sha== generate_sha256(file_path): #this command is to crosscheck the new hash with the constant one
             print("file is okey")
        else:
            print("file tampared")
    else:
        print(f"{file_path} does not exist.")