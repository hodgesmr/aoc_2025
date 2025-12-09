from bisect import bisect_right
from utils import timed, get_input_lines


def parse_ingredients(input_lines):
    ranges = []
    ids = []
    parsing_ids = False
    for line in input_lines:
        if line == "":
            parsing_ids = True
        elif not parsing_ids:
            ranges.append([int(item) for item in line.split("-")])
        else:
            ids.append(int(line))

    return ranges, ids


def build_range_index(ranges):
    # This merges overlapping ranges
    # ranges: iterable of (start, end) pairs
    # First sort ranges by start (end as tiebreaker) so we can merge overlaps
    ranges = sorted(ranges)
    merged = []
    for s, e in ranges:
        # If there are no merged ranges yet, or this range starts after
        # the end of the last merged range, start a new disjoint interval
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            # Otherwise, the current range overlaps or touches the last one
            # Extend the end of the last merged range
            if e > merged[-1][1]:
                merged[-1][1] = e
    # Split merged disjoint intervals into parallel arrays
    starts = [s for s, _ in merged]
    ends = [e for _, e in merged]
    return starts, ends


def in_any_range(x, starts, ends):
    # Find the index of the rightmost interval whose start <= x.
    # bisect_right gives the insertion point to keep starts sorted,
    # so subtract 1 to get the interval
    i = bisect_right(starts, x) - 1
    if i < 0:
        # x is smaller than the first start so it can't be in any interval
        return False
    # Check if x is within the candidate interval's end
    return x <= ends[i]


def part_1(input_lines):
    ranges, ids = parse_ingredients(input_lines)
    starts, ends = build_range_index(ranges)
    return sum([in_any_range(id, starts, ends) for id in ids])


def part_2(input_lines):
    ranges, _ = parse_ingredients(input_lines)
    starts, ends = build_range_index(ranges)

    count = 0
    for i, end in enumerate(ends):
        count += (end + 1) - starts[i]

    return count


timed(part_1, [get_input_lines()])
timed(part_2, [get_input_lines()])
