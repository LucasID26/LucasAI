HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    from os import environ

    STRING = environ["STRING"]
    API_ID = environ["API_ID"]
    API_HASH = environ["API_HASH"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]



# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.dev"
