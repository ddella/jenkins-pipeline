import sys
import platform

"""
Get the Python's version
"""

print('\nHello #50 from Jenkins Pipeline 😀')
# check the Python version using the sys module
print(f'sys module: {sys.version}')

# check the Python version using the platform module
print(f'platform module: {platform.python_version()}')

# version number in tuple format
print(f'tuple format: {sys.version_info}')
print(f'python version tuple: {platform.python_version_tuple()}\n')
