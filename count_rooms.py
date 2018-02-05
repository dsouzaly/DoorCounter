s = input("Enter room #'s: ")
s = s.split()
done = []
doors = 0
for room in s:
    if room[:2] == 'OP':
        doors += 1
    else:
        if room[:5] not in done:
            done.append(room[:5])
            doors += 1
print(doors)
