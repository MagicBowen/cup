"""
cup : c++ unified package management tool.
"""

import argparse
import new

parser = argparse.ArgumentParser(description = 'cup : c++ unified package management tool')
subparsers = parser.add_subparsers(help = 'commands')

parser.add_argument("-v", "--verbose", help="show cup version no", action = "store_true")

# parser.add_argument("new", action = 'store', help="create a new project")

newparser = subparsers.add_parser('new', help = 'new a project')
newparser.add_argument('project', action = 'store', help = 'project name')
newparser.set_defaults(func = new.new_cmd)

args = parser.parse_args()
args.func(args)

if args.verbose:
	print "cup v0.0.1"