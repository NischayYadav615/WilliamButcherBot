import os

BOT_TOKEN = os.environ.get('6194546283:AAFveZy9kq4_V91G_XhI4591rN__JATvhCY')
API_ID = int(os.environ.get('24720215'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQF5M1cAVDiFkI5zDie44Vbgn8d_nXYdR3txtrNXb6mBvlVkmkNPnb4t-HroEu85GG6fncwRSpgoFywjWpiEk1raDlCXvseDhBYWuh2mcCcrmINz3wPIOQztAwZauOESaskbG1sl5aVPX80FArAkfhIPPgLwHu6PGn7B_Z9BEcBPKpDfxspc8u4ZMn2WTLIEJQrzJcpcnHcmz6IUYrI_tw0GFgT8B8bQWHXEJDnjFF_KKIr1zanV_27Djg-DjvxY0-aKwYsMOuqgH-AOk1TdXD3ppP-1s9YZr1QuzlT0HZ1Flr4zI3zT0voivLjqnjzbPFqqWV7ImppkswIgxio6PVObfIDvxgAAAAF3PrMGAA')
API_HASH = os.environ.get('c0d3395590fecba19985f95d6300785e')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('+919992120679')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '6295565062').split()))
LOG_GROUP_ID = int(os.environ.get('-657588737'))
GBAN_LOG_GROUP_ID = int(os.environ.get('-657588737'))
MESSAGE_DUMP_CHAT = int(os.environ.get('-657588737'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('mongodb+srv://Nischaybot:Nischaybot@cluster0.thf9kzz.mongodb.net/?retryWrites=true&w=majority')
ARQ_API_KEY = os.environ.get('XZCTKZ-STIPNM-VRKGOD-OAIYJV-ARQ')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
