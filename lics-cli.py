import argparse
from lics import *

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-m', '--message')
args = parser.parse_args()
print(modify_sentence(args.message))

