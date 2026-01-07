main, add = map(int, input().split())
dist = 0
while main > 0:
    main -= 1
    dist += 10
    if main % 5 == 0 and add > 0:
        main += 1
        add -= 1
print(dist)
