#!/usr/local/bin/python3

import argparse
import newcmd
import addcmd
import buildcmd
import testcmd


def main():
    parser = argparse.ArgumentParser(description = 'cup : c++ unified package management tool')
    subparsers = parser.add_subparsers(help = 'commands')

    new_parser = subparsers.add_parser('new', help = 'create project')
    new_parser.add_argument('project_name', action = 'store', help = 'project name')
    new_parser.add_argument('-e', '--eclipse', action = 'store_true', help = 'generate eclipse project')
    new_parser.add_argument('-b', '--build', action = 'store_true', help = 'generate build script')
    new_parser.set_defaults(func = newcmd.run)   

    add_parser = subparsers.add_parser('add', help = 'add files for project')
    add_parser.add_argument('file', action = 'store', help = 'file name')
    add_parser.add_argument('-i', '--include', action = 'store_true', help = 'header file')
    add_parser.add_argument('-s', '--src', action = 'store_true', help = 'source file')
    add_parser.add_argument('-t', '--test',   action = 'store_true', help = 'test file')
    add_parser.add_argument('-c', '--struct',  action = 'store_true', help = 'class file')
    add_parser.add_argument('-a', '--all',    action = 'store_true', help = 'class file with test')
    add_parser.set_defaults(func = addcmd.run)    

    build_parser = subparsers.add_parser('build', help = 'build project')
    build_parser.add_argument('-c', '--clean', action = 'store_true', help = 'clean build result')
    build_parser.set_defaults(func = buildcmd.run)  

    test_parser = subparsers.add_parser('test', help = 'test project')
    test_parser.add_argument('-p', '--paras', action = 'store', default = '', help = 'test parameters')
    test_parser.set_defaults(func = testcmd.run)   

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    try:
        main()
        exit(0)
    except Exception as e:
        print('CUP failed: ', str(e))  
        exit(1)         