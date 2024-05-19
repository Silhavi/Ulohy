

import math

input_text = """-1000000,0: LOT
1000000,0: KLM
5000000,0: AirFrance
"""

planes = []
distances = []
planes_combinations = []
lines = input_text.split("\n")

for i in lines:
    if i == "":
        break
    i.split(": ")
    i.split(",")
    planes.append(i.split(": "))

try:
    for i in planes:
        i[0] = i[0].split(",")
        i[0][0] = float(i[0][0])
        i[0][1] = float(i[0][1])
except:
    print("Nesprávný vstup.")
    exit()
planes_copy = planes.copy()

for i in range(len(planes)):
    for j in range(i + 1, len(planes)):

        distance_x = abs(planes[i][0][0] - planes[j][0][0])
        distance_y = abs(planes[i][0][1] - planes[j][0][1])
        
        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        planes_combinations.append([planes[i][1], planes[j][1]])
        
        
        distances.append(distance)

# print()
# print(f"{planes_combinations}")
# print(f"{distances}")
# print()
print(f"Pozice letadel:")
for i in planes:
    print(i)
print(f"Vzdálenost nejbližších letadel: {min(distances)}")
print(f"Počet nalezených dvojic: {distances.count(min(distances))}")
print(f"Nejbližší letadla:")
for i in range(len(distances)):
    if distances[i] == min(distances):
        print(f"{planes_combinations[i][0]} - {planes_combinations[i][1]}")
        
# print(distances)

# print(f"das {min(distances)}")