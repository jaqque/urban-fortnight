#!/usr/bin/env python3

import resource
def using(point=""):
    usage=resource.getrusage(resource.RUSAGE_SELF)
    return '''%s: usertime=%s systime=%s mem=%s mb
           '''%(point,usage[0],usage[1],
                usage[2]/1024.0 )

print(using("start"))

import re
import fileinput
records=0
for i in fileinput.input():
    re.sub('Ex', 'Exo', re.sub('Is', 'Isa', re.sub('Mk', 'Mrk', re.sub('Jms', 'Jas', i))))
    records += 1
print(f"Processed {records:,} records")
print(using("finish"))
