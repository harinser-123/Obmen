
ax, ay, bx, by, cx, cy = map(int,input().split())

AB = abs(ax-bx) + abs(ay-by)
AC = abs(ax-cx) + abs(ay-cy) + abs(cx-bx) + abs(cy-by)
r = abs(AC-AB)
# print(AC)
# print(AB)

print(r)



