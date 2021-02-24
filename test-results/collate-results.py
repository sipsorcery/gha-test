import os
import glob
from collections import defaultdict
from datetime import datetime

# The character width of each cell in the results markdown table.
COL_WIDTH = 12

print("Collating Test Results")

resultFiles = glob.glob("./*.txt")

results = defaultdict(dict)
serverKeys = []
clientKeys = []

for resFile in resultFiles:
    with open(resFile) as f:
        for line in f:
            cols = line.strip().split(',')
            if not cols[0] in serverKeys:
                serverKeys.append(cols[0])
            if not cols[1] in clientKeys:
                clientKeys.append(cols[1])
            #if not results[cols[0]]:
            #    results[cols[0]] = {}
            results[cols[0]][cols[1]] = cols[2]

sorted(serverKeys)
sorted(clientKeys)

#print(serverKeys)
#print(clientKeys)
#print(results)

#print("len(clientKeys)=%i" % len(clientKeys))

print('Echo Test Interoperability Results')
print('Test run at %s' % datetime.now())

# Print Table header row.
print(f'| {"Server": <{COL_WIDTH}}| {"Client": <{COL_WIDTH}}', end='')
for i in range(0, (len(clientKeys) - 1)):
    print(f'| {" ":<{COL_WIDTH}}', end='')
print('|')

# Print end of header line.
sep = '-' * (COL_WIDTH + 1)
for i in range(len(clientKeys) + 1):
    print(f'|{sep}', end='')
print('|')

# Print Client column headings.
print(f'| {" ":<{COL_WIDTH}}', end='')
for clientKey in clientKeys:
    print(f'| {clientKey: <{COL_WIDTH}}', end='')
print('|')

# Print Server rows.
for serverKey in serverKeys:
    print(f'| {serverKey: <{COL_WIDTH}}', end='')
    for clientKey in clientKeys:
        if serverKey in results.keys() and clientKey in results[serverKey].keys():
            resultChar = '&#9745;' if results[serverKey][clientKey] == '0' else '&#x2612;'
            print(f'| {resultChar:<{COL_WIDTH}}', end='')
        else:
            print(f'| {" ":<{COL_WIDTH}}', end='')
    print('|')