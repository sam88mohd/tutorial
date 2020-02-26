#! python3
# randomQuizGenerator.py- Create quizzes with questions and answers in
# random order, along with the answer keys.

import random

# The quiz data. Keys are state and values are theirs capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 
'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 
'Wyoming': 'Cheyenne' }

# Generate 35 quiz files.
for quizNum in range(35):

	# Create the quiz and answer key files
	quizFile = open('capitalquiz{}'.format(quizNum + 1), 'w')
	answerKeyFile = open('capitalquiz_answer{}'.format(quizNum + 1), 'w')

	# Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' '*20) + 'State Capital Quiz (Form {})'.format(quizNum + 1))
	quizFile.write('\n\n') 

	# Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)

	# Loop through all 50 states, making a question for each.
	for questionNum in range(50):

		# Get right and wrong answers.
		correctAnswer = capitals[states[questionNum]]
		wrongAnswer = list(capitals.values())
		del wrongAnswer[wrongAnswer.index(correctAnswer)]
		wrongAnswer = random.sample(wrongAnswer, 3)
		answerOptions = wrongAnswer + [correctAnswer]
		random.shuffle(answerOptions)

		# Write the question and answer option to the quiz file
		quizFile.write('{}. What is the capital of {}? \n'.format(questionNum + 1, states[questionNum]))
		for i in range(4):
			quizFile.write('    {}. {}\n'.format('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		# Write the answer key to a file
		answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()
