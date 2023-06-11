import os

# get enviroment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Telegram user api token
TELEGRAM_API_ID = os.environ.get('API_ID')
TELEGRAM_API_HASH = os.environ.get('API_HASH')

# Telegram bot api token
TELEGRAM_BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Telethon session file
telethon_session_name = 'olx_ads_on_telegram/session_name'

base_url = "https://www.olx.com.br/estado-df?f=p&q="
most_recent_filter = "&sf=1"

olx_search_types = [
        "boardgames",
        "games",
        "ereader"
        ]

telegram_channel_list = {
        "boardgames": 'olxbgbr',
        "games": 'olxgp',
        "ereader": 'olxereade'
        }

olx_list_queries = {
        "boardgames": [
            "jogo%20tabuleiro",
            "board%20game",
            "galapagos%20jogo",
            "sleeve%20jogo",
            "jogo%20carta",
            "catan%20jogo",
            # "lego"
            ],
        "games": [
            "anbernic",
            "powkiddy",
            "caanoo",
            "retroid",
            "miyoo",
            "dingoo",
            "rgb10s",
            "3ds",
            "2ds",
            "nds",
            "nintendo 2ds",
            "nintendo ds",
            "nintendo 3ds"
            # "nintendo%20switch"
            ],
        "ereader": [
            "kindle",
            "kobo"
            ]

        }

olx_category_filters = {
        "boardgames": [
            "https://df.olx.com.br/distrito-federal-e-regiao/artigos-infantis",
            "https://df.olx.com.br/distrito-federal-e-regiao/hobbies-e-colecoes"
            ],
        "games": [
            "https://df.olx.com.br/distrito-federal-e-regiao/videogames",
            "https://df.olx.com.br/distrito-federal-e-regiao/computadores-e-acessorios"
            ],
        "ereader": [
            "https://df.olx.com.br/distrito-federal-e-regiao/computadores-e-acessorios",
            "https://df.olx.com.br/distrito-federal-e-regiao/livros-e-revistas"
            ]
        }

olx_search_exclude = [
        'star-wars',
        'bandeja',
        'bandai',
        'pokemon',
        'gamer',
        'taro',
        'xadrez',
        'dama',
        'pneu',
        'pneus',
        'lego'
        ]
