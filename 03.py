from utils import timed, get_input_lines


def part_1(input_lines):
    sum = 0

    for bank in input_lines:
        max_1 = max(bank[:-1])
        max_1_index = bank.index(max_1)
        max_2 = max(bank[max_1_index + 1 :])

        sum += (10 * int(max_1)) + int(max_2)

    return sum


def part_2(input_lines):
    num_batteries = 12
    total_joltage = 0

    def find_digits(digits, num_batteries, result=0):
        # Current number of digits already chosen into `result`
        curr_len = len(str(result)) if result else 0

        # Base case: we have exactly the required number of digits
        if curr_len == num_batteries:
            return result

        # How many more digits we still need to pick
        remaining_needed = num_batteries - curr_len

        # We can only search up to a point where there will still be enough
        # digits left after the chosen one to fill out the remaining_needed - 1
        search_end = len(digits) - (remaining_needed - 1)

        # Choose the largest digit within the allowed search window
        # to maximize the resulting number while preserving order
        search_window = digits[:search_end]
        next_max = max(search_window)
        next_max_index = digits.index(next_max)

        # Append the chosen digit to the result
        updated_result = result * 10 + int(next_max)

        # Recurse on the suffix after the chosen digit
        return find_digits(digits[next_max_index + 1 :], num_batteries, updated_result)

    for bank in input_lines:
        total_joltage += find_digits(bank, num_batteries)

    return total_joltage



timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
