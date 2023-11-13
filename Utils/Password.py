import bcrypt

config_bcrypt = bcrypt.gensalt()


def encode_password(password: str) -> bytes:
    return bcrypt.hashpw(bytes(password, encoding='utf-8')
                         , config_bcrypt)


def password_check(password_input, hashed_password):
    return bcrypt.checkpw(password_input.encode('utf-8'), hashed_password.encode('utf-8'))
