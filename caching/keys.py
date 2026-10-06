import hashlib

def key_genrater(path_param,query_param,jwt_sub):
    path_param = sorted(path_param)
    query_param = sorted(query_param)
    jwt_sub = sorted(jwt_sub)

    payload_string = path_param
    payload_string += "|:|"
    for key,value in query_param:
        payload_string += f"{key}={value}"
    payload_string += "|:|"
    payload_string += jwt_sub

    encoded = payload_string.encode()
    hash_object = hashlib.sha256(encoded)
    returnable_string = hash_object.hexdigest()

    return returnable_string