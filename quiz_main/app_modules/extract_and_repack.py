class ExtractRepack:
    
    def extract_and_repack(lines_list):
        """
        Extracts each lines from the line_list and uses it to create an instance of the class named 'Item'.
        Accepts a list of lines that is read from the questions.txt file.
        Returns a list of instances of the class 'Item'. 
        """

        # A list of objects (referred to as items) of the class 'Item'. The lines from line_list are passed as properties of these items
        quiz_dict = {}

        # Assign each item a number as a form of identifier.
        counter = 1

        # Loop through 'line_list' using the 'lines' variable to track the current line and 'index' to track its index
        for index, lines in enumerate(lines_list):  
            if str(lines).startswith("Q:") == True:  # If the line starts with the 'Q:' prefix, construct an instance of the class 'Item' with the following properties:
                question = lines
                option_a = lines_list[index + 1]
                option_b = lines_list[index + 2]
                option_c = lines_list[index + 3]
                option_d = lines_list[index + 4]
                correct_answer = lines_list[index + 5]

                # Construct an instance of the class 'Item' using the above lines as properties
                question_item = Item(question, option_a, option_b, option_c, option_d, correct_answer) 

                # Store each item in a dictionary using the property 'question' as the key and the item itself as the value
                quiz_dict[counter] = question_item 

                # Increments by 1 for every loop
                counter += 1

        return quiz_dict
