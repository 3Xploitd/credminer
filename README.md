# rseek

rseek is a Python recursive string and regex utility. It allows you to recursively search through all files with in a directory and any subdirectories and matches on a string or regex. When a match is found it prints what was matched and the full path of the file it was found in to the screen.

## usage

~~~

usage: rseek.py [-h] (-t TEXT | -r REGEX | -s SECRETS) -d DIRECTORY [-f FILETYPE]

usage: rseek.py [-h] (-t TEXT | -r REGEX | -s) -d DIRECTORY -f FILETYPE [-a ADDREGEX]

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  text or to search for
  -r REGEX, --regex REGEX
                        regular expression to match on
  -s, --secrets         Secrets to search for
  -d DIRECTORY, --directory DIRECTORY
                        The directory to search in
  -f FILETYPE, --filetype FILETYPE
                        The file extention to search for
  -a ADDREGEX, --addregex ADDREGEX
                        Temporarily adds a regex expression to the secrets file
~~~

      
## Examples

`python3 rseek.py -d / -f txt -t password`
This will search for any files under the root directory that are text files and contain the word password in them.

`python3 rseek.py -d / -f all -t password`
This will search for the word password in all files under the root directory

`python3 rseek.py -d / -f txt -r "(pass|password|code|key)"`
This will search for either the word password or passcode in text files that are under the root directory
<script src="https://github.com/3Xploitd/credminer/blob/main/demo5.cast" id="asciicast-14" async data-autoplay="true" data-size="big"></script>

