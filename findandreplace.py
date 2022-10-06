
import fileinput
import sys

text = "-17."   # if any line contains this text, I want to modify the whole line.

x = fileinput.input(files="/Users/yashraj/Desktop/coords/edit.txt", inplace=1)
for line in x:
    if text in line:
        new_text = " LatLng(" + [ t for t in line.split() if t.startswith('28.') ][0] +[ t for t in line.split() if t.startswith('-17.') ][0]+ "),"
        line = new_text
    sys.stdout.write(line)
x.close()