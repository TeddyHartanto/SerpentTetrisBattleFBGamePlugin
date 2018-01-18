from serpent.game import Game

from .api.api import TetrisBattleFBAPI

from serpent.utilities import Singleton

from serpent.game_launchers.web_browser_game_launcher import WebBrowser


class SerpentTetrisBattleFBGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "web_browser"
        kwargs["browser"] = WebBrowser.CHROME
        kwargs["window_name"] = "Play Tetris | Free Online Game | Tetris"
        kwargs["url"] = "https://tetris.com/play-tetris"

        super().__init__(**kwargs)

        self.api_class = TetrisBattleFBAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "MAIN_MENU": (277, 489, 922, 1355)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
