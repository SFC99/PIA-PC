import hashlib

def Hash(file):
    with open(file, "rb") as f:
        byte = f.read()
        hash_text = hashlib.sha256(byte).hexdigest()
        print(hash_text)
