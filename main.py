#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author            : Nishacid
# Python Version    : 3.*

import argparse
import requests
import sys

if __name__ == "__main__":
    
    # Arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", dest="host", help="Targeted host", required=True)
    parser.add_argument("-f", dest="file", help="File which will be tested", required=True)
    args = parser.parse_args()

    # List of backup extensions 
    list=[".backup",".bck",".old",".save",".bak",".sav","~",".copy",".old",".orig",".tmp",".temp",".swp", ".txt",".back",".bkp",".bac",".tar",".gz",".tar.gz",".zip",".rar", ".copia"]

    file = args.file
    host = args.host

    for ext in list:
        try:
            url = host + file + ext
            result = requests.get(url)
            if result.status_code == 200:
                print('\033[92m' + "[+] Found : " + url + " | HTTP Code : " + str(result.status_code) + '\033[0m')
            else:
                print('\033[91m' + "[-] " + url + " | HTTP Code : " +str(result.status_code) + '\033[0m')
        except requests.ConnectionError:
            print("Error, failed to etablish connection on : " + url)
            sys.exit(1)
        except requests.Timeout: 
            print("Error, request time out")
            
