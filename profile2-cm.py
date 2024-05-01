#!/usr/bin/env python3

import resource
def using(point=""):
    usage=resource.getrusage(resource.RUSAGE_SELF)
    return '''%s: usertime=%s systime=%s mem=%s mb
           '''%(point,usage[0],usage[1],
                usage[2]/1024.0 )

print(using("start"))

import re
with open('file.txt','r') as fileobject:
  for i in fileobject:
    re.sub('Ex', 'Exo', re.sub('Is', 'Isa', re.sub('Mk', 'Mrk', re.sub('Jms', 'Jas', i))))
print(using("finish"))
