import urllib.request
from os.path import exists
import sys

import bullscows as bc


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        # without length
        
        link = sys.argv[1]
        
        dictionary = None
        if exists(link):
            dictionary = open(link, 'r').readlines()
        else:
            with urllib.request.urlopen(link) as response:
                dictionary = response.read().decode('utf-8').split('\n')
        
        length = 5
        if len(sys.argv) >= 3:
            # with length
            length = int(sys.argv[2])
            
        print(bc.gameplay(bc.ask, bc.inform, dictionary))
    else:
        raise TypeError('Not enough arguments')