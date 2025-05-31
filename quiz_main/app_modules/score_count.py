class ScoreCount:

    def score_count(result_summary):
        """
        Evaluates the amount of correct answer from a result summary
        Accepts the result summary dictionary of a quiz
        Returns the number of correct answers in a result summary
        """
        true_count = 0
        for key in result_summary:  # Loop through results of the summary
            if result_summary[key] == True:  # If an item has a value of True
                true_count += 1  # Increment the counter by one
        return true_count 
