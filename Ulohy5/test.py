import math

input_text = """0,0: LOT
5,8 KLM
"""

planes = []
distances = []
planes_combinations = []
lines = input_text.split("\n")

try:
    if len(lines) < 2:
        raise ValueError("Méně než dvě letadla na vstupu (jinak není definovaná nejmenší vzdálenost).")

    for i in lines:
        if i == "":
            break
        parts = i.split(": ")
        if len(parts) != 2:
            raise ValueError("Chybějící nebo přebývající oddělovače (čárka, dvojtečka).")
        
        coordinates = parts[0].split(",")
        if len(coordinates) != 2 or not all(coord.replace(".", "").isdigit() for coord in coordinates):
            raise ValueError("Neplatné souřadnice (není platné desetinné číslo).")
        
        planes.append([list(map(float, coordinates)), parts[1]])

    planes_copy = planes.copy()

    for i in range(len(planes)):
        for j in range(i + 1, len(planes)):
            distance_x = abs(planes[i][0][0] - planes[j][0][0])
            distance_y = abs(planes[i][0][1] - planes[j][0][1])
            
            distance = math.sqrt(distance_x**2 + distance_y**2)
            
            planes_combinations.append([planes[i][1], planes[j][1]])
            distances.append(distance)

    print(f"Pozice letadel:")
    for i in planes:
        print(i)
    if not distances:
        raise ValueError("Nejsou k dispozici žádné vzdálenosti.")
    print(f"Vzdálenost nejbližších letadel: {min(distances)}")
    print(f"Počet nalezených dvojic: {distances.count(min(distances))}")
    print(f"Nejbližší letadla:")
    for i in range(len(distances)):
        if distances[i] == min(distances):
            print(f"{planes_combinations[i][0]} - {planes_combinations[i][1]}")
except ValueError as ve:
    print(f"Chyba: {ve}")
