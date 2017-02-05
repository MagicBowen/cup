"""
cup : c++ unified package management tool.
"""

import argparse
import initcmd
import newcmd
import updatecmd
import movecmd



def main():
    parser = argparse.ArgumentParser(description = 'cup : c++ unified package management tool')
    subparsers = parser.add_subparsers(help = 'commands')

    init_parser = subparsers.add_parser('init', help = 'initialize a project')
    init_parser.add_argument('project', action = 'store', help = 'project name')
    init_parser.set_defaults(func = initcmd.run)

    new_parser = subparsers.add_parser('new', help = 'create files')
    new_parser.add_argument('file', action = 'store', help = 'file name')
    new_parser.add_argument('-i', '--include', action = 'store_true', help = 'with header file')
    new_parser.add_argument('-s', '--src', action = 'store_true', help = 'with source file')
    new_parser.add_argument('-t', '--test',   action = 'store_true', help = 'with test file')
    new_parser.add_argument('-c', '--struct',  action = 'store_true', help = 'with header and source file')
    new_parser.add_argument('-a', '--all',    action = 'store_true', help = 'with header, source and test file')
    new_parser.set_defaults(func = newcmd.run)

    move_parser = subparsers.add_parser('move', help = 'rename class, file or move folder')
    move_parser.add_argument('-s', '--source', action = 'store', help = 'source name')
    move_parser.add_argument('-d', '--destination', action = 'store', help = 'destination name')

    update_parser = subparsers.add_parser('update', help = 'update project according configuration')
    update_parser.set_defaults(func = updatecmd.run)    

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()      