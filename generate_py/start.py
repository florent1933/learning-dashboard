import sys

from es import *
from fixtures import *


if __name__ == '__main__':
    '''
    Argv :
    d: delete index
    c: create index
    f: create fixtures
    '''

    if(len(sys.argv) > 1):
        if "g" in sys.argv[1]:
            get_es()
        if "d" in sys.argv[1]:
            delete_es()
        if "c" in sys.argv[1]:
            create_es()
        if "f" in sys.argv[1]:
            create_fixtures()
    else:
        print("Miss parameters")
        print("g : get indexes from ES")
        print("d : delete indexes on ES")
        print("c : create indexes on ES")
        print("f : creates fixtures on ES")
