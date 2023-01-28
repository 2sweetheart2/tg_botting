.. currentmodule:: tg_botting

.. _tg_api_commands:

Commands
==========

One of the most appealing aspect of the library is how easy it is to define commands and
how you can arbitrarily nest commands to have a rich command system.

Commands are defined by attaching it to a regular Python function. The command is then invoked by the user using a similar
signature to the Python function.

For example, in the given command definition:

.. code-block:: python3

    @bot.command('foo')
    async def foo(message):
        await message.send('oof!')

With the following prefix (``$``), it would be invoked by the user via:

.. code-block:: none

    $ foo some text

A command must always have one parameter, ``message``, which is the :class:`.Message`.

Invocation Message
-------------------

As seen earlier, every command must take a single parameter, called the :class:`objects.Message`.

This parameter gives you access to something called the "invocation message". Essentially all the information you need to
know how the command was executed. It contains a lot of useful information:

- :attr:`.Message.user.id` to fetch the id of message author.
- :attr:`.Message.chat.id` to fetch id of conversation.
- :meth:`.Message.get_text()` to fetch the text of the message with out his name and prefix
- :meth:`.Message.send()` to send a message to the conversation the command was used in.

Error Handling
----------------

When our commands fail to parse we will, by default, receive a noisy error in ``stderr`` of our console that tells us
that an error has happened and has been silently ignored.

In order to handle our errors, we must use something called an error handler. There is a global error handler (listener),
who can called :func:`

In order to handle our errors, we must use something called an error handler. There is a global error handler, called
:func:`on_command_error`. This global error handler is called for every error reached.

Most of the time however, we want to handle an error local to the command itself. :func:`on_command_error` can also handle
this error

.. code-block:: python3

    @bot.command('ping',ignore_filter=True)
    async def ping(message)
        user = message.user
        print(0/2)
        await message.send('pong')

    @bot.listener(ignore_filter=True)
    async def on_command_error(message, command, exception):
        await message.reply(f"some error in {''.join(traceback.format_tb(exception.__traceback__))}")

The first parameter of the error handler is :class:`.Message`, because of which the error was caused,
the second parameter is :class:`.Command` - the command in which the error was caused,
and the third parameter is `Exception <https://docs.python.org/3/tutorial/errors.html >`_ - an error that was called in the command.

Unknow commands
-------------------

this method will be called when the user uses a command that the bot does't know.
Eg:

.. code-block:: python3

    @bot.listener()
    async def on_unknow_command(message):
        await message.reply('the bot doen't know this command, who called {message.text}')

also, almost all listeners and commands receive only one parameter as input :class:`.Message`.
You can find more about other handlers below.