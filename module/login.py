from .bombScreen import *
from .logger import LoggerEnum, logger, logger_translated
from .config import Config
from .mouse import *
from .utils import *

class Login:
    def do_login(manager):
        current_screen = BombScreen.get_current_screen()
        logged = False
        
        if current_screen != BombScreenEnum.LOGIN.value and current_screen != BombScreenEnum.NOT_FOUND.value and current_screen != BombScreenEnum.POPUP_ERROR.value:
            logged = True

        if not logged:
            logger_translated("login", LoggerEnum.ACTION)

            login_attepmts = Config.PROPERTIES["screen"]["number_login_attempts"]
        
            for i in range(login_attepmts):
                
                if BombScreen.get_current_screen() != BombScreenEnum.LOGIN.value:
                    refresh_page()
                    BombScreen.wait_for_screen(BombScreenEnum.LOGIN.value)

                logger_translated("Login", LoggerEnum.PAGE_FOUND)

                logger_translated("wallet", LoggerEnum.BUTTON_CLICK)
                if not click_when_target_appears("button_connect_wallet"):
                    refresh_page()
                    continue

                logger_translated("Popup connect", LoggerEnum.BUTTON_CLICK)
                if not click_when_target_appears("button_popup_connect_wallet"):
                    refresh_page()
                    continue

                logger_translated("sigin wallet", LoggerEnum.BUTTON_CLICK)
                if not click_when_target_appears("button_connect_wallet_sign"):
                    refresh_page()
                    continue

                if (BombScreen.wait_for_screen(BombScreenEnum.HOME.value) != BombScreenEnum.HOME.value):
                    logger("🚫 Failed to login, restart proccess...")
                    continue
                else:
                    logger("🎉 Login successfully!")
                    logged = True
                    break

        manager.set_refresh_timer("refresh_login")
        return logged
