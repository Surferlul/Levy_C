import turtle

t=turtle.Turtle()
n = int(input("Recursion Depth [-1 for inf]:"))
if n<0:
    color_diff = 1
else:
    color_diff = 1/(n+1)
color = [0,0,1]

while True:
    a = input("Starting Structure [I for one line, L for l-shape, C for custom]:")
    if a.upper() == "I":
        s=[(0, True)]
    elif a.upper() == "L":
        s = [(-90, True), (90, True)]
    elif a.upper() == "C":
        s = eval(input("Input custom starting structure [Format: [(int Rotation, bool Walk first), (int Rotation, bool Walk first)]]:\n"))
    else:
        print("Invalid input!")
        continue
    break
m = input("Size Multiplier [default 50]:")
if m:
    m=int(m)
else:
    m=50
speed = input("speed [default 0]:")
if speed:
    speed=int(speed)
else:
    speed=0
clr = input("Color (many times slower) [default 0]")
if clr:
    clr = int(clr)
else:
    clr = 0
r = input("Start Rotation [default 0]:")
if r:
    r=int(r)
else:
    r=0
frm = input("Display from [default 0]:")
if frm:
    frm=int(frm)
else:
    frm=0
to = input("Display to [default inf]:")
if to:
    to=int(to)
else:
    to=9e999

if -1>speed>10:
    t.speed(10-speed)
else:
    turtle.tracer(0, 0)

def draw_arr(arr, multiplier=50, step=1, frm=0, to=9e999):
    x=0
    rot=0
    for i,j in arr:
        if x >= frm and x <= to:
            if j:
                if rot:
                    t.right(rot)
                t.forward(multiplier)
                t.right(i)
                rot=0
            else:
                rot += i
            if step>1:
                if not x % step:
                    turtle.update()
        x+=1
    t.right(rot)


def levy_c(n, rotations, start_rotation=0):
    def gen(n):

        yield start_rotation, False
        if n == 0:
            yield from next(rotations)
        else:
            yield 45, False
            if clr:
                color[0] += color_diff
                color[2] -= color_diff
                t.color(tuple(color))
            yield from gen(n-1)
            if clr:
                color[0] -= color_diff
                color[2] += color_diff
                t.color(tuple(color))
            yield -90, False
            yield from gen(n-1)
            yield 45, False
    while True:
        yield gen(n)

def arr_generator(arr):
    def gen():
        for i in arr:
            yield i
    while True:
        yield gen()

def optimize_arr(arr):
    for i in range(len(arr)):
        while len(arr) > i+1 and not arr[i+1][1]:
            arr[i] = ((arr[i][0] + arr.pop(i+1)[0])%360, arr[i][1])
    return arr

s = arr_generator(s)

if n < 0:
    while True:
        turtle.update()
        if not clr:
            s = arr_generator(optimize_arr([i for i in next(s)]))

        s = levy_c(1, s)
        t.right(-45)
        draw_arr(next(s), multiplier=m, step=speed, frm=frm, to=to)
        color_diff=1/(1/color_diff+1)
else:
    draw_arr(next(levy_c(n, s, r)), multiplier=m, step=speed, frm=frm, to=to)

turtle.update()
input("Done!")
