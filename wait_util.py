from threading import _start_new_thread
import time

def _wait_for(bool, err, text, blinc, end, errtxt, delay):
    print(text)
    i = 0
    while bool[0] and not err[0]:
        print('\033[1A\033[{}C{}'.format(len(text), blinc[i % len(blinc)]))
        i += 1
        time.sleep(delay)
    if err[0]:
        print('\033[1A\033[{}C{}'.format(len(text), '\033[91m' + errtxt + '\033[0m'))
    else:
        print('\033[1A\033[{}C{}'.format(len(text), '\033[92m' + end + '\033[0m'))

def wait_for(bool, err, text, blinc=['-','/','|','\\'], end='done!', errtxt='error!', delay=.7):
    _start_new_thread(_wait_for, (bool, err, text, blinc, end, errtxt, delay, ))
