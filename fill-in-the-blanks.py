# For this project, I'll be building a Fill-in-the-Blanks quiz.
# It will prompt a user with a paragraph containing several blanks.
# The user should then fill in each blank appropriately to complete the paragraph.

#=========================================================
#==== Select difficulty level ============================
#=========================================================

def select_difficulty_level():

	user_level = input("Please select game level of difficulty: (easy, medium, hard) : ")
	print("Your selected difficulty level is: " + str(user_level))

	if user_level == "easy":

		quiz_paragraph = '''When I first brought my cat ___1___ from the Humane Society she was a mangy, pitiful 
		___2___. She was so thin that you could count her vertebrae just by looking at her. Apparently ___4___ was 
		declawed by her previous owners, then abandoned or ___3___. Since she couldn't hunt, ___4___ nearly starved. 
		Not only that, but ___4___ had an abscess on one hip.'''

		quiz_answers = ["home","animal","lost","she"]

	elif user_level == "medium":

		quiz_paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
		adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
		don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
		tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
		
		quiz_answers = ["function","argument","zero","array"]

	elif user_level == "hard":

		quiz_paragraph = '''The longer the ___1___ or the more complex the criteria, the longer students will take 
		to complete a thorough peer ___2___. If you assign shorter papers, you can easily devote a part of a ___3___
		 to peer ___2___ or ask students to complete the peer ___2___ outside of ___3___. But if you assign long, 
		 complex papers, consider breaking the peer ___2___ into several ___4___ sections. '''
		
		quiz_answers = ["paper","review","class","short"]

	else:
		print("Not a valid selection. Please try again.")
		select_difficulty_level()

	print("Quiz paragraph is: " + str(quiz_paragraph))
	print("Quiz answers are: " + str(quiz_answers))
	return (quiz_paragraph, quiz_answers)

#=========================================================
#==== Get user answers ===================================
#=========================================================

def get_user_answers():

	user_answers = []
	for blank in range(0,4):
		user_answer = input("Fill in the blank #"+ str(blank + 1) + ": ")
		user_answers.append(user_answer)
	print("Your answers are: " + str(user_answers))
	return user_answers

#=========================================================
#==== Check user answers ===================================
#=========================================================

def check_user_answers(user_answers, quiz_answers):

	if user_answers == quiz_answers:
		print("You win!!! Your answers are correct!")
	else:
		print("One or more answers are wrong ... please try again")
		pipeline(quiz_paragraph, quiz_answers)

#=========================================================
#==== Complete the quiz paragraph ========================
#=========================================================

def complete_the_quiz_paragraph(quiz_paragraph, user_answers):

	blank_list = ['___1___','___2___','___3___','___4___']
	complete_paragraph = []
	quiz_paragraph_split = quiz_paragraph.split()
	for word in quiz_paragraph_split:
		blank = word_is_blank_or_not(word, blank_list)
		if blank != None:
			answer = blank_to_answer(blank, user_answers)
			word = word.replace(blank,answer)
			# print("word is: " + word)
			# print("complete par is: " + str(complete_paragraph))
			complete_paragraph.append(word)
		else:
			complete_paragraph.append(word)
	complete_paragraph = " ".join(complete_paragraph)
	return complete_paragraph

#=========================================================
#==== Blank to answer mapping ============================
#=========================================================

def blank_to_answer(blank, user_answers):
    mapper = {
        "___1___": user_answers[0],
        "___2___": user_answers[1],
        "___3___": user_answers[2],
        "___4___": user_answers[3],
    }
    return mapper.get(blank, "nothing")

#=========================================================
#==== Check if the word is blank or not ==================
#=========================================================

def word_is_blank_or_not(word, blank_list):
	
	for blank in blank_list:
		if blank in word:
			print("blank is: " + str(blank))
			return blank
	return None

#=========================================================
#==== Quiz pipeline ======================================
#=========================================================

def pipeline(quiz_paragraph, quiz_answers):
	user_answers = get_user_answers()
	# check_user_answers(user_answers, quiz_answers)
	complete_paragraph = complete_the_quiz_paragraph(quiz_paragraph, user_answers)
	print("The complete paragraph is: " + str(complete_paragraph))

#=========================================================
#==== Start the Quiz =====================================
#=========================================================

quiz_paragraph, quiz_answers = select_difficulty_level()
pipeline(quiz_paragraph, quiz_answers)

