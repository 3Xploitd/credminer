#!/usr/bin/python3

import re,sys,argparse,json
from time import time

from pathlib import Path

def rseek(directory,filetype,regex):
    
    if filetype.lower() == 'all':
        filetype = '*'
    if args.regex or args.text != None:
        pattern = re.compile(regex)
    start = time()
    outfile = {}
    
    for path in Path(directory).rglob('*.' + str(filetype)):
        
        encoding_list = 'latin-1'
        
        try:
            
            f = open(path,'r',encoding=encoding_list).read()
            if args.text or args.regex != None:
                pattern = re.compile(regex)
                result = pattern.findall(f, re.IGNORECASE)
                if result != []:
                    print("Found {} in {}".format(set(result),path))
                    
                        
            else:# args.secrets == True:
                get_secrets(regex,path,f)
                        
        except KeyboardInterrupt:
            print("Keyboard Interrupt Detected, exiting now...")
            sys.exit(0)

        except Exception as e:
            continue
    end = time()
    totaltime = (end-start)/60
    print("\nCompleted in {} minutes\n".format(str(totaltime)))
def load_secrets():
    f = open("regexes.json",'r').read()
    regex = json.loads(f)
    
    return regex
    

def get_secrets(regex,path,f):

    for search_pattern in regex:
        pattern = re.compile(regex[search_pattern])
        result = pattern.findall(f)
        if result != []:
            print("{}:\033[1;31;40m{}\033[0;0m Found in {}".format(search_pattern,list(set(result))[0],path))
           
        
if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t','--text',help='text or to search for',action='store')
    group.add_argument('-r','--regex',help='regular expression to match on',action='store')
    group.add_argument('-s','--secrets',help='Secrets to search for',action='store_true')
    parser.add_argument('-d','--directory',help='The directory to search in',required=True,action='store')
    parser.add_argument('-f','--filetype',help='The file extention to search for',required=True,action='store')
    parser.add_argument('-a','--addregex',help='Adds a regex expression to the secrets file',required=False,action='store')
    
    args = parser.parse_args()

    directory = args.directory
    filetype = args.filetype
    if args.text != None:
        regex = r'{}'.format(re.escape(args.text))

    elif args.regex != None:
        regex = r'{}'.format(args.regex)

    else:
        regex = load_secrets()
        if args.addregex:
            add_regex = args.addregex
            regex[add_regex[:(add_regex.find(':'))]] = add_regex[(add_regex.find(':')+1):]
       
    rseek(directory,filetype,regex)
