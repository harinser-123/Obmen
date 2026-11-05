
W, H, w, h = map(int,input().split())

if H>=h and W>=w:
    print("STRAIGHT")
elif H>=w and W>=h:
    print('TURN')
else:
    print("NO")


