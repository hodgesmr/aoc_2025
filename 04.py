from utils import timed, get_input_lines


def part_1(input_lines):
    count = 0

    lookup_table = {}

    for i, line in enumerate(input_lines):
        for j, cell in enumerate(line):

            adjacent_count = 0

            if cell == "@":
                lookup_table[(i, j)] = True

                # East
                if j < len(line) - 1:
                    coord = (i, j + 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = line[j + 1] == "@"
                    adjacent_count += lookup_table[coord]

                # West
                if j > 0:
                    coord = (i, j - 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = line[j - 1] == "@"
                    adjacent_count += lookup_table[coord]

                # North
                if i > 0:
                    coord = (i - 1, j)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i - 1][j] == "@"
                    adjacent_count += lookup_table[coord]

                # South
                if i < len(input_lines) - 1:
                    coord = (i + 1, j)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i + 1][j] == "@"
                    adjacent_count += lookup_table[coord]

                # NE
                if i > 0 and j < len(line) - 1:
                    coord = (i - 1, j + 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i - 1][j + 1] == "@"
                    adjacent_count += lookup_table[coord]

                # NW
                if i > 0 and j > 0:
                    coord = (i - 1, j - 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i - 1][j - 1] == "@"
                    adjacent_count += lookup_table[coord]

                # SE
                if i < len(input_lines) - 1 and j < len(line) - 1:
                    coord = (i + 1, j + 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i + 1][j + 1] == "@"
                    adjacent_count += lookup_table[coord]

                # SW
                if i < len(input_lines) - 1 and j > 0:
                    coord = (i + 1, j - 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i + 1][j - 1] == "@"
                    adjacent_count += lookup_table[coord]

                if adjacent_count < 4:
                    count += 1

    return count


def part_2(input_lines):
    count = 0

    lookup_table = {}
    to_remove = set()

    # First pass, build the lookup table and initial removable set
    for i, line in enumerate(input_lines):
        for j, cell in enumerate(line):

            adjacent_count = 0

            if cell == "@":
                lookup_table[(i, j)] = True

                # East
                if j < len(line) - 1:
                    coord = (i, j + 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = line[j + 1] == "@"
                    adjacent_count += lookup_table[coord]

                # West
                if j > 0:
                    coord = (i, j - 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = line[j - 1] == "@"
                    adjacent_count += lookup_table[coord]

                # North
                if i > 0:
                    coord = (i - 1, j)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i - 1][j] == "@"
                    adjacent_count += lookup_table[coord]

                # South
                if i < len(input_lines) - 1:
                    coord = (i + 1, j)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i + 1][j] == "@"
                    adjacent_count += lookup_table[coord]

                # NE
                if i > 0 and j < len(line) - 1:
                    coord = (i - 1, j + 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i - 1][j + 1] == "@"
                    adjacent_count += lookup_table[coord]

                # NW
                if i > 0 and j > 0:
                    coord = (i - 1, j - 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i - 1][j - 1] == "@"
                    adjacent_count += lookup_table[coord]

                # SE
                if i < len(input_lines) - 1 and j < len(line) - 1:
                    coord = (i + 1, j + 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i + 1][j + 1] == "@"
                    adjacent_count += lookup_table[coord]

                # SW
                if i < len(input_lines) - 1 and j > 0:
                    coord = (i + 1, j - 1)
                    if coord not in lookup_table:
                        lookup_table[coord] = input_lines[i + 1][j - 1] == "@"
                    adjacent_count += lookup_table[coord]

                if adjacent_count < 4:
                    to_remove.add((i, j))

            else:
                lookup_table[(i, j)] = False

    # 2+n pass; mutate the lookup table
    while to_remove:
        while to_remove:  # clear out the removable set and keep count
            removable = to_remove.pop()
            lookup_table[removable] = False
            count += 1

        # rebuild the removable set
        for i in range(len(input_lines)):
            for j in range(len(input_lines[0])):

                adjacent_count = 0

                if lookup_table[(i, j)] == True:

                    # East
                    if j < len(line) - 1:
                        coord = (i, j + 1)
                        adjacent_count += lookup_table[coord]

                    # West
                    if j > 0:
                        coord = (i, j - 1)
                        adjacent_count += lookup_table[coord]

                    # North
                    if i > 0:
                        coord = (i - 1, j)
                        adjacent_count += lookup_table[coord]

                    # South
                    if i < len(input_lines) - 1:
                        coord = (i + 1, j)
                        adjacent_count += lookup_table[coord]

                    # NE
                    if i > 0 and j < len(line) - 1:
                        coord = (i - 1, j + 1)
                        adjacent_count += lookup_table[coord]

                    # NW
                    if i > 0 and j > 0:
                        coord = (i - 1, j - 1)
                        adjacent_count += lookup_table[coord]

                    # SE
                    if i < len(input_lines) - 1 and j < len(line) - 1:
                        coord = (i + 1, j + 1)
                        adjacent_count += lookup_table[coord]

                    # SW
                    if i < len(input_lines) - 1 and j > 0:
                        coord = (i + 1, j - 1)
                        adjacent_count += lookup_table[coord]

                    if adjacent_count < 4:
                        to_remove.add((i, j))

                else:
                    lookup_table[(i, j)] = False

    return count


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
