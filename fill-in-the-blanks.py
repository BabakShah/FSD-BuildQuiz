#=========================================================
#==== Fill-in-the-blanks Quiz ============================
#=========================================================

# For this project, I'll be building a Fill-in-the-Blanks quiz.
# It will prompt a user with a paragraph containing several blanks.
# The user should then fill in each blank appropriately to complete the paragraph.

#=========================================================
#==== Import Libraries ===================================
#=========================================================

import sys

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
	
	if user_level == "easy" or user_level == "medium" or user_level == "hard":
		print("Your selected difficulty level is: " + str(user_level))
		quiz_paragraph = quiz_paragraph_and_answers[user_level]['quiz_paragraph']
		quiz_answers = quiz_paragraph_and_answers[user_level]['quiz_answers']
		return (quiz_paragraph, quiz_answers)

#=========================================================
#==== Quiz paragraphs and answers object =================
#=========================================================

quiz_paragraph_and_answers = {
	'easy': {
		'quiz_paragraph' : '''When I first brought my cat ___1___ from the Humane Society she was a mangy, pitiful 
		___2___. She was so thin that you could count her vertebrae just by looking at her. Apparently ___4___ was 
		declawed by her previous owners, then abandoned or ___3___. Since she couldn't hunt, ___4___ nearly starved. 
		Not only that, but ___4___ had an abscess on one hip.''',
		'quiz_answers' : ["home","animal","lost","she"]
	},
	'medium': {
		'quiz_paragraph' : '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
		adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
		don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
		tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
		'quiz_answers' : ["function","argument","zero","array"]
	},
	'hard': {
		'quiz_paragraph' : '''The longer the ___1___ or the more complex the criteria, the longer students will take 
		to complete a thorough peer ___2___. If you assign shorter papers, you can easily devote a part of a ___3___
		to peer ___2___ or ask students to complete the peer ___2___ outside of ___3___. But if you assign long, 
		complex papers, consider breaking the peer ___2___ into several ___4___ sections. ''',
		'quiz_answers' : ["paper","review","class","short"]
	}
}

#=========================================================
#==== Get and check user answers==========================
#=========================================================
"""
	Behavior: This function gets and checks the user inputs (answers) 
	Inputs: The inputs are the quiz paragraph and answers, user answer and some counters
	Outputs: This function has no output
"""
def get_and_check_user_answers(user_answers, count_wrong,answer_number,answers_count,quiz_paragraph, quiz_answers):

	if (answer_number < 5):
		for count in range(answer_number,answers_count):
			user_answer = get_user_answer(count)
			check_user_answer(count_wrong,user_answer,user_answers,answer_number,quiz_paragraph, quiz_answers,count,answers_count)
	end_game()

#=========================================================
#==== Get user answers ===================================
#=========================================================
"""
	Behavior: This function gets the user inputs (answers) 
	Inputs: The inputs is the count variable
	Outputs: The output is the user answer
"""
def get_user_answer(count):
	user_answer = input("Fill in the blank #"+ str(count) + ": ")
	return user_answer

#=========================================================
#==== Check user answers ===================================
#=========================================================
"""
	Behavior: This function checks the user answer 
	Inputs: The inputs are the quiz paragraph and answers, user answer and some counters
	Outputs: This function has no output
"""
def check_user_answer(count_wrong,user_answer,user_answers,answer_number,quiz_paragraph, quiz_answers, count, answers_count):
			
	print("Your answer is: " + user_answer)
	print("Quiz answer is: " + quiz_answers[count-1])
	if quiz_answers[count-1] == user_answer:
		print("You're correct")
		user_answers.append(user_answer)
		complete_paragraph = complete_the_quiz_paragraph(count,quiz_paragraph, user_answer,user_answers)
		print("The paragraph is: " + str(complete_paragraph))
		answer_number += 1
		get_and_check_user_answers(user_answers, count_wrong,answer_number,answers_count,quiz_paragraph, quiz_answers)
				
	else:
		print("You're wrong. Try again...")
		count_wrong += 1
		get_and_check_user_answers(user_answers, count_wrong,answer_number,answers_count,quiz_paragraph, quiz_answers)

#=========================================================
#==== Complete the quiz paragraph ========================
#=========================================================
"""
	Behavior: This function completes the quiz paragraph with user answers 
	Inputs: The inputs are the quiz paragraph, the user answers and count variable
	Outputs: The output is the complete paragraph 
"""
def complete_the_quiz_paragraph(count,quiz_paragraph, user_answer, user_answers):

	blank_list = ['___1___','___2___','___3___','___4___']
	complete_paragraph = []
	quiz_paragraph_split = quiz_paragraph.split()
	
	for word in quiz_paragraph_split:
		blank = word_is_blank_or_not(count,word, blank_list)
		if blank != None:
			if blank == "___1___":
				word = word.replace(blank,user_answers[0])
				complete_paragraph.append(word)
			elif blank == "___2___":
				word = word.replace(blank,user_answers[1])
				complete_paragraph.append(word)
			elif blank == "___3___":
				word = word.replace(blank,user_answers[2])
				complete_paragraph.append(word)
			else:
				word = word.replace(blank,user_answers[3])
				complete_paragraph.append(word)
		else:
			complete_paragraph.append(word)
		
	complete_paragraph = " ".join(complete_paragraph)

	return complete_paragraph

#=========================================================
#==== Check if the word is blank or not ==================
#=========================================================
"""
	Behavior: This function checks to see whether the word in the original paragraph is blank or not 
	Inputs: This inputs are the paragraph word and the list of blanks
	Outputs: The output is either each blank item or none depending on the word 
"""
def word_is_blank_or_not(count,word, blank_list):

	for ctr,blank in enumerate(blank_list):
		if(ctr < count):
			if blank in word:
				ctr+=1
				return blank

	return None

#=========================================================
#==== End quiz function ==================================
#=========================================================

def end_game():
	print("CONGRATUALTIONS!!! YOU WON!!!")
	sys.exit()

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
answer_number = 1
answers_count = 5
count_wrong = 0
user_answers = []
user_answer = get_and_check_user_answers(user_answers, count_wrong,answer_number,answers_count,quiz_paragraph, quiz_answers)
