from modules.write_content import WriteFile

# Directory of the quiz file that stores all formatted questions
quiz_directory = r"quiz_main/quiz_creator/quiz_file/quiz_file.txt"

# Runs a loop; accepts and writes the inputs until the user decides to exit
while True: 
    # Accepts the input for the question
    input_question = input("Enter a question: ")

    # Writes the input into a specified quiz file
    WriteFile.write_question(input_question,quiz_directory)

    # Accepts the input for the options and writes it into the specified quiz file at the same time
    WriteFile.write_option(quiz_directory)
        
    # Accepts the input for the correct answer
    input_answer = input("Enter the letter of the correct answer: ")
    
    # Writes the input for the correct answer
    WriteFile.write_correct(input_answer, quiz_directory)

    # Gives user the ability to exit or continue the loop
    user_option = input("Do you wish to continue? (any key to continue and // to exit): ")
    if user_option == "//":
        break
