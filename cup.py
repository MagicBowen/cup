"""
cup : c++ unified package management tool.
"""

import argparse
from newcmd    import ProjectGenerator
from filecmd   import FileGenerator
from updatecmd import ProjectUpdater
import initcmd



def main():
    parser = argparse.ArgumentParser(description = 'cup : c++ unified package management tool')
    subparsers = parser.add_subparsers(help = 'commands')

    init_parser = subparsers.add_parser('init', help = 'initialize a project')
    init_parser.add_argument('project', action = 'store', help = 'project name')
    init_parser.set_defaults(func = initcmd.run)

    new_parser = subparsers.add_parser('new', help = 'new a project')
    new_parser.add_argument('project', action = 'store', help = 'project name')
    new_parser.add_argument('-e', '--ide', action = 'store_true', help = 'generate eclipse project')
    new_parser.set_defaults(func = ProjectGenerator.generate)

    file_parser = subparsers.add_parser('file', help = 'generate files')
    file_parser.add_argument('file', action = 'store', help = 'file name')
    file_parser.add_argument('-i', '--include', action = 'store_true', help = 'with header file')
    file_parser.add_argument('-s', '--src', action = 'store_true', help = 'with source file')
    file_parser.add_argument('-t', '--test',   action = 'store_true', help = 'with test file')
    file_parser.add_argument('-c', '--struct',  action = 'store_true', help = 'with header and source file')
    file_parser.add_argument('-a', '--all',    action = 'store_true', help = 'with header, source and test file')
    file_parser.set_defaults(func = FileGenerator.generate)

    update_parser = subparsers.add_parser('update', help = 'update project according configuration')
    update_parser.set_defaults(func = ProjectUpdater.update)    

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()      