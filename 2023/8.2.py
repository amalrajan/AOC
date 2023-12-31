import sys
import math
import collections

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    directions = input().strip()
    directions = tuple(0 if ch == "L" else 1 for ch in directions)
    _ = input()

    graph = collections.defaultdict(tuple)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        else:
            # Source -> (Left, Right)
            source, RHS = line.split("=")
            left, right = RHS.strip()[1:-1].split(",")
            graph[source.strip()] = (left.strip(), right.strip())
    return directions, graph


def travel(source, directions, graph):
    # Directions tuple pointer
    dirx = 0

    stack = [source]
    steps = 0

    while stack:
        node = stack.pop()
        if node[-1] == "Z":
            break
        steps += 1
        stack.append(graph[node][directions[dirx]])
        dirx = (dirx + 1) % len(directions)

    return steps


def find_starting_nodes(graph):
    starting_nodes = []
    for node in graph:
        if node[-1] == "A":
            starting_nodes.append(node)

    return starting_nodes


def find_lcm(nums):
    if not nums:
        return []

    lcm = nums[0]
    for i in range(1, len(nums)):
        lcm = (lcm * nums[i]) // math.gcd(lcm, nums[i])

    return lcm


directions, graph = parse_input()

steps = []
for node in find_starting_nodes(graph):
    steps.append(travel(node, directions, graph))


print("Ans:", find_lcm(steps))
