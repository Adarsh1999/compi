asteroids = [5, 10, -5]
# Output: [5, 10]

# asteroids = sorted(asteroids)

print(asteroids)

neg_l = list()
pos_l = []

for x in range(len(asteroids)):
    if asteroids[x] < 0:
        neg_l.append(asteroids[x])  
    else:
        pos_l.append(asteroids[x])  

