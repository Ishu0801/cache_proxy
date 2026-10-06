import jwt
import os
from jwt.exceptions import InvalidTokenError

def decode_token(token):
    try:
        payload = jwt.decode(token,
                             os.environ.get("SECRET_TOKEN"),
                             algorithms = [os.environ.get("ALGORITHM")])
    except InvalidTokenError:
        return None

    sub = payload.get("sub")

    if sub:
        return sub

    return None
