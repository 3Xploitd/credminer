#!/usr/bin/python3

import re,sys,argparse,json
from time import time,strftime
import magic
from pathlib import Path
from pdfminer.high_level import extract_text

def rseek(directory,filetype,regex):
    
    if args.regex or args.text != None:
        pattern = re.compile(regex)
    start = time()
    outfile = {}
    extensions = ['pdf','gzip']
    for path in Path(directory).rglob('*.' + str(filetype)):
        
        try:
            if path.name == 'regexes.json' or path.is_dir():
                continue
            m = magic.open(magic.MAGIC_NONE)
            m.load()
            ftype = m.file(path).lower()
            if ftype.count('pdf') >= 1:
                f = extract_text(path)
            
            if ftype.count('pdf') == 0:
                f = open(path,'r',encoding='latin-1').read()
            if args.text or args.regex != None:
                pattern = re.compile(regex)
                result = pattern.findall(f)
                if result != []:
                    print("Found \033[1;31;40m{}\033[0;0m in {}".format(result[0],path))        
            else:
                get_secrets(regex,path,f)
                        
        except KeyboardInterrupt:
            print("Keyboard Interrupt Detected, exiting now...")
            sys.exit(0)

        except Exception as e:
            print(e)
            continue
    end = time()
    totaltime = (end-start)
    if totaltime > 60:
        print("\nCompleted in {} minutes\n".format(str(totaltime/60)))
    else:
        print("\nCompleted in {} seconds\n".format(str(totaltime)))
        
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
    parser.add_argument('-f','--filetype',help='The file extention to search for',default='*',required=False,action='store')
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
