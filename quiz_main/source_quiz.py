# Path of the question file
quiz_directory = r"recall_quiz_generator/quiz_creator/quiz_file.txt" 

class Item:

    def __init__(self, question, option_a, option_b, option_c, option_d, correct_answer):
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_answer = correct_answer
