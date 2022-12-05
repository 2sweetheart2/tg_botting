def command(name):
    def decorator(func):
        setattr(func, '__command__', name)
        return func

    return decorator


def listener():
    def decorator(func):
        setattr(func, '__listener__', func.__name__)
        return func

    return decorator


class Cog:
    def __init__(self, bot):
        self.bot = bot
