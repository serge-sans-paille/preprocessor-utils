import subprocess
import sys
import re
import collections
import operator

linemarker = re.compile(r'^#\s(\d+)\s"([^"]+)"((?:\s\d)*)')

histogram = collections.defaultdict(int)
file_stack = []
output = subprocess.check_output(sys.argv[1:])
for line in output.decode().split("\n"):
    m = linemarker.match(line)
    if m:
        filename = m.group(2)
        flags = tuple(map(int, m.group(3).split()))
        if 1 in flags or not flags:
            file_stack.append(filename)
        elif 2 in flags:
            file_stack.pop()
    else:
        histogram[file_stack[-1]] += 1

for k, v in sorted(histogram.items(), key=operator.itemgetter(1), reverse=True):
    print(k, v)
