#!/usr/bin/env python3
import json


def file_founder(way):
    file_way = json.load(open(way))
    return file_way


def found_difference(way_one, way_two):
    file_one = file_founder(way_one)
    file_two = file_founder(way_two)
    key_set = set(file_one) | set(file_two)
    output = ''
    start, finish = '{', '}'
    for key in key_set:
        if key in file_one and key in file_two:
            new_string = ''
            if file_one[key] == file_two[key]:
                new_string = f'    {key}: {file_one[key]}\n'
            else:
                new_string = f'  - {key}: {file_one[key]}\n' \
                    f'  + {key}: {file_two[key]}\n'
            if new_string not in output:
                output += new_string
        elif key in file_one and key not in file_two:
            output += f'  - {key}: {file_one[key]}\n'
        elif key not in file_one and key in file_two:
            output += f'  + {key}: {file_two[key]}\n'
    return f'{start}\n{output} {finish}\n'


def output(args):
    print(found_difference(args.first_file, args.second_file))
