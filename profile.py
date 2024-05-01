#!/usr/bin/env python3

import resource
def using(point=""):
    usage=resource.getrusage(resource.RUSAGE_SELF)
    return '''%s: usertime=%s systime=%s mem=%s mb
           '''%(point,usage[0],usage[1],
                usage[2]/1024.0 )

print(using("start"))
file = open('file.txt','r')
topology_list = file.readlines()
for i in topology_list:
    i.replace('Ex','Exo').replace('Is','Isa').replace('Mk','Mrk').replace('Jms','Jas')
print(using("finish"))
