from threading import _start_new_thread
import time

def _wait_for(bool, text, blinc, end, delay):
    print(text)
    i = 0
    while bool[0] > 0:
        print('\033[1A\033[{}C{}'.format(len(text), blinc[i % len(blinc)]))
        i += 1
        time.sleep(delay)
    print('\033[1A\033[{}C{}'.format(len(text), end))

def wait_for(bool, text, blinc=['-','/','|','\\'], end=' done!', delay=.7):
    _start_new_thread(_wait_for, (bool, text, ['-','/','|','\\'], ' done!', delay, ))
