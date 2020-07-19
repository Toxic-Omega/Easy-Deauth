import os

os.system('sed -i 1d scan.txt')
os.system('sed -i 1d scan.txt')
print('\033[1;31m')
os.system('cat scan.txt')
os.system('rm -r scan.txt')
