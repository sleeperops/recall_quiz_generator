def shuffle(min,max):
    """
    Creates a list of numbers in a random order. 
    Accepts a minimum and maximum number and returns a randomly ordered list of numbers in that range.
    """
    # A list of randomly ordered numbers
    shuffled_sequence = []

    while len(shuffled_sequence) != max:  # Loop until the amount of numbers in the list matches the length of the range
        random_num = random.randint(min, max)  # Generate a random number in the specified range
        if random_num not in shuffled_sequence:  # If the random number is not yet in the list
            shuffled_sequence.append(random_num)  # Add it to the list

    return shuffled_sequence