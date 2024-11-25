import os
import hashlib

def generate_sha256(file_path):
    """Generate SHA-256 hash for a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_integrity(file_paths):
    """Check integrity of files by generating their SHA-256 hashes."""
    for file_path in file_paths:
        if os.path.isfile(file_path):
            print(f"{file_path}: {generate_sha256(file_path)}")
        else:
            print(f"{file_path} does not exist.")

# Example usage
files_to_check = ["test.txt", "all codes.txt"]
check_integrity(files_to_check)
                