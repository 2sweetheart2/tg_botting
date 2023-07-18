def flatten_error_dict(d, key=''):
    items = []
    for k, v in d.items():
        new_key = key + '.' + k if key else k

        if isinstance(v, dict):
            try:
                _errors = v['_errors']
            except KeyError:
                items.extend(flatten_error_dict(v, new_key).items())
            else:
                items.append((new_key, ' '.join(x.get('message', '') for x in _errors)))
        else:
            items.append((new_key, v))

    return dict(items)


class TGException(Exception):
    """Base exception class for tg_botting

    Ideally speaking, this could be caught to handle any exceptions thrown from this library.
    """
    pass


class TGApiError(TGException):
    """Exception for most of errors sent by TG API in responses"""
    pass


class CommandError(TGException):
    r"""The base exception type for all command related errors.

    This inherits from :exc:`TGException`.

    This exception and exceptions inherited from it are handled
    in a special way as they are caught and passed into a special event
    from :class:`.Bot`\, :func:`on_command_error`.
    """
    def __init__(self, message=None, *args):
        if message is not None:
            super().__init__(message, *args)
        else:
            super().__init__(*args)


class CommandNotFound(TGException):
    """Exception raised when a command is attempted to be invoked
    but no command under that name is found.

    This is not raised for invalid subcommands, rather just the
    initial main command that is attempted to be invoked.

    This inherits from :exc:`CommandError`.
    """
    pass


class DisabledCommand(CommandError):
    """Exception raised when the command being invoked is disabled.

    This inherits from :exc:`CommandError`
    """
    pass


class CommandOnCooldown(CommandError):
    """Exception raised when the command being invoked is on cooldown.
    This inherits from :exc:`CommandError`

    Attributes
    -----------
    cooldown: Cooldown
        A class with attributes ``rate``, ``per``, and ``type`` similar to
        the :func:`.cooldown` decorator.
    retry_after: :class:`float`
        The amount of seconds to wait before you can retry again.
    """
    def __init__(self, cooldown, retry_after):
        self.cooldown = cooldown
        self.retry_after = retry_after
        super().__init__('You are on cooldown. Try again in {:.2f}s'.format(retry_after))


class CheckFailure(CommandError):
    """Exception raised when the predicates in :attr:`.Command.checks` have failed.

    This inherits from :exc:`CommandError`
    """
    pass


class ClientException(TGException):
    """Exception that's thrown when an operation in the :class:`Client` fails.

    These are usually for exceptions that happened due to user input.
    """
    pass


class CommandInvokeError(CommandError):
    """Exception raised when the command being invoked raised an exception.
    This inherits from :exc:`CommandError`

    Attributes
    -----------
    original
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """
    def __init__(self, e):
        self.original = e
        super().__init__('Command raised an exception: {0.__class__.__name__}: {0}'.format(e))


class ArgumentError(CommandError):
    """The base exception type for errors that involve errors
    regarding arguments.

    This inherits from :exc:`CommandError`.
    """
    pass


class BadArgument(ArgumentError):
    """Exception raised when a parsing or conversion failure is encountered
    on an argument to pass into a command.

    This inherits from :exc:`ArgumentError`
    """
    pass


class BadUnionArgument(ArgumentError):
    """Exception raised when a :data:`typing.Union` converter fails for all
    its associated types.
    This inherits from :exc:`ArgumentError`

    Attributes
    -----------
    param: :class:`inspect.Parameter`
        The parameter that failed being converted.
    converters: Tuple[Type, ...]
        A tuple of converters attempted in conversion, in order of failure.
    errors: List[:class:`CommandError`]
        A list of errors that were caught from failing the conversion.
    """
    def __init__(self, param, converters, errors):
        self.param = param
        self.converters = converters
        self.errors = errors

        def _get_name(x):
            try:
                return x.__name__
            except AttributeError:
                return x.__class__.__name__

        to_string = [_get_name(x) for x in converters]
        if len(to_string) > 2:
            fmt = '{}, or {}'.format(', '.join(to_string[:-1]), to_string[-1])
        else:
            fmt = ' or '.join(to_string)

        super().__init__('Could not convert "{0.name}" into {1}.'.format(param, fmt))


class MissingRequiredArgument(ArgumentError):
    """Exception raised when parsing a command and a parameter
    that is required is not encountered.

    This inherits from :exc:`ArgumentError`

    Attributes
    -----------
    param: :class:`inspect.Parameter`
        The argument that is missing.
    """
    def __init__(self, param):
        self.param = param
        super().__init__('{0.name} is a required argument that is missing.'.format(param))


class TooManyArguments(ArgumentError):
    """Exception raised when the command was passed too many arguments and its
    :attr:`.Command.ignore_extra` attribute was not set to ``True``.

    This inherits from :exc:`ArgumentError`
    """
    pass


class ConversionError(ArgumentError):
    """Exception raised when a Converter class raises non-CommandError.
    This inherits from :exc:`CommandError`.

    Attributes
    ----------
    converter: :class:`conversions.Converter`
        The converter that failed.
    original
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """
    def __init__(self, converter, original):
        self.converter = converter
        self.original = original


class ExtensionError(TGException):
    """Base exception for extension related errors.

    This inherits from :exc:`TGException`.

    Attributes
    ------------
    name: :class:`str`
        The extension that had an error.
    """
    def __init__(self, message=None, *args, name):
        self.name = name
        m = message or 'Extension {!r} had an error.'.format(name)
        super().__init__(m, *args)


class ExtensionAlreadyLoaded(ExtensionError):
    """An exception raised when an extension has already been loaded.

    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        super().__init__('Extension {!r} is already loaded.'.format(name), name=name)


class ExtensionNotLoaded(ExtensionError):
    """An exception raised when an extension was not loaded.

    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        super().__init__('Extension {!r} has not been loaded.'.format(name), name=name)


class NoEntryPointError(ExtensionError):
    """An exception raised when an extension does not have a ``setup`` entry point function.

    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        super().__init__("Extension {!r} has no 'setup' function.".format(name), name=name)


class ExtensionFailed(ExtensionError):
    """An exception raised when an extension failed to load during execution of the module or ``setup`` entry point.

    This inherits from :exc:`ExtensionError`

    Attributes
    -----------
    name: :class:`str`
        The extension that had the error.
    original: :exc:`Exception`
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """
    def __init__(self, name, original):
        self.original = original
        fmt = 'Extension {0!r} raised an error: {1.__class__.__name__}: {1}'
        super().__init__(fmt.format(name, original), name=name)


class ExtensionNotFound(ExtensionError):
    """An exception raised when an extension is not found.

    This inherits from :exc:`ExtensionError`

    Attributes
    -----------
    name: :class:`str`
        The extension that had the error.
    original: :class:`NoneType`
        Always ``None`` for backwards compatibility.
    """
    def __init__(self, name, original):
        self.original = original
        fmt = 'Extension {0!r} could not be loaded.'
        super().__init__(fmt.format(name), name=name)


class UnexpectedQuoteError(ArgumentError):
    """An exception raised when the parser encounters a quote mark inside a non-quoted string.

    This inherits from :exc:`ArgumentError`.

    Attributes
    ------------
    quote: :class:`str`
        The quote mark that was found inside the non-quoted string.
    """
    def __init__(self, quote):
        self.quote = quote
        super().__init__('Unexpected quote mark, {0!r}, in non-quoted string'.format(quote))


class InvalidEndOfQuotedStringError(ArgumentError):
    """An exception raised when a space is expected after the closing quote in a string
    but a different character is found.

    This inherits from :exc:`ArgumentError`.

    Attributes
    -----------
    char: :class:`str`
        The character found instead of the expected string.
    """
    def __init__(self, char):
        self.char = char
        super().__init__('Expected space after closing quotation but received {0!r}'.format(char))


class ExpectedClosingQuoteError(ArgumentError):
    """An exception raised when a quote character is expected but not found.

    This inherits from :exc:`ArgumentError`.

    Attributes
    -----------
    close_quote: :class:`str`
        The quote character expected.
    """
    def __init__(self, close_quote):
        self.close_quote = close_quote
        super().__init__('Expected closing {}.'.format(close_quote))


class LoginError(ClientException):
    """Exception that's thrown when bot fails to login with provided token for some reason"""
    pass
