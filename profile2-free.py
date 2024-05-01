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
import fileinput
gc.enable()
#file = open('file.txt','r')
#topology_list = file.readlines()
#for i in topology_list:
for i in fileinput.input():
    exo=re.sub('Ex', 'Exo', i)
    del i
    isa=re.sub('Is', 'Isa', exo)
    del exo
    mrk=re.sub('Mk', 'Mrk', isa)
    del isa
    jas=re.sub('Jms', 'Jas', mrk)
    del mrk
    # process
    del jas
print(using("finish"))
