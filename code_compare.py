import random
import sys, os
import argparse
parser = argparse.ArgumentParser(description="Compare two code")
parser.add_argument('tc_generator', type=str, default='tc_gen.py', help="python code which generates test cases")
parser.add_argument('code1', type=str, default='code1.py', help="The first python code")
parser.add_argument('code2', type=str, default='code2.py', help="The second python code")
parser.add_argument('op_compare', type=str, default='op_compare.py', help="Python code which compares two outputs")
args = parser.parse_args()
tc = args.tc_generator
code1 = args.code1
code2 = args.code2
code_compare = args.op_compare
pyth =  'python3'
os.system('{} {} > inp.txt'.format(pyth,tc))
os.system('cat inp.txt | {} {} > op1.txt'.format(pyth,code1))
os.system('cat inp.txt | {} {} > op2.txt'.format(pyth,code2))
os.system('{} {}'.format(pyth,code_compare))

