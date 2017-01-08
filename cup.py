"""
cup : c++ unified package management tool.
"""

import argparse
from NewCmd    import new_project
from UpdateCmd import update_project
from FileCmd   import create_file

def main():
    parser = argparse.ArgumentParser(description = 'cup : c++ unified package management tool')
    subparsers = parser.add_subparsers(help = 'commands')

    new_parser = subparsers.add_parser('new', help = 'new a project')
    new_parser.add_argument('project', action = 'store', help = 'project name')
    new_parser.set_defaults(func = new_project)

    file_parser = subparsers.add_parser('file', help = 'generate files')
    file_parser.add_argument('file', action = 'store', help = 'file name')
    file_parser.add_argument('-i', '--header', action = 'store_true', help = 'with header file')
    file_parser.add_argument('-s', '--source', action = 'store_true', help = 'with source file')
    file_parser.add_argument('-t', '--test',   action = 'store_true', help = 'with test file')
    file_parser.add_argument('-c', '--class',  action = 'store_true', help = 'with header and source file')
    file_parser.add_argument('-a', '--all',    action = 'store_true', help = 'with header, source and test file')
    file_parser.set_defaults(func = create_file)

    update_parser = subparsers.add_parser('update', help = 'update project according configuration')
    update_parser.set_defaults(func = update_project)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()		