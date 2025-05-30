import read_quiz
import extract_and_repack
import shuffle
import display_question
import score_count

# Path of the quiz file
quiz_directory = r"recall_quiz_generator/quiz_creator/quiz_file.txt" 

class Item:

    def __init__(self, question, option_a, option_b, option_c, option_d, correct_answer):
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_answer = correct_answer

# UI ----------------------
# Initialization
quiz_lines_list = read_quiz(quiz_directory)
quiz_items_dict = extract_and_repack(quiz_lines_list)  # List of questions/item

# Header ------------------
print(f"""Welcome to the recall quiz app
""")

# Program Loop ------------
while True:

    # Initialize randomize_index. Stores a random sequence of numbers based on the range of the given dictionary.
    randomized_index = shuffle(1, len(quiz_items_dict))

    # Initialize quiz_result_summary dictionary. Records the finished items along with the results.
    quiz_result_summary = {}

    # Asks the user for permission to start the test
    input_start_option = input("Start the test? (any key to start, x to exit): ")

    if input_start_option.lower() == "x":  
        break
    else:
        # Pick a random question from the question dictionary (quiz_item_dict)
        for index in randomized_index:

            # Print the question in a question-options format
            print(display_question(quiz_items_dict,index)) 

            # Request for an answer 
            input_answer = input("Answer: ")  

            # Tells whether the input answer is correct (True) or incorrect (False)
            answer_state = None 

            # If the input answer is the same as the correct answer
            if f"A: {input_answer.lower()}" == quiz_items_dict[index].correct_answer:  
                answer_state = True  # Mark the answer as True, indicating that the answer is correct

            # If it is not
            else:
                answer_state = False  # Mark as false, indicating that it is incorrect

            # Record the answer in a dictionary. Use the question's index as the key and it's state as the value
            quiz_result_summary[index] = answer_state

    # Print the score over the total number of items
    print(f" Total Score: {score_count(quiz_result_summary)}/{len(quiz_items_dict)}")