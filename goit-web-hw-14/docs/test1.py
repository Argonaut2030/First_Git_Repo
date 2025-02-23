import os
import sys

parent_dir = os.path.abspath('../')
print(parent_dir)
sys.path.append(os.path.abspath('../'))
# print(sys.path)
print(sys.modules)