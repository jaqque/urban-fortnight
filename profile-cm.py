#!/usr/bin/env python3

import resource
def using(point=""):
    usage=resource.getrusage(resource.RUSAGE_SELF)
    return '''%s: usertime=%s systime=%s mem=%s mb
           '''%(point,usage[0],usage[1],
                usage[2]/1024.0 )

print(using("start"))
with open('file.txt','r') as fileobject:
  for i in fileobject:
    i.replace('Ex','Exo').replace('Is','Isa').replace('Mk','Mrk').replace('Jms','Jas')
print(using("finish"))
