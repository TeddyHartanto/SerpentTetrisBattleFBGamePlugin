from serpent.game import Game

from .api.api import WebTetrisAPI

from serpent.utilities import Singleton

from serpent.game_launchers.web_browser_game_launcher import WebBrowser


class SerpentWebTetrisGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "web_browser"
        kwargs["browser"] = WebBrowser.DEFAULT
        kwargs["window_name"] = "Play Tetris | Free Online Game | Tetris"
        kwargs["url"] = "https://tetris.com/play-tetris"

        super().__init__(**kwargs)

        self.api_class = WebTetrisAPI
        self.api_instance = None  # Will be instantiated, it's a singleton. Just call the property api

    @property
    def screen_regions(self):
        # TODO: [Low priority] make the names more generic?
        regions = {
            "MAIN_MENU_PLAY_BUTTON": (519, 824, 559, 1017),
            "MAIN_MENU_SELECT_LEVEL_BUTTON": (587, 834, 617, 1004),
            "HOLD": (376, 569, 468, 707),
            "SCORE": (686, 572, 718, 704),
            "LEVEL": (752, 572, 784, 704),
            "LINES": (818, 571, 850, 705),
            "NEXT": (377, 1136, 614, 1271),
            "BOARD": (310, 773, 890, 1070),  # mainly for play game context
            "HI_SCORE": (255, 389, 281, 532),
            "HI_SCORE_ENTER_INITIALS": (304, 422, 326, 498),
            "HI_SCORE_OK": (339, 438, 358, 482),
            "GAME_OVER_MAIN_MENU_BUTTON": (345, 420, 365, 452),
            "GAME_OVER_RETRY_BUTTON": (345, 467, 365, 498)
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
