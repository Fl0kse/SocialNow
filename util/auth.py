from functools import wraps


def authenticated(f):
    @wraps(f)
    async def decorated(request):
        user_id = None
        return f(request, user_id)
    return decorated