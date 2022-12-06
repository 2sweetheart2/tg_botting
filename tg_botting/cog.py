def command(name,ignore_filter=False):
    def decorator(func):
        setattr(func, '__command__', name)
        setattr(func, '__ignore_filter__', ignore_filter)
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
