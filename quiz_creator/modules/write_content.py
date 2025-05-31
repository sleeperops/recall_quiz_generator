class WriteFile:
    
    """
    This module contains the functions that allows the user to write contents to the quiz file
    """

    def write_question(input_question, file_directory):
        """
        Accepts a question and writes it into a specified file
        """
        with open(file_directory, "a") as fd:  # Writes the question into the specified file
            fd.write(f'''Q: {input_question}
    ''')

    def write_option(file_directory):
        """
        Asks for the options and writes it into a specified file
        """
        with open(file_directory, "a") as fd:
            for char in "abcd":  # Creates a block of string with that contains the options
                option = input(f"Option {char}: ")
                fd.write(f'''{option}
    ''')


    def write_correct(input_answer, file_directory):
        """
        Accepts and writes the correct answer into the specified file
        """
        with open(file_directory, "a") as question_file:  # Writes the correct answer into the file
            question_file.write(f'''A: {input_answer}
    ''')