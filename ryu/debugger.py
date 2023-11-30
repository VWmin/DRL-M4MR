import sys
from ryu.cmd import manager


def main():
    sys.argv.append(r'/home/fwy/Desktop/refer/DRL-M4MR/ryu/shortest_path_forwarding.py')
    sys.argv.append('--verbose')
    sys.argv.append('--enable-debugger')
    manager.main()


if __name__ == '__main__':
    main()
