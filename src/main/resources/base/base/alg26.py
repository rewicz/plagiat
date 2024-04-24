def find_max(collection):
    if len(collection) == 0:
        return "No input to process"
    max_element = collection[0]
    for element in collection:
        if element > max_element:
            max_element = element
    return max_element