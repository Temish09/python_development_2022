import figdate as fd
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(fd.date())
    else:
        print(fd.date(*sys.argv[1:]))
    