#=========================================================
#==== Fill-in-the-blanks Quiz ============================
#==== Version: Answer one at a time ======================
#=========================================================

# For this project, I'll be building a Fill-in-the-Blanks quiz.
# It will prompt a user with a paragraph containing several blanks.
# The user should then fill in each blank appropriately to complete the paragraph.

#=========================================================
#==== Select difficulty level ============================
#=========================================================
"""
	Behavior: This function selects the difficulty level of the game
	Inputs: This function doesn't take any inputs
	Outputs: The outputs are the quiz paragraph and quiz answers
"""
def select_difficulty_level():

	user_level = input("Please select game level of difficulty: (easy, medium, hard) : ")
	print("Your selected difficulty level is: " + str(user_level))

	if user_level == "easy":
		quiz_paragraph, quiz_answers = update_easy_quiz_paragraph_and_answers()
	elif user_level == "medium":
		quiz_paragraph, quiz_answers = update_medium_quiz_paragraph_and_answers()
	elif user_level == "hard":
		quiz_paragraph, quiz_answers = update_hard_quiz_paragraph_and_answers()
	else:
		quiz_paragraph = " "
		quiz_answers = " "
		print("Not a valid selection. Please try again.")
		select_difficulty_level()

	return (quiz_paragraph, quiz_answers)

#=========================================================
#==== Update easy quiz paragraph and answers =============
#=========================================================
"""
	Behavior: This function updates the easy quiz paragraph 
			  and answers based on the difficulty level 
	Inputs: This function doesn't take any inputs
	Outputs: The outputs are the quiz paragraph and quiz answers
"""
def update_easy_quiz_paragraph_and_answers():

	quiz_paragraph = '''When I first brought my cat ___1___ from the Humane Society she was a mangy, pitiful 
	___2___. She was so thin that you could count her vertebrae just by looking at her. Apparently ___4___ was 
	declawed by her previous owners, then abandoned or ___3___. Since she couldn't hunt, ___4___ nearly starved. 
	Not only that, but ___4___ had an abscess on one hip.'''
	quiz_answers = ["home","animal","lost","she"]

	return (quiz_paragraph, quiz_answers)

#=========================================================
#==== Update medium quiz paragraph and answers ===========
#=========================================================
"""
	Behavior: This function updates the medium quiz paragraph 
			  and answers based on the difficulty level 
	Inputs: This function doesn't take any inputs
	Outputs: The outputs are the quiz paragraph and quiz answers
"""
def update_medium_quiz_paragraph_and_answers():

	quiz_paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
	adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
	don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
	tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
	quiz_answers = ["function","argument","zero","array"]

	return (quiz_paragraph, quiz_answers)

#=========================================================
#==== Update hard quiz paragraph and answers =============
#=========================================================
"""
	Behavior: This function updates the hard quiz paragraph 
			  and answers based on the difficulty level 
	Inputs: This function doesn't take any inputs
	Outputs: The outputs are the quiz paragraph and quiz answers
"""
def update_hard_quiz_paragraph_and_answers():

	quiz_paragraph = '''The longer the ___1___ or the more complex the criteria, the longer students will take 
	to complete a thorough peer ___2___. If you assign shorter papers, you can easily devote a part of a ___3___
	to peer ___2___ or ask students to complete the peer ___2___ outside of ___3___. But if you assign long, 
	complex papers, consider breaking the peer ___2___ into several ___4___ sections. '''
	quiz_answers = ["paper","review","class","short"]

	return (quiz_paragraph, quiz_answers)

#=========================================================
#==== Get user answers ===================================
#=========================================================
"""
	Behavior: This function gets the user inputs (answers) 
	Inputs: The inputs are the quiz paragraph and answers
	Outputs: The output is the complete paragraph
"""
def get_user_answers(quiz_paragraph, quiz_answers):

	number_of_blanks = 4
	for blank in range(0,number_of_blanks):
		user_answer = input("Please fill in the ___" + str(blank + 1) + "___ blank: ")
		print("Your answer is: " + str(user_answer))
		complete_paragraph = complete_the_quiz_paragraph(quiz_paragraph, user_answer, quiz_answers)
	
	return complete_paragraph

#=========================================================
#==== Complete the quiz paragraph ========================
#=========================================================
"""
	Behavior: This function completes the quiz paragraph 
			  with user answers 
	Inputs: The inputs are the quiz paragraph, the user 
			and quiz answers
	Outputs: The output is the complete paragraph 
"""
def complete_the_quiz_paragraph(quiz_paragraph, user_answer, quiz_answers):

	blank_list = ['___1___','___2___','___3___','___4___']
	complete_paragraph = []
	quiz_paragraph_split = quiz_paragraph.split()
	updated_quiz_paragraph = quiz_paragraph

	for word in quiz_paragraph_split:
		blank = word_is_blank_or_not(word, blank_list)
		if blank != None:
			quiz_answer = blank_to_quiz_answer(blank, quiz_answers)
			word = word.replace(blank,user_answer)
			if user_answer == quiz_answer:
				print("Your answer is CORRECT!!!")
				print(updated_quiz_paragraph.replace(blank,user_answer))
			complete_paragraph.append(word)
		else:
			complete_paragraph.append(word)
		
		# print(complete_paragraph)
	complete_paragraph = " ".join(complete_paragraph)

	return complete_paragraph

# def replace_blank_with_user_answer:

#=========================================================
#==== Blank to quiz answer mapping =======================
#=========================================================
"""
	Behavior: This function maps the blank number with the
			  correspinding quiz answer
	Inputs: The inputs are the blank number and the quiz 
			answers
	Outputs: The output is either quiz answers or nothing 
"""
def blank_to_quiz_answer(blank, quiz_answers):
    mapper = {
        "___1___": quiz_answers[0],
        "___2___": quiz_answers[1],
        "___3___": quiz_answers[2],
        "___4___": quiz_answers[3],
    }

    return mapper.get(blank, "nothing")

#=========================================================
#==== Check if the word is blank or not ==================
#=========================================================
"""
	Behavior: This function checks to see whether the word
			  in the original paragraph is blank or not 
	Inputs: This inputs are the paragraph word and the list
			of blanks
	Outputs: The output is either each blank item or none 
			 depending on the word 
"""
def word_is_blank_or_not(word, blank_list):
	
	for blank in blank_list:
		if blank in word:
			return blank
	return None

#=========================================================
#==== Quiz functions pipeline ============================
#=========================================================

def pipeline(quiz_paragraph, quiz_answers):

	complete_paragraph = get_user_answers(quiz_paragraph, quiz_answers)
	# complete_paragraph = complete_the_quiz_paragraph(quiz_paragraph, user_answers)
	print("The complete paragraph is: " + str(complete_paragraph))

#=========================================================
#==== Start the Quiz =====================================
#=========================================================
"""
	We start the quiz by selecting the difficulty level and then
	displaying the quiz paragraph and answers. After that we go
	through the quiz pipeline (NOTE: quiz answers are displayed 
	only for testing purposes. Please comment or remove the line 
	before playing the game)
"""
quiz_paragraph, quiz_answers = select_difficulty_level()
print("Quiz paragraph is: " + str(quiz_paragraph))
print("Quiz answers are: " + str(quiz_answers))
pipeline(quiz_paragraph, quiz_answers)

