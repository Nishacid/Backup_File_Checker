# Backup File Checker
Find backup file on a web server

## Installation

```
git clone https://github.com/Nishacid/Backup_File_Checker
cd Backup_File_Checker/
pip3 install -r requirements.txt
```

## Usage

```
usage: python3 main.py -host HOST -f FILE

optional arguments:
  -h, --help  show this help message and exit
  -host HOST  Targeted host
  -f FILE     File which will be tested
```

## Example 

Usage example agaist 127.0.0.1 on index.php file 

```
python3 main.py -host http://127.0.0.1/ -f index.php

[-] http://127.0.0.1/index.php.backup | HTTP Code : 404
[-] http://127.0.0.1/index.php.bck | HTTP Code : 404
[-] http://127.0.0.1/index.php.old | HTTP Code : 404
[-] http://127.0.0.1/index.php.save | HTTP Code : 404
[+] Found : http://127.0.0.1/index.php.bak | HTTP Code : 200
[-] http://127.0.0.1/index.php.sav | HTTP Code : 404
[-] http://127.0.0.1/index.php~ | HTTP Code : 404
[-] http://127.0.0.1/index.php.copy | HTTP Code : 404
[-] http://127.0.0.1/index.php.old | HTTP Code : 404
[-] http://127.0.0.1/index.php.orig | HTTP Code : 404
[-] http://127.0.0.1/index.php.tmp | HTTP Code : 404
[-] http://127.0.0.1/index.phptemp | HTTP Code : 404
[-] http://127.0.0.1/index.php.txt | HTTP Code : 404
[-] http://127.0.0.1/index.php.back | HTTP Code : 404
[-] http://127.0.0.1/index.php.bkp | HTTP Code : 404
[-] http://127.0.0.1/index.php.bac | HTTP Code : 404
[-] http://127.0.0.1/index.php.tar | HTTP Code : 404
[-] http://127.0.0.1/index.php.gz | HTTP Code : 404
[-] http://127.0.0.1/index.php.tar.gz | HTTP Code : 404
[-] http://127.0.0.1/index.php.zip | HTTP Code : 404
[-] http://127.0.0.1/index.php.rar | HTTP Code : 404
[-] http://127.0.0.1/index.phpcopia | HTTP Code : 404
```