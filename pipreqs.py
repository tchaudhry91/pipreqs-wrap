import sys
import os

args = " ".join(sys.argv[1:])

command = "pipreqs " + args
os.system(command)
