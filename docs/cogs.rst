.. currentmodule:: tg_botting

.. _tg_api_cogs:

Cogs
======

There comes a point in your bot's development when you want to organize a collection of commands, listeners, and some state into one class. Cogs allow you to do just that.

The gist:

- Each cog is a Python class :class:`.Cog`.
- Every command is marked with the :func:`.cog.command` decorator.
- Every listener is marked with the :meth:`.cog.listener` decorator.
- Cogs are then registered with the :meth:`.Bot.add_cog` call.

Quick Example
---------------

This example cog defines a ``Greetings`` category for your commands, with a single :ref:`command <tg_api_commands>` named ``hello`` as well as a listener to listen to an :ref:`Event <tg_api_events>`.

.. code-block:: python3

    from tg_botting.cog import Cog, command, lisener

    class Greetings(Cog):
        def __init__(self, bot):
            self.bot = bot
            self._last_user = None

        @listener()
        async def on_new_member(self, message):
            user = message.new_chat_member
            # or user = message.new_chat_participant
            # I recommend using user = message.new_chat_member or message.new_chat_participant
            await message.send('Welcome {}!'.format(user.first_name))

        @command('hello')
        async def hello(self, message):
            """Says hello"""
            user_id = message.user.id
            # if you need, you can try to load user by pyrogram who has in tg-botting
            # user = await User.load(user_id)
            if self._last_user is None or self._last_user != user_id:
                await message.send('Hello {}!'.format(user.first_name))
            else:
                await message.send('Hello {}... This feels familiar.'.format(user.first_name))
            self._last_user = user_id

A couple of technical notes to take into consideration:

- All commands must now take a ``self`` parameter to allow usage of instance attributes that can be used to maintain state.

Cog Registration
-------------------

Once you have defined your cogs, you need to tell the bot to register the cogs to be used. We do this via the :meth:`~.bot.Bot.add_cog` method.

.. code-block:: python3

    bot.add_cog(Greetings(bot))

This binds the cog to the bot, adding all commands and listeners to the bot automatically.


Inspection
------------

Since cogs ultimately are classes, we have some tools to help us inspect certain properties of the cog.


To get a :class:`list` of commands, we can refer to dict inside the :class:`Bot` class

    >>> commands = bot.all_commands().get(cog_class_name)
    >>> print([c.name for c in commands])
