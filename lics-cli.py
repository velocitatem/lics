import argparse
from lics import *

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-m', '--message')
parser.add_argument('-r', '--random', help="This is a pretty dangerous option, as it can make it very difficult to understanc" , action="store_true")
args = parser.parse_args()
mod = modify_sentence(args.message, args.random)
print(mod)

