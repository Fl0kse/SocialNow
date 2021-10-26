from functools import wraps


def authenticated(f):
    @wraps(f)
    async def decorated(request):
        ...
        return decorated
