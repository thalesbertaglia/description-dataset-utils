import sys
import subprocess
import time
import os


username = 'PLy5'
password = 'zoi8Ua4uki'

if __name__ == '__main__':
    in_file = sys.argv[1]
    with open(in_file) as f:
        for line in f:
            print(line)
            root = os.getcwd()+'/avi/'
            film = line.split('/avi/')[-1].split('/')[0]+'/'
            arq = line.split('/')[-1]
            path = root+film+arq
            args = ['wget', '-crnH', '-q', line.strip(), '--cut-dirs=2', '--user='+username, '--password='+password, '--auth-no-challenge']
            p1 = subprocess.Popen(args)
            p1.communicate()
            pc = subprocess.Popen(['ffmpeg', '-nostats', '-loglevel', str(0), '-i', path, '-f', 'wav', '-ab', str(192000), '-vn', path.split('.avi')[0]+'.wav'])
            pc.communicate()
            pr = subprocess.Popen(['rm', path])
            pr.communicate()
