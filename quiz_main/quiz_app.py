from app_modules.read_quiz import ReadQuiz
from app_modules.extract_and_repack import ExtractRepack
from app_modules.shuffle import Shuffle
from app_modules.display_question import DisplayQuestion
from app_modules.score_count import ScoreCount

# Path of the quiz file
quiz_directory = r"quiz_main/quiz_creator/quiz_file/quiz_file.txt" 

# Creates a list of all the lines from the quiz_file text file
quiz_lines_list = ReadQuiz.read_quiz(quiz_directory)

# Extracts those lines and encapsulates them into objects as "items".
# It then returns a dictionary that contains those items
quiz_items_dict = ExtractRepack.extract_and_repack(quiz_lines_list)  

# Header ------------------
print(f"""Welcome to the recall quiz app
""")

# Program Loop ------------
while True:

    # Initialize randomize_index. Stores a random sequence of numbers based on the range of the given dictionary.
    randomized_index = Shuffle.shuffle(1, len(quiz_items_dict))

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
            print(DisplayQuestion.display_question(quiz_items_dict,index)) 

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
    print(f" Total Score: {ScoreCount.score_count(quiz_result_summary)}/{len(quiz_items_dict)}")