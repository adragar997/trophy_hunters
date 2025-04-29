import os

requirements = [
            {
                'url' : f'{os.getenv('URL_GAME_NEWS')}',
                'params': {
                    'key': f'{os.getenv('STEAM_API_TOKEN')}',
                    'appid': 500,
                }
            },
            {
                'url': f'{os.getenv('URL_SHOP_GAME')}',
                'params': {
                    'appids': 500,
                }
            },
            {
                'url': f'{os.getenv('URL_PLAYER_DETAILS')}',
                'params': {
                    'key': f'{os.getenv('STEAM_API_TOKEN')}',
                    'steamids': 76561198993274902,
                }
            }
        ]