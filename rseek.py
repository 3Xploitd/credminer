#!/usr/bin/python3

import re,sys,argparse

from pathlib import Path

def rseek(directory,filetype,text):
    exception_errors = [KeyboardInterrupt,IsADirectoryError,UnicodeDecodeError]
    if filetype.lower() == 'all':
        filetype = '*'
    for path in Path(directory).rglob('*.' + str(filetype)):
        if args.regex != None:
            search_string = r"{}".format(text)
            
        else:
            search_string = r"{}".format(re.escape(text)) + r"{1,20}"
        encoding_list = 'latin-1'
        try:
            f = open(path,'r',encoding=encoding_list).read()
            regex = re.findall(search_string,f, re.IGNORECASE)
            if regex != []:
                print(set(regex),path)

        except KeyboardInterrupt:
            print('KeyboardInterrupt Detected, exiting now....')
            sys.exit(1)
        except Exception as e:
            continue
            
        
        
if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t','--text',help='text or to search for',action='store')
    group.add_argument('-r','--regex',help='regular expression to match on',action='store')
    parser.add_argument('-d','--directory',help='The directory to search in',required=True,action='store')
    parser.add_argument('-f','--filetype',help='The file extention to search for')
    args = parser.parse_args()

    directory = args.directory
    filetype = args.filetype
    if args.text != None:
        text = args.text
    else:
        text = args.regex
        
    rseek(directory,filetype,text)
    
