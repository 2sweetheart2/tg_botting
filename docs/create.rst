.. currentmodule:: vk_botting

.. _tg-intro:

Creating a Bot
========================

In order to work with the library and the Telegram Bot API in general, we must first create a Telegram Bot.

Creating a Bot is a pretty straightforward process.

Make sure that you have user_id and user_hash, as well as the bot token that issues @BotFather in Telegram

    .. warning::

        It should be worth noting that this token is essentially yours bot's
        password. You should **never** share this to someone else. In doing so,
        someone can log into your bot and do malicious things, such as removing
        wall posts, spamming messages or even banning all members.

        The possibilities are endless, so **do not share this token.**

        If you accidentally leaked your token, click the "Revoke current token" button as soon
        as possible. This revokes your old token and  then generate a new one.
        Now you need to use the new token to login.

And that's it. You now have a bot account and you can login with that token.
