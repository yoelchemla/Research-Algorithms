import sys
import math

# credit: https://github.com/gctom57/codingame/blob/master/VeryHard/MusicScores.java

width, height = [int(i) for i in input().split()]
arr = input().split()
image = "".join(" " * int(arr[x + 1]) if arr[x] == "W" else "x" * int(arr[x + 1]) for x in range(0, len(arr), 2)) 
image = [image[x: x + width] for x in range(0, len(image), width)]  

t = ""
note = []
notes = []

for x in range(width):  
    line = "".join(image[y][x] for y in range(height))[::-1]

    if "x" in line:  # if notation has started
        if t == "": # initialize  
            t = line[line.index("x"):line[line.index("x"):].index(" x") + line.index("x") + 1]
            first = line
        if line.strip() in [(t*5).strip(), (t*6).strip()]:  # if there are not notes in current
            if len(note) > 0:  
                middle = note[len(note) // 2]
                longest = max(middle.split(), key=len)
                if len(longest) > sum(len(p) for p in middle.split() if p != longest) and not all(p == middle.split()[0] for p in middle.split()): 
                    term = "Q"
                else:  
                    top = max([i for i in range(len(middle)) if middle[i] == "x" and first[i] != "x"])
                    space = middle[:top][::-1].index(" x") + 1
                    middle = middle[:top - space] + "x"*space + middle[top:]
                    term = "H"
                longest = max(middle.split(), key=len)
                mid_len = len(middle.split())
                note_idx = middle.split().index(longest)
                if mid_len == 6: incline = "C"
                elif middle.count(t) == 5 and len(middle.split()[0]) == len(longest): incline = "D"
                elif note_idx == 0: incline = "E" if mid_len == 5 else "F"
                elif note_idx == 1: incline = "G" if mid_len == 5 else "A"
                elif note_idx == 2: incline = "B" if mid_len == 5 else "C"
                elif note_idx == 3: incline = "D" if mid_len == 5 else "E"
                elif len(middle.split()[4]) == len(longest) and t*4 not in middle: incline = "F"
                else: incline = "G"
                notes.append(incline + term)
                note = []
        else:  
            note.append(line)
print(*notes, sep=" ")