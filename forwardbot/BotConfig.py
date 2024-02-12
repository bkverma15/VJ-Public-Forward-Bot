from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "23167032")
    API_HASH = environ.get("API_HASH", "8ce105e6b601d979e9c61058aefa9602")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6922036916:AAHod6WEiUf70eq6ytG2P1uRrk6__uQ-xHU")
    STRING_SESSION = environ.get("STRING_SESSION", "1BVtsOKgBuxPHD4Y4E14RcX4C64XcSvdapsWtv9yapAZmslE_v7hn_8ahYo6193JcaX7R4Cr_kER7PVdyCKa0Yz4J6TFBe0486Df18znTByKPJnxhzpMyVq15b5s8vuBI7DrpS1Oc0KKs2lvHbKZ0YVTeCkJLXc8l3E9CF1TzXjK7dgTF5gqKHhw-5pT6NYxOF7L0aOXu_xTtR1Tn3fHrpozxjezJ24D-JOlpchWC60Mkz7xGmpNW74zq6wUTZgwSHiJd-0T07aH_0hbZnyDh4NH1L10BylkeZUU-XqD7B8lNAgDFCNu9gghQfBz4fGZYPBFkUQoBlzlCrJ5XLrn1l04AE_sTllw=")
    SUDO_USERS = environ.get("SUDO_USERS", "6466507994")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@KingVJ01**
    """
