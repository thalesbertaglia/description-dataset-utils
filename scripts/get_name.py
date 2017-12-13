import sys
import os

if __name__ == '__main__':
    if sys.argv[1] == '0':
        print(sys.argv[2].strip())
    else:
        line = sys.argv[2]
        root = os.getcwd()+'/avi/'
        film = line.split('/avi/')[-1].split('/')[0]+'/'
        arq = line.split('/')[-1]
        print(root+film+arq)
