#!/home/rapa/project/first/venv/bin/python

import os

stream = os.popen('./test.sh')
output = stream.read()

print(output)

