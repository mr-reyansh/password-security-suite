import bcrypt

def hash_bcrypt(password):

    salt=bcrypt.gensalt()

    hashed=bcrypt.hashpw(password.encode(),salt)

    return hashed.decode()