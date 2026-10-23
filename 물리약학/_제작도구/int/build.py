import sys, lib
mods = sys.argv[1:] or ['front', 'p1', 'p2', 'p3', 'p4', 'p5']
for m in mods:
    __import__(m)
lib.build('out')
