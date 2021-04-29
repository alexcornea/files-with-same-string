#! /usr/bin/python3

import os

string = input('Type a string: ')
dirsrc = input('Type a path: ')
file_type = '.txt'

if __name__ == "__main__":
    def containsString(file, line):
        with open(file, 'r') as reader:
            for line in reader:
                if string in line:
                    return True

    print(f'The files that contains the string "{string}" are:')
    for dirpath, dirnames, files in os.walk(dirsrc):
        for file_name in files:
            file_path = f'{dirpath}/{file_name}'
            if file_name.endswith(file_type) and containsString(file_path, string):
                print(file_name, end='\n')