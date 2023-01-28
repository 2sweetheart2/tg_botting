.. currentmodule:: tg_botting

.. _intro:

Introduction
==============

This is the documentation for tg-botting, a library for Python to aid
in creating applications that utilise the Telegram Bot API.

Prerequisites
---------------

tg-botting works with Python 3.6.0 or higher. Support for earlier versions of Python
is not provided. Python 2.7 or lower is not supported.


.. _installing:

Installing
-----------

You can get the library directly from PyPI: ::

    python3 -m pip install -U tg-botting

If you are using Windows, then the following should be used instead: ::

    py -3 -m pip install -U tg-botting

Virtual Environments
~~~~~~~~~~~~~~~~~~~~~

Sometimes you want to keep libraries from polluting system installs or use a different version of
libraries than the ones installed on the system. You might also not have permissions to install libaries system-wide.
For this purpose, the standard library as of Python 3.3 comes with a concept called "Virtual Environment"s to
help maintain these separate versions.

A more in-depth tutorial is found on `Virtual Environments and Packages <https://docs.python.org/3/tutorial/venv.html>`_.

However, for the quick and dirty:

1. Go to your project's working directory:

    .. code-block:: shell

        $ cd your-bot-source
        $ python3 -m venv bot-env

2. Activate the virtual environment:

    .. code-block:: shell

        $ source bot-env/bin/activate

    On Windows you activate it with:

    .. code-block:: shell

        $ bot-env\Scripts\activate.bat

3. Use pip like usual:

    .. code-block:: shell

        $ pip install -U tg-botting

Congratulations. You now have a virtual environment all set up.

Basic Concepts
---------------

vk-botting revolves around the concept of :ref:`events <tg_api_events>`.
An event is something you listen to and then respond to. For example, when a message
happens, you will receive an event about it that you can respond to.

for find user_id and user_hash:

Visit https://my.telegram.org/apps and log in with your Telegram account.

Fill out the form with your details and register a new Telegram application.

Done. The API key consists of two parts: user_id and user_hash. Keep it secret.


A quick example to showcase how events work:

.. code-block:: python3

    from tg_botting.bot import Bot

    bot = Bot(['your','prefixs'], user_id, user_hash)

    @bot.listener()
    async def on_message_new(message):
        print(message.text)

    @bot.listener()
    async def on_start():
        print('start')

    bot.run(bot-token)
