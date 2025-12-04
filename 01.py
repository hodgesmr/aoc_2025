from utils import timed, get_input_lines


def part_1(input_lines):
    zeros = 0
    position = 50

    for line in input_lines:
        turn = int(line[1:])  # grab the numeric value
        if line[0] == "L":  # subtract then mod
            position = (position - turn) % 100
        else:  # add the mod
            position = (position + turn) % 100

        if not position:  # 0 is Falsy
            zeros += 1

    return zeros


def part_2(input_lines):
    zeros = 0
    position = 50

    for line in input_lines:
        turn = int(line[1:])  # grab the numeric value
        if line[0] == "L":
            # floor division of negative numbers give negaitive quotient
            zeros += abs(((position - turn) // 100))
            position = (position - turn) % 100
        else:
            zeros += (position + turn) // 100
            position = (position + turn) % 100

    return zeros


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
