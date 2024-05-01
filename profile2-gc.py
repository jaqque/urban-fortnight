#!/usr/bin/env python3

import resource
def using(point=""):
    usage=resource.getrusage(resource.RUSAGE_SELF)
    return '''%s: usertime=%s systime=%s mem=%s mb
           '''%(point,usage[0],usage[1],
                usage[2]/1024.0 )

print(using("start"))

import re
import gc
file = open('file.txt','r')
topology_list = file.readlines()
for i in topology_list:
    re.sub('Ex', 'Exo', re.sub('Is', 'Isa', re.sub('Mk', 'Mrk', re.sub('Jms', 'Jas', i))))
    gc.collect()
print(using("finish"))
