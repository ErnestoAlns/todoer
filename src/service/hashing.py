import bcrypt

def hash_passw(password):
    pass_encode = password.encode('utf-8')
    hashed = bcrypt.hashpw(pass_encode, bcrypt.gensalt())

    return hashed.decode('utf-8')

def passw_auth(password, passw_hash):
    try:
        passw_encode = password.encode('utf-8')
        hashp_encode = passw_hash.encode('utf-8')

        return bcrypt.checkpw(passw_encode, hashp_encode)
    except ValueError:
        return False




