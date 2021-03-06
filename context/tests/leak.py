#!/dls_sw/tools/python2.4-debug/bin/python2.4

from __future__ import print_function

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from cothread import *

def Task():
    pass

def run(N):
    print('start', sys.gettotalrefcount())
    tasks = [Spawn(Task) for n in range(N)]
    for t in tasks:
        t.Wait()
    print('done', sys.gettotalrefcount())

for i in range(5):
    run(10)
    print('None', sys.getrefcount(None))
