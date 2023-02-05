# credminer

credminer is a Python recursive string and regex utility. It allows you to recursively search through all files with in a directory and any subdirectories and matches on a string or regex. When a match is found it prints what was matched and the full path of the file it was found in to the screen. By default it will search all filetypes so unless you want to look for secrets in a specific filetype the `-f` can be ommited.

![secret_search.gif](https://github.com/3Xploitd/credminer/blob/5f0d943987684b7af1a91fe8059d97424e0832c9/secret_search.gif)

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

`python3 credminer.py -d / -f pdf -t password`
This will search for the word password in pdf files under the root directory

`python3 credminer.py -d / -s`
This will load the json regexes file and search for secrets matching each of the regexes on all file types under the root directory

`python3 credminer.py -d / -f txt -r "(pass|password|code|key)"`
This will search for either the word password or passcode in text files that are under the root directory

# invoke_credminer

This is  a modified version of `credminer.py` to allow you to run the script without saving it to disk. The reason being, is depending on your use case such as a Penetration Tester, you may not want the script to be saved on disk to leave definite artifacts behind. By default it runs the `get_secrets` function on the root directory, looking for all filetypes. However, this can be easily changed as there are several variables which have been added to pass the arguments to the script without having to pass them yourself. In a way this functions similarly to `IEX` in PowerShell. By changing the values of `text_search`, `regex_search`, `secret_search`, `filetype_search`, and `search_directory` it will automatically assign the arguments so all that has to be done to run the program on disk is `python3 credminer.py` but to run it without downloading it to disk you can run `python3 -c 'import requests; r = requests.get("https://raw.githubusercontent.com/3Xploitd/credminer/main/invoke_credminer.py").text;exec(r)'`.

![demo.gif](https://github.com/3Xploitd/credminer/blob/c3a23752a1accbaffce095824b158f53de8918ec/demo.gif)
