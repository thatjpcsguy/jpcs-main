import sys
import os
sys.path.insert(0, '/home/james/jpcs-main')

for line in open('/home/james/jpcs-main/keys.txt', 'rU'):
    print line
    line = line.split('=')
    os.environ[line[0]] = line[1]

from jpcs import app as application
