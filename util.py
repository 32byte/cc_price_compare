import urllib.parse

import utils.instant_gaming
import utils.steam
import utils.g2a
import utils.uplay

import utils.wait_util
import time


def get_prices(query, dlc=False, max=3):
    query = urllib.parse.quote_plus(query)

    out = []
    error = [False]
    try:
        error[0] = False
        waiting = [True]
        utils.wait_util.wait_for(waiting, error, 'Connecting to instant-gaming ')
        out += utils.instant_gaming.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        error[0] = True
        time.sleep(.8)
    try:
        error[0] = False
        waiting = [True]
        utils.wait_util.wait_for(waiting, error, 'Connecting to steam ')
        out += utils.steam.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        error[0] = True
        time.sleep(.8)
    try:
        error[0] = False
        waiting = [True]
        utils.wait_util.wait_for(waiting, error, 'Connecting to g2a ')
        out += utils.g2a.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        error[0] = True
        time.sleep(.8)
    try:
        error[0] = False
        waiting = [True]
        utils.wait_util.wait_for(waiting, error, 'Connecting to uplay ')
        out += utils.uplay.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        error[0] = True
        time.sleep(.8)
    return out
