from hashlib import sha256

def hashed(password):
    return sha256(password.encode('utf-8')).hexdigest()
