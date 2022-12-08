def command(name,aliases=None,usage=None,description=None, roles=None, ignore_filter=False):
    def decorator(func):
        setattr(func, '__command__', name)
        setattr(func, '__ignore_filter__', ignore_filter)
        if description:
            setattr(func,'description',description)
        if aliases:
            setattr(func,'aliases',aliases)
        if usage:
            setattr(func,'usage',usage)
        if roles:
            setattr(func,'roles',roles)
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
