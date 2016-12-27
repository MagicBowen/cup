"""
cup : c++ unified package management tool.
"""

import argparse
import UpdateCmd
import NewCmd

def main():
    parser = argparse.ArgumentParser(description = 'cup : c++ unified package management tool')
    subparsers = parser.add_subparsers(help = 'commands')
    newparser = subparsers.add_parser('new', help = 'new a project')
    newparser.add_argument('project', action = 'store', help = 'project name')
    newparser.set_defaults(func = NewCmd.new_cmd)
    initparser = subparsers.add_parser('update', help = 'update project according configuration')
    initparser.set_defaults(func = UpdateCmd.update_cmd)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()		