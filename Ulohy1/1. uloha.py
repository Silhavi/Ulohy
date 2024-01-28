import math
import os

# Funkce pro výpočet délky hadice

def check_valid_input(point, room_size):
    c = 0
    for coord in point:
        if coord<20 or coord>room_size-20:
            c+=1
    on_wall = 0 in point or room_size in point
    return c==1 and on_wall

def calculate_hose_length(room_size, point1, point2, wall_case):
    match wall_case:
        case "adjacent_wall":
            distances = [abs(point1[i] - point2[i]) for i in range(3)]
            axis = [i for i in range(3) if (point1[i] not in [0, room_size]) and (point2[i] not in [0, room_size])][0]
            other_sides = [distances[i] for i in range(3) if i != axis]
            return math.sqrt(sum(other_sides)**2 + distances[axis]**2)
        case "opposite_wall":
            point1 = [i for i in point1 if (i != 0) and (i != room_size)]
            point2 = [i for i in point2 if (i != 0) and (i != room_size)]

            point1_distances = distance_to_edges(point1, room_size)
            point2_distances = distance_to_edges(point2, room_size)

            distances = []

            for direction in range(4):
                point1_distance = point1_distances[direction]
                point2_distance = point2_distances[direction]

                between_points = [abs(point1[0] - point2[0]), abs(point1[1] - point2[1])]

                if direction%2==1:
                    dist = math.sqrt((point1_distance + point2_distance + room_size)**2 + between_points[0]**2)
                else:
                    dist = math.sqrt((point1_distance + point2_distance + room_size)**2 + between_points[1]**2)

                distances.append(dist)

            return min(distances)

# Funkce pro detekci typu umístění bodů
def detect_wall_case(point1, point2, room_size):
    distances = [abs(point1[i] - point2[i]) for i in range(3)]
    if room_size in distances:
        return "opposite_wall"
    else:
        return "adjacent_wall"

def distance_to_edges(point, room_size):
    return [point[0], point[1],room_size - point[0], room_size - point[1]]

# Funkce pro výpočet délky trubek pro různé případy
def calculate_pipe_length(room_size, point1, point2, case):
    if case == "adjacent_wall":
        # Výpočet pro sousední stěny
        distance = [abs(point1[i] - point2[i]) for i in range(3)]
        return sum(distance)
    elif case == "opposite_wall":
        point1 = [i for i in point1 if (i != 0) and (i != room_size)]
        point2 = [i for i in point2 if (i != 0) and (i != room_size)]

        point1_distances = distance_to_edges(point1, room_size)
        point2_distances = distance_to_edges(point2, room_size)

        distances = []

        for direction in range(4):
            point1_distance = point1_distances[direction]
            point2_distance = point2_distances[direction]

            between_points = [abs(point1[0] - point2[0]), abs(point1[1] - point2[1])]

            if direction%2==1:
                dist = point1_distance + point2_distance + room_size + between_points[0]
            else:
                dist = point1_distance + point2_distance + room_size + between_points[1]

            distances.append(dist)

        return min(distances)

    else:
        return 0

#Hlavní funkce
def main():
    path = 'test_cases/CZE/'
    for filename in os.listdir(path):
        if not "_in" in filename:
            continue
        with open(path+filename, 'r', encoding="utf-8") as file:
            lines = file.read().splitlines()
            
            try:
                room_size = int(lines[0])
                point1 = [int(i) for i in lines[1].split()]
                point2 = [int(i) for i in lines[2].split()]
            except:
                print(f"Nespravny vstup v souboru {filename}.\n")
                continue
                
            if not check_valid_input(point1,room_size) or not check_valid_input(point2,room_size):
                print(f"Nespravny vstup v souboru {filename}.\n")
                continue

            wall_case = detect_wall_case(point1, point2, room_size)
            pipe_length = calculate_pipe_length(room_size, point1, point2, wall_case)
            hose_length = calculate_hose_length(room_size, point1, point2, wall_case)

            print(f"Delka potrubi (soubor {filename}, {wall_case}): {pipe_length}")
            print(f"Delka hadice (soubor {filename}): {hose_length:.6f}\n")

# Spuštění programu
if __name__ == "__main__":
    main()
