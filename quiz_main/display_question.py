def display_question(question_dict, question_index):
    """
    Displays the item in a questionnaire format.
    Accepts the dictionary from where the item belongs(question_dict) and the key that corresponds to that item
    Returns the item in a question-options format
    """
    return f"""
{question_dict[question_index].question}
a). {question_dict[question_index].option_a}
b). {question_dict[question_index].option_b}
c). {question_dict[question_index].option_c}
d). {question_dict[question_index].option_d}
"""
