# JAVA

# (Bubble Sort): Sorts an array of integers using the bubble sort algorithm.
# gpt 3.5
# Sorting algorithm implementing the bubble sort technique. It iterates over the array, swapping adjacent elements if they are in the wrong order, until no more swaps are needed.
# gpt 4
# [Reverse Bubble Sort]: This algorithm sorts a list in ascending order by repeatedly traversing it backward, swapping adjacent elements if they are in the wrong order, until no more swaps are needed, indicating the list is sorted.
def alg1(array):
    while True:
        changed = False
        for i in range(len(array) - 1, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                changed = True
        if not changed:
            break

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.triggered = False
        self.expand = False

# (Tree Node Replacement): Modifies a tree by replacing the children of a node that matches a given key with new nodes.
# gpt 3.5
# Updates a tree node by matching its key with the provided title. If a match is found, updates the node's children with new nodes.
# gpt 4
# [Tree Node Update]: This algorithm searches through a tree structure for a node with a specified key, updates that node's children with new nodes, and sets its 'triggered' status to true if the node is found, applying the update recursively to all child nodes.
def alg2(element, matching_title, new_nodes):
    if element is None:
        return None
    if element.key == matching_title:
        element.children = new_nodes
        element.triggered = True
        return element
    for child in element.children:
        alg2(child, matching_title, new_nodes)
    return element


# (Find Parent Node): Finds the parent node of a given child node in a tree.
# gpt 3.5
# Searches for a node in a tree structure based on a matching title, returning its parent node if found.
# gpt 4
# [Find Parent Node]: This algorithm searches a tree structure to find the parent node of a specified node (identified by a matching key), returning the first parent node encountered in a depth-first search manner. If no such parent exists, it returns None.
def alg3(element, matching_title):
    if element is None or element.children is None:
        return None

    for child in element.children:
        if child.key == matching_title:
            return element
        parent = alg3(child, matching_title)
        if parent is not None:
            return parent

    return None

# (Collect Keys): Collects and returns keys from a tree in a list, stopping at a specified key.
# gpt 3.5
# Recursively searches for all keys of child nodes under a given element until the temporary key is found, returning a list of keys.
# gpt 4
# [Collect Keys Excluding Match]: This algorithm traverses a tree structure, collecting the keys of all nodes except those that match a specified key, and returns a list of these keys as strings, avoiding traversal beyond nodes that match the specified key.
def alg4(element, temp_key):
    if element is None or element.key == temp_key:
        return []
    array_keys = [str(element.key)]
    if element.children is None:
        return array_keys

    for child in element.children:
        parent_keys = alg4(child, temp_key)
        array_keys.extend(parent_keys)
    return array_keys

# (Find Maximum Value): Finds and returns the maximum value in an array.
# gpt 3.5
# Finds the maximum value in an array, throwing an exception if the array is empty or null.
# gpt 4
# [Find Maximum Value]: This algorithm iterates through a list to identify and return the maximum value present. It raises an error if the list is empty.
def alg5(array):
    if not array:
        raise ValueError("Array is empty or null")
    max_value = array[0]
    for value in array:
        if value > max_value:
            max_value = value
    return max_value

# (Factorial Calculation): Calculates the factorial of a non-negative integer.
# gpt 3.5
# Computes the factorial of a non-negative integer using iteration, raising an exception if the input is negative.
# gpt 4
# [Calculate Factorial]: This algorithm computes the factorial of a non-negative integer by multiplying all positive integers up to that number together, returning the result. It raises an error if the input number is negative.
def alg6(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# (Safe Array Access): Safely accesses an array element with a default value if out of bounds.
# gpt 3.5
# Retrieves the value from an array at the specified index, returning a default value if the index is out of bounds or the array is empty.
# gpt 4
# [Safe Element Retrieval]: This algorithm retrieves an element from a list at a specified index, returning a default value if the index is out of bounds or the list is None, ensuring safe access to list elements.
def alg7(array, index, default_value):
    if array is None or index < 0 or index >= len(array):
        return default_value
    return array[index]

# (Bubble Sort Optimization): Optimized bubble sort algorithm that stops early if no swaps are needed.
# gpt 3.5
# Implements the bubble sort algorithm to sort an array in ascending order.
# gpt 4
# [Bubble Sort]: This algorithm sorts a list by repeatedly traversing it, swapping adjacent elements if they are in the wrong order, and stops early if no swaps are made during a complete pass, indicating the list is sorted.
def alg8(array):
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

# (Array Summation): Computes the sum of all elements in an array.
# gpt 3.5
# Calculates the sum of all elements in an array.
# gpt 4
# [Sum of List]: This algorithm calculates and returns the total sum of all elements in a list.
def alg9(array):
    return sum(array)

# (Greatest Common Divisor): Calculates the greatest common divisor of two numbers.
# gpt 3.5
# Finds the greatest common divisor of two integers using the Euclidean algorithm.
# gpt 4
# [Euclidean Algorithm for GCD]: This algorithm finds the greatest common divisor (GCD) of two numbers by repeatedly applying the Euclidean algorithm, where the second number is replaced by the remainder of the first number divided by the second number until the second number becomes zero.
def alg10(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# (Sum of Array Elements): Similar to alg9, this function computes the sum of all elements in an array.
# gpt 3.5
# Computes the sum of all elements in an array.
# gpt 4
# [Sum of List]: This algorithm computes and returns the sum of all elements within a list, effectively aggregating their total value.
def alg11(array):
    return sum(array)

# (Majority Element Finder): Finds the majority element in an array, if it exists.
# gpt 3.5
# Finds the majority element in an array, if it exists, using the Boyer-Moore Majority Vote algorithm.
# gpt 4
# [Majority Element Finder]: This algorithm identifies the majority element in a list, which is an element that appears more than half of the time. It first uses the Boyer-Moore voting algorithm to find a candidate, then verifies if the candidate truly is the majority by counting its occurrences.
def alg12(array):
    count = 0
    candidate = None

    for number in array:
        if count == 0:
            candidate = number
        if number == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for number in array:
        if number == candidate:
            count += 1

    if count > len(array) / 2:
        return candidate
    return None

# (Sieve of Eratosthenes): Generates a list of boolean values representing whether numbers are prime up to a given limit.
# gpt 3.5
# Generates a list of boolean values indicating whether numbers are prime up to a given limit using the Sieve of Eratosthenes algorithm.
# gpt 4
# [Sieve of Eratosthenes]: This algorithm generates a list indicating the primality of numbers up to n by initially assuming all numbers are prime and then iteratively marking the multiples of each prime number, starting from 2, as non-prime.
def alg13(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return primes

# (Insertion Sort): Sorts an array using the insertion sort method.
# gpt 3.5
# Sorts an array using the insertion sort algorithm.
# gpt 4
# [Insertion Sort]: This algorithm sorts a list by sequentially taking each element and inserting it into its correct position within the already sorted part of the list, ensuring each iteration leaves the list sorted up to the current element.
def alg14(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current

# (Shell Sort): An optimized version of insertion sort known as shell sort.
# gpt 3.5
# Sorts an array using the shell sort algorithm, an optimized version of insertion sort.
# gpt 4
# [Shell Sort]: This algorithm enhances insertion sort by initially sorting elements far apart from each other using a gap, then gradually reducing the gap and sorting until the list is completely sorted.
def alg15(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

# (Decimal to Binary Conversion): Converts a decimal number to its binary representation.
# gpt 3.5
# Converts a decimal number to its binary representation.
# gpt 4
# [Binary Conversion]: This algorithm converts a given number into its binary representation as a string, excluding the '0b' prefix that indicates binary in Python.
def alg16(number):
    return bin(number)[2:]

# (Dijkstra) Find the shortest paths from a starting node to all other nodes in a graph represented as an adjacency matrix.
# gpt 3.5
# Finds the shortest distances from a given start node to all other nodes in a graph using Dijkstra's algorithm.
# gpt 4
# [Dijkstra's Shortest Path Algorithm]: This algorithm calculates the shortest paths from a start node to all other nodes in a graph, initializing distances to infinity except for the start node, and iteratively updating the shortest distance to each node by considering all its unvisited neighbors and choosing the path that offers the lowest total distance.
def alg17(graph, start_node):
    n_vertices = len(graph)
    shortest_distances = [float('inf')] * n_vertices
    added = [False] * n_vertices

    shortest_distances[start_node] = 0

    for _ in range(1, n_vertices):
        nearest_vertex = -1
        shortest_distance = float('inf')
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        added[nearest_vertex] = True

        for vertex_index in range(n_vertices):
            edge_distance = graph[nearest_vertex][vertex_index]

            if edge_distance > 0 and ((shortest_distance + edge_distance) < shortest_distances[vertex_index]):
                shortest_distances[vertex_index] = shortest_distance + edge_distance

# Change of Base to Vector
# gpt 3.5
# Converts a decimal number to its equivalent in a given base, returning a list representing the number in that base.
# gpt 4
# [Base Conversion]: This algorithm converts a given non-negative integer into a specified base, generating a list of digits in that base, and returns the list in the correct order, starting from the least significant digit to the most significant.
def alg18(base, number):
    if number < 0:
        return None

    if number == 0:
        return [0]

    vector = []
    while number > 0:
        vector.append(number % base)
        number = number // base

    return vector[::-1]


//CPP

# //(Insertion Sort): Sorts an array using the insertion sort method.
# gpt 3.5
# Sorts an array of integers in non-decreasing order using the insertion sort algorithm.
# gpt 4
# [Insertion Sort]: This algorithm sorts a list by repeatedly taking each element and inserting it into its correct position within the sorted portion of the list, ensuring the list is sorted incrementally from the beginning to the end.
def alg19(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current

# // (Shell Sort): An optimized version of insertion sort known as shell sort.
# gpt 3.5
# Sorts an array of integers in non-decreasing order using the shell sort algorithm, an optimized version of insertion sort.
# gpt 4
# [Shell Sort]: Enhances the insertion sort algorithm by initially sorting elements that are far apart from each other (determined by 'gap'), then gradually reducing the gap to perform finer sorting, until the gap is 1 and the list is fully sorted.
def alg20(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

# (Decimal to Binary Conversion): Converts a decimal number to its binary representation.
# gpt 3.5
# Converts a decimal number to its binary representation using the built-in format function.
# gpt 4
# [Binary Representation with Padding]: This algorithm converts a given number into a binary string representation, ensuring it is padded to 32 bits in length, filling with leading zeros if necessary.
def alg21(number):
    return format(number, '032b')

# Dijkstra's
# gpt 3.5
# Finds the shortest distances from a given start node to all other nodes in a graph using Dijkstra's algorithm.
# gpt 4
# [Dijkstra's Algorithm for Shortest Paths]: This algorithm finds the shortest paths from a starting node to all other nodes in a weighted graph, updating the shortest known distance to each node iteratively and using a "visited" marker to avoid re-evaluating nodes.
def alg22(graph, start_node):
    n_vertices = len(graph)
    shortest_distances = [float('inf')] * n_vertices
    added = [False] * n_vertices

    shortest_distances[start_node] = 0

    for _ in range(1, n_vertices):
        nearest_vertex = -1
        shortest_distance = float('inf')
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        added[nearest_vertex] = True

        for vertex_index in range(n_vertices):
            if graph[nearest_vertex][vertex_index] > 0:
                edge_distance = graph[nearest_vertex][vertex_index]
                if shortest_distance + edge_distance < shortest_distances[vertex_index]:
                    shortest_distances[vertex_index] = shortest_distance + edge_distance

# Verhoeff
# gpt 3.5
# Checks if a given number is a multiple of 3 using finite automata and a predetermined table.
# gpt 4
# [Dihedral Group Permutation Check]: This algorithm checks if a sequence represented by a number conforms to a specific condition defined by dihedral group operations and a permutation table, evaluating the sequence in reverse and updating a condition variable through table lookups. It concludes by verifying if the final condition matches a target value, indicating conformity to the specified pattern.
def alg23(number):
    c = 0
    d = [[...]] # Dihedral group, replace ... with actual values
    p = [[...]] # Permutation table, replace ... with actual values
    length = len(number)

    for i in range(length):
        digit = int(number[length - i - 1])
        c = d[c][p[i % 8][digit]]

    return c == 0

//PASCAL
# Change Base to Vector
# gpt 3.5
# Converts a decimal number to a base-N representation.
# gpt 4
# [Base Conversion with Count]: This algorithm converts a given non-negative integer into a specified base, then prepends the total count of digits in the converted form to the result, returning a list where the first element is the digit count followed by the digits of the number in the new base.
def alg24(pods, liczba):
    if liczba < 0:
        return []
    if liczba == 0:
        return [1, 0]
    v = []
    i = 0
    while liczba > 0:
        v.append(liczba % pods)
        liczba = liczba // pods
        i += 1
    w = [i] + v[::-1]
    return w

# Change Base Vector to Number
# gpt 3.5
# Converts a base-N representation to a decimal number.
# gpt 4
# [Reverse Base Conversion with Count]: This algorithm converts a list, where the first element indicates the count of the following elements (digits in a base), back into a decimal number by calculating the sum of each digit multiplied by its base raised to the corresponding power, effectively reversing a base conversion that includes a leading digit count.
def alg25(pods, v):
    suma = 0
    j = 0
    for i in range(v[0], 0, -1):
        suma += v[i] * (pods ** j)
        j += 1
    return suma


//PYTHON
# find max
# gpt 3.5
# Finds the maximum element in a collection of numbers.
# gpt 4
# [Find Maximum Element]: This algorithm iterates through a collection to identify and return the maximum element. If the collection is empty, it returns a message indicating there is no input to process.
def alg26(collection):
    if len(collection) == 0:
        return "No input to process"
    max_element = collection[0]
    for element in collection:
        if element > max_element:
            max_element = element
    return max_element


# minimum_distance
# gpt 3.5
# Finds the index of the minimum element in a list, ignoring visited nodes.
# gpt 4
# [Find Nearest Unvisited Node]: This algorithm searches through a list of distances to find the unvisited node with the smallest distance, returning the index of that node. It is typically used in graph algorithms to select the next node to visit.
def alg27(distance, visited):
    minimum = math.inf
    min_index = -1
    for v in range(len(distance)):
        if distance[v] < minimum and (not visited[v]):
            minimum = distance[v]
            min_index = v
    return min_index

# a_star_algorithm
# gpt 3.5
# Finds the shortest path between two points in a graph using the A* algorithm.
# gpt 4
# [A Pathfinding Algorithm]**: This algorithm finds the shortest path between a start and end point in a graph using the A search algorithm. It calculates costs (g, h, f) for each node, where g is the cost from the start node, h is the heuristic estimated cost to the end node, and f is the total cost of the node. Nodes are added to an open list for exploration and moved to a closed list once explored, with the path being reconstructed from the end node to the start node once the end is reached.
def alg28(graph, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_nodes = []
    closed_nodes = []
    open_nodes.append(start_node)

    while len(open_nodes) > 0:
        current_node = open_nodes[0]
        current_idx = 0

        for idx, node in enumerate(open_nodes):
            if node.f < current_node.f:
                current_node = node
                current_idx = idx

        open_nodes.pop(current_idx)
        closed_nodes.append(current_node)

        if current_node == end_node:
            path = []
            temp = current_node
            while temp is not None:
                path.append(temp.cord)
                temp = temp.parent
            return [(t[1], t[0]) for t in path][::-1]

        neighbours = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            current_position = (current_node.cord[0] + new_position[0], current_node.cord[1] + new_position[1])

            if current_position[0] > (len(graph) - 1) or current_position[0] < 0 or current_position[1] > (
                    len(graph[len(graph) - 1]) - 1) or current_position[1] < 0:
                continue

            if graph[current_position[0]][current_position[1]] != 0:
                continue

            new_node = Node(current_node, current_position)
            neighbours.append(new_node)

        for neighbour in neighbours:
            for closed in closed_nodes:
                if neighbour == closed:
                    continue

            neighbour.g = current_node.g + 1
            neighbour.h = calculate(neighbour, end_node)
            neighbour.f = neighbour.g + neighbour.h

            for opened in open_nodes:
                if neighbour == opened and neighbour.g > opened.g:
                    continue

            open_nodes.append(neighbour)

# floyd_warshall_algorithm
# gpt 3.5
# Finds all-pairs shortest paths in a weighted graph using the Floyd-Warshall algorithm.
# gpt 4
# [Floyd-Warshall Algorithm]: This algorithm computes the shortest paths between all pairs of vertices in a graph, updating the distances matrix by considering each vertex as an intermediate point and minimizing the distance between every pair of vertices through it.
def alg29(graph):
    n = len(graph)
    distance = copy.deepcopy(graph)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

    return distance

# boyer_moore_algorithm
# gpt 3.5
# Finds occurrences of a pattern within a string using the Boyer-Moore algorithm.
# gpt 4
# [Boyer-Moore String Search Algorithm]: This algorithm efficiently searches for occurrences of a pattern within a string by using a preprocessed table to skip sections of the text that cannot possibly match the pattern, significantly reducing the number of comparisons. It updates its position within the string based on the last occurrence of the mismatched character in the pattern, moving more intelligently than simple character-by-character comparison.
def alg30(string, pattern):
    s_len = len(string)
    p_len = len(pattern)

    chars = [-1] * 200
    for p in range(p_len):
        chars[ord(pattern[p])] = p

    i = 0
    while i <= s_len - p_len:
        p = p_len - 1

        while p >= 0 and pattern[p] == string[i + p]:
            p -= 1

        if p < 0:
            if i + p_len < s_len:
                i += (p_len - chars[ord(string[i + p_len])])
            else:
                i += 1
        else:
            i += max(1, p - chars[ord(string[i + p])])

# karp_rabin_algorithm
# gpt 3.5
# Finds occurrences of a pattern within a string using the Rabin-Karp algorithm.
# gpt 4
# [Hash-Based Pattern Matching]: This algorithm uses hash values to search for a pattern within a string, comparing the hash of the pattern with the hash of current substrings of equal length. It increments a counter for each match found and moves through the string, recalculating hashes and checking against the pattern's hash. If no matches are found, it outputs a message indicating the absence of the pattern.
def alg31(string, pattern):

    string_len = len(string)
    pattern_len = len(pattern)

    p_hash = hash(pattern)
    s_hash = hash(string[0:pattern_len])

    counter = 0

    for i in range(string_len - pattern_len + 1):
        if s_hash != p_hash:
            s_hash = hash(string[i:i + pattern_len])
        else:
            counter += 1
            s_hash = hash(string[i:i + pattern_len])

    if counter == 0:
        print('No matching pattern in given string')

# cezar_algorithm
# gpt 3.5
# Performs Caesar cipher encryption on a string with a given step value.
# gpt 4
# [Caesar Cipher Shift]: This algorithm shifts each letter in a given string by a specified number of positions in the alphabet, wrapping around if necessary, and leaves non-alphabet characters unchanged, effectively implementing a Caesar cipher encryption or decryption.
def alg32(step, string):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for s in string:
        idx = alphabet.find(s)

        if idx == -1:
            result += s
        else:
            new_index = (idx + step) % len(alphabet)
            result += alphabet[new_index]

    return result

# bubble_sort_algorithm
# gpt 3.5
# Implements selection sort to sort a list of elements.
# gpt 4
# [Bubble Sort]: This algorithm sorts a list by repeatedly comparing and swapping adjacent elements if they are in the wrong order, ensuring each element moves to its correct position through a series of passes over the entire list.
def alg33(d):
    if len(d) <= 1:
        return d

    for i in range(len(d)):
        for j in range(len(d)):
            if d[i] < d[j]:
                tmp = d[i]
                d[i] = d[j]
                d[j] = tmp
    return d

# quick_sort_algorithm
# gpt 3.5
# Implements quick sort to sort a list of elements.
# gpt 4
def alg34(d):
    if len(d) <= 1:
        return d
    less = []
    equal = []
    more = []

    pivot = d[0]
    for n in d:
        if n < pivot:
            less.append(n)
        elif n == pivot:
            equal.append(n)
        elif n > pivot:
            more.append(n)
    return alg34(less) + equal + alg34(more)

# prime alg
# gpt 3.5
# Finds the minimum spanning tree of a graph using the Prim's algorithm.
# gpt 4
def alg35(graph, n, start):
    visited = [False] * n
    visited[start] = True
    t = []

    for i in range(n - 1):
        minimum = math.inf
        x = 0
        y = 0
        for j in range(n):
            if visited[j]:
                for k in range(n):
                    if (not visited[k]) and graph[j][k]:
                        if minimum > graph[j][k]:
                            minimum = graph[j][k]
                            x = j
                            y = k
        visited[y] = True
        t.append((x, y, graph[x][y]))
    return t
