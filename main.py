# Peter's Problem 2022 No.15

from itertools import combinations

valid_points = []

points = ["A", "B", "C", "D", "E", "F", "P", "Q", "R", "S"]
zone1 = ["A", "B", "C", "D", "E", "F"]
zone2 = ["P", "Q", "C", "R", "S"]

def filter_comb(comb):
    count1 = 0
    count2 = 0

    for point in comb:
        if point in zone1:
            count1 += 1
        if point in zone2:
            count2 += 1

    
    if count1 < 3 and count2 < 3:
        return True
    else:
        return False
    

for comb in combinations(points, 3):
    if filter_comb(comb):
        valid_points.append(comb)

print(f"Answer: {len(valid_points)}")
print("")
print(valid_points)
