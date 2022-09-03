#!/usr/bin/python3
print([x for x in xrange(0,100) if len(set(str(x)))==len(str(x))])
