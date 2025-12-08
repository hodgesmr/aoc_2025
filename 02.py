from utils import timed, get_input_lines


def part_1(input_lines):
    sum = 0

    ranges_strings = input_lines[0].split(",")
    for range_string in ranges_strings:
        range_parts = range_string.split("-")
        r = range(
            int(range_parts[0]), int(range_parts[1]) + 1
        )  # +1 b/c exclusive stop value
        for i in r:
            # if the two halves of the string match, add it
            str_i = str(i)
            a = str_i[(len(str_i) // 2) :]
            b = str_i[: (len(str_i) // 2)]
            if a == b:
                sum += i
    return sum


def part_2(input_lines):
    sum = 0

    ranges_strings = input_lines[0].split(",")
    for range_string in ranges_strings:
        range_parts = range_string.split("-")
        r = range(
            int(range_parts[0]), int(range_parts[1]) + 1
        )  # +1 b/c exclusive stop value
        for i in r:
            str_i = str(i)

            #  The longest possible match substring is half the string
            str_i_len = len(str_i)
            max_sub_len = str_i_len // 2

            # loop over all the possible lenghts of substrings less than half, always starting at the index 0
            for j in range(0, (max_sub_len)):
                sub = str_i[0 : max_sub_len - j]

                # Once we have a substring, multiply it to lenght of the original string
                mult = str_i_len // (max_sub_len - j)
                val = sub * mult

                # See if it's a match
                if val == str_i:
                    sum += i
                    break

    return sum


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
