import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from tqdm import tqdm
import console_color


def detect_head(FILE_NAME):
    data_list = []

    with open(FILE_NAME, 'r+') as f:
        for line in f:
            line_list = line.split()
            line_list = [float(i) for i in line_list]
            data_list.append(line_list)
        print(
            f'{console_color.BOLD}{console_color.HEADER}Making a tuple list of coordinates{console_color.ENDC}')

    coordinates = []
    for i in tqdm(range(len(data_list)), desc='Processing'):
        each_coordinates = []
        for j in range(1, len(data_list[i]) - 1, 2):
            each_coordinates.append(
                list([data_list[i][j], data_list[i][j+1]]))
        coordinates.append(each_coordinates)
    # print(coordinates)

    print(
        f'{console_color.BOLD}{console_color.HEADER}Making a combintation list{console_color.ENDC}')
    coordinates_combination = []
    for coordinate in tqdm(coordinates):
        combination = list(itertools.combinations(coordinate, 2))
        coordinates_combination.append(combination)

    print(
        f'{console_color.BOLD}{console_color.OKGREEN}Calculating distances{console_color.ENDC}')

    coordinates_combination_list = []
    for i in range(len(coordinates_combination)):
        coordinates_combination_list.append([])
        for j in range(len(coordinates_combination[i])):
            coordinates_combination_list[i].append(
                list(coordinates_combination[i][j]))

    for i in range(len(coordinates_combination_list)):
        for j in range(len(coordinates_combination_list[i])):
            x = np.array(coordinates_combination_list[i][j][0])
            y = np.array(coordinates_combination_list[i][j][1])
            try:
                distance = np.linalg.norm(y-x)
            except:
                distance = 0

            coordinates_combination_list[i][j].append(distance)

    # compaare
    head_coordinates_list = []
    for i in range(len(coordinates_combination_list)):
        distance = [row[2] for row in coordinates_combination_list[i]]
        distance_maximum = max(distance)
        distance_maximum_index = distance.index(distance_maximum)

        coordinates_combination_list_r = coordinates_combination_list.copy()
        del coordinates_combination_list_r[i][distance_maximum_index]
        distance = [row[2] for row in coordinates_combination_list_r[i]]
        distance_second = max(distance)
        distance_second_index = distance.index(distance_second)

        distance_maximum_list = coordinates_combination_list[i][distance_maximum_index]
        distance_second_list = coordinates_combination_list_r[i][distance_second_index]

        if (np.any(distance_maximum_list[0] == distance_second_list[0] or distance_maximum_list[0] == distance_second_list[1])):
            head_coordinates_list.append(distance_maximum_list[0])
        elif (np.any(distance_maximum_list[1] == distance_second_list[0] or distance_maximum_list[1] == distance_second_list[1])):
            head_coordinates_list.append(distance_maximum_list[1])
        else:
            head_coordinates_list.append(list([(distance_maximum_list[0][0] + distance_maximum_list[1][0]) /
                                               2, (distance_maximum_list[0][1] + distance_maximum_list[1][1])/2]))

    return head_coordinates_list


if __name__ == '__main__':
    FILE_NAME = './debug/data/euglena-m1_2.txt'
    result = detect_head(FILE_NAME)
    print(result)
