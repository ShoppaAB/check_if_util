#!/usr/bin/python
# Check interface utilization using nicstat
# nicstat needs to be in $PATH
# Author: Mattias Mikkola
import subprocess
import sys
from optparse import OptionParser
from numpy import mean

parser = OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='Interface to monitor')
parser.add_option('-w', '--warning', dest='warn', help='Warning threshhold')
parser.add_option('-c', '--critical', dest='crit', help='Critical threshhold')
parser.add_option('-n', '--iterations', dest='iter', help='Number of values to read')

(options, args) = parser.parse_args()

vals = []
p = subprocess.Popen('nicstat -p -i %s 1 %s' % (options.interface, int(options.iter)+1), shell=True, stdout=subprocess.PIPE)
for line in p.stdout.readlines():
    s = str.split(line, ':')
    vals.append(float(s[6]))
del vals[0]
avg = mean(vals)

if avg > float(options.crit):
    status = 'CRITICAL'
    code = 2
elif avg > float(options.warn):
    status = 'WARNING'
    code = 1
else:
    status = 'OK'
    code = 0

print('%s: Network utilization: %.2f%%|util=%.2f;%.2f;%.2f;0.00;100.00' % (status, avg, avg, float(options.warn), float(options.crit)))
exit(code)