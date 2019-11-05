import argparse
import os
import platform
import sys
from subprocess import call
from pathlib import Path


class DiffCommand:
    def __init__(self, args):
        self.args = args

def launch_difftool():
    if platform.system() == 'Windows':
        file_to_run = Path('c:\\')
        os.startfile()

def main():
    args = sys.argv
    diffcmd = DiffCommand(args)
    
    arg_no = 0
    for arg in diffcmd.args:
        print('{}: {}'.format(arg_no, arg))
        arg_no += 1
    return 0
    
if __name__ == '__main__':
    exit(main())
