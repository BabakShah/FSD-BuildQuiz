# For this project, I'll be building a Fill-in-the-Blanks quiz.
# It will prompt a user with a paragraph containing several blanks.
# The user should then fill in each blank appropriately to complete the paragraph.

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!



# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# blanks = ['___1___','___2___','___3___','___4___']
# correct_answers = ["Function","Argument","Zero","Array"]
# user_answers = []
# blanks_indices = []

# paragraph_split = paragraph.split()
# print(str(paragraph_split))



#=========================================================
#==== Build up the complete sentence =====================
#=========================================================

# def create_complete_sentence(user_answers,paragraph_split):
# 	complete_paragraph = []
	
# 	for part in paragraph_split:
# 		answer = get_blanks_indices(paragraph_split)
# 		# print(answer)
# 		if answer != None:
# 			print("inside if condition")
# 			part = part.replace(answer,user_answers[0])
# 			print(part)
# 			complete_paragraph.append(part)

# 		else:
# 			complete_paragraph.append(part)
# 	return complete_paragraph

#=========================================================
#==== Get the indexes of blanks ==========================
#=========================================================

# blanks_indices = get_blanks_indices(paragraph_split)
# for blank in range(0,4):
# 	word = input("Fill in the blank #"+ str(blank+1) + ": ")
# 	user_answers.append(word)
# print("Your answers are: ")
# print(user_answers)

# if user_answers == correct_answers:
# 	print("Answers are correct!")
# 	print("The full sentence is:")
# else:
# 	print("One or more answers are wrong ... please try again")

# complete_paragraph = create_complete_sentence(user_answers,paragraph_split)
# print(complete_paragraph)
# print(paragraph_split)
# for index, part in enumerate(paragraph_split):
# 	# print("inside the for loop")
# 	if index in blanks_indices:
		
		# part = part.replace(part, "user_answers[index]")
	# print(paragraph_split)

#=========================================================
#==== Select difficulty level ============================
#=========================================================

def select_difficulty_level():

	user_level = input("Please select game level of difficulty: (easy, medium, hard) : ")
	print("Your selected difficulty level is: " + str(user_level))

	if user_level == "easy":
		quiz_paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
		adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
		don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
		tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
		quiz_answers = ["a","s","d","f"]

	elif user_level == "medium":
		quiz_paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
		adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
		don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
		tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
		quiz_answers = ["Function","Argument","Zero","Array"]

	elif user_level == "hard":
		quiz_paragraph = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
		adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
		don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
		tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
		quiz_answers = ["Function","Argument","Zero","Array"]

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

