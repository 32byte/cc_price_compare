import urllib.parse

import util.instant_gaming as instant_gaming
import util.steam as steam
import util.g2a as g2a

import util.wait_util as wait_util
import time


def get_prices(query, dlc=False, max=3):
    query = urllib.parse.quote_plus(query)

    out = []
    error = [False]
    try:
        error[0] = False
        waiting = [True]
        wait_util.wait_for(waiting, error, 'Connecting to instant-gaming ')
        out += instant_gaming.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        error[0] = True
        time.sleep(.8)
    try:
        error[0] = False
        waiting = [True]
        wait_util.wait_for(waiting, error, 'Connecting to steam ')
        out += steam.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        error[0] = True
        time.sleep(.8)
    try:
        error[0] = False
        waiting = [True]
        wait_util.wait_for(waiting, error, 'Connecting to g2a ')
        out += g2a.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        error[0] = True
        time.sleep(.8)
    return out
