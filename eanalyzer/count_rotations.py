def max_min_cross(p1, p2, q1, q2):
    p_min, p_max = min(p1, p2), max(p1, p2)
    q_min, q_max = min(q1, q2), max(q1, q2)

    if p_min > q_max or p_max < q_min:
        return False
    else:
        return True


def cross_judge(p1, p2, q1, q2):
    if not max_min_cross(p1[0], p2[0], q1[0], q2[0]):
        return False

    if not max_min_cross(p1[1], p2[1], q1[1], q2[1]):
        return False

    tc1 = (p1[0] - p2[0]) * (q1[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - q1[0])
    tc2 = (p1[0] - p2[0]) * (q2[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - q2[0])
    td1 = (q1[0] - q2[0]) * (p1[1] - q1[1]) + (q1[1] - q2[1]) * (q1[0] - p1[0])
    td2 = (q1[0] - q2[0]) * (p2[1] - q1[1]) + (q1[1] - q2[1]) * (q1[0] - p2[0])
    return tc1 * tc2 <= 0 and td1 * td2 <= 0


def count_rotations(head_coordinates):
    s = 0
    i = 1
    g = len(head_coordinates) - 1
    count = 0

    while i < g:
        if s == i - 1:
            i += 1
            continue
        elif cross_judge(head_coordinates[s], head_coordinates[s+1], head_coordinates[i], head_coordinates[i+1]):
            count += 1
            s = i
            i += 1
            continue
        else:
            i += 1
            continue

    return count


if __name__ == '__main__':
    head_coordinates = [[-4, -4], [-2, -3], [-5, -1], [-2, -4], [-2.5, -3],
                        [-4.5, -2], [-4.5, -1], [-2, -1.5], [-3.5, -3], [-5, -1.25]]

    print(count_rotations(head_coordinates))
