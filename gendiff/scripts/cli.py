#!/usr/bin/env python3
import argparse


def run():
    parser = argparse.ArgumentParser(prog='gendiff',
            description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
            help='set format of output')

    args = parser.parse_args()
    return args


