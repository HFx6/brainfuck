import sys

op=[">","<","+","-","[","]",",","."]

inst = ""
cells = {1:0}
p=1
loops=[]
insp = 0
s=""

with open(sys.argv[1], 'r') as f:
    for l in f:
        for ch in l:
            if ch in op:
                inst+=ch.strip()
f.close()

def inc(n):
    if cells.get(p):
        if cells[p]+n > 255:
            cells[p]=n-255
            return
    cells[p] = cells.get(p, 0)+n

def dloop(insp):
    print(insp)
    print('dead loop')
    c=0
    insph = insp
    while insph < len(inst[insp+1:])+1:
        i = inst[insph]
        if i=="[":
            c+=1
        if i=="]":
            c-=1
        print(c)
        if c==0:
            print(insph)
            return insph
        insph+=1
    return insph
while insp < len(inst):
    ch = inst[insp]
    if ch==">":
        p+=1
        if p not in cells.keys():
            cells[p] = 0
    elif ch=="<":
        if p==1:
            p=max(cells.keys())
        else:
            p-=1
    elif ch=="+":
        inc(1)
    elif ch=="-":
        if p>=1:
            cells[p]-=1
    elif ch=="[":
        if cells[p]==0:
            insp=dloop(insp)
        else:          
            loops.append(insp)
    elif ch=="]":
        if len(loops)>0:
            if cells[p]==0:
                loops.pop()
            else:
                insp=loops[-1]
        else:
            sys.stdout.write("loop closed but never opened")
            break
    elif ch==",":
        x = input("input value in cell[{}]: ".format(p))
        inc(ord(x[0]))
    elif ch==".":
        s+=chr(cells[p])
    print(insp)
    insp+=1
print(cells, loops)
if len(loops)>0:
    sys.stdout.write("loop(s) started but never closed")
else:
    sys.stdout.write(s)