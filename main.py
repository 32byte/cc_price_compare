import instant_gaming
import steam
import g2a

import wait_util
import time

def get_prices(query, dlc=False, max=3):
    out = []
    try:
        waiting = [True]
        
        wait_util.wait_for(waiting, 'Connecting to instant-gaming ')
        out += instant_gaming.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        pass
    try:
        waiting = [True]
        wait_util.wait_for(waiting, 'Connecting to steam ')
        out += steam.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        pass
    try:
        waiting = [True]
        wait_util.wait_for(waiting, 'Connecting to g2a ')
        out += g2a.get_prices(query, dlc, max)
        waiting[0] = False
        time.sleep(.8)
    except Exception:
        pass
    return out