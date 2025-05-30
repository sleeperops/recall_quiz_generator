def read_quiz(file_directory):
    """
    Reads the quiz.txt file and extracts each questions into a list
    Accepts the file directory of the quiz.txt and returns a list with all the questions
    """
    
    # Stores each lines extracted from the quiz.txt
    lines_list = []  

    # Use a context manager to open and automatically close the file once the lines have been extracted
    with open(file_directory, "r") as quiz:
        temp_lines_list = quiz.readlines()  # Stores each lines of the quiz.txt file to a temporary list before stripping      
        
        # Loops through the entire list and removes the /n in each line that is in that list
        for line in temp_lines_list: 
            line = str(line)  # Converts the lines into a string so that the strip method could be applied
            if line == "///":  
                continue
            else:
                lines_list.append(line.strip())  

    return lines_list  
