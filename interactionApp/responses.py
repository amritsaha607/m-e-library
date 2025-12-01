def bake_response(message: str):
    return {
        'status': message,
    }


RESPONSE_OK = bake_response('OK')
RESPONSE_UNAUTHORIZED = bake_response('Unauthorized Request')
