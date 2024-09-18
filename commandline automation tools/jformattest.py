import os
import sys
import json
import argparse
import click

def formatter(string,sort_keys =True, indent  =4):
    loaded_json = json.loads(string)
    return json.dumps(loaded_json,sort_keys = sort_keys,indent =indent)

def main(path,no_sort):
    if no_sort:
        sort_keys =False
    else:
        sort_keys = True
    with open(path,'r') as _f:
        print(
            formatter(_f.read(),sort_keys=sort_keys)
        )
        
print(sys.argv) # shows whats being passed to the command line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "This is a Jformat tool")
    parser.add_argument("--sort",action = "store_true",help = "set the sorting")
    args = parser.parse_args()
    print(args.sort)
    # main(sys.argv[-1 ],no_sort=False)
