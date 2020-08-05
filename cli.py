class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_data(data):
    data.sort(key=lambda tup:(tup[0].lower(), float(tup[1])))

    last = None
    for e in data:
        if last != e[0].lower():
            if last != None:
                print()
            print('{}{}:{}'.format(bcolors.HEADER, e[0], bcolors.ENDC))
            print('\t{}Price: {:>6} \tWebsite: {:<20}{}'.format(bcolors.OKGREEN, e[1], e[2], bcolors.ENDC))
        else:
            print('\t{}Price: {:>6} \tWebsite: {:<20}{}'.format(bcolors.WARNING, e[1], e[2], bcolors.ENDC))
        last = e[0].lower()

if __name__ == '__main__':
    import main

    print_data(main.get_prices('ark'))