import random
import os
import re
from datetime import date
from pathlib import Path

'''Python guesses answers to multiple choice tests taken today. Guesses are written to disk.'''

top_folder = Path.cwd()

# Go to tests
os.chdir(top_folder/'output'/'attempts')

# Create today's date string
today_dir = (str(date.today()).replace('-','_'))

# Make a folder dated today
try:
	os.mkdir(today_dir)
except FileExistsError:
	pass

# List absolute paths of today's tests
tests = []
for root, dirs, files in os.walk(top_folder/'output'/'test_papers'):
	for file in files:
		if today_dir in file:
			tests.append(Path(root,file))

for test in tests:
	with open(str(test),'r') as read_test:
		# Add test lines to list
		contents = [i for i in read_test.readlines()]

		# Define pattern to get the multiple choice line of the exam
		multiple_choice_pat = re.compile(r'^.+?(,).+?(?=\n)')

		# Add matches (four options per question) to a list
		matches = []
		for i in contents:
			if multiple_choice_pat.match(i):
				matches.append([x.strip() for x in i[:-1].split(',')])

		# Select a random answer from the questions' options
		guess_answers = [random.choice(i) for i in matches]

		# Move to attempts dir
		os.chdir(top_folder/'output'/'attempts'/today_dir)

		# Set doc title
		attempt_title = os.path.basename(test)[:-4] + '_atmpt'

		# Write guess answers to file
		with open(f'{attempt_title}.txt','w+') as atmpt_file:
			atmpt_file.write(f'{attempt_title}\n\n')
			for i in range(len(guess_answers)):
				atmpt_file.write(f'{i+1}. {guess_answers[i]} \n\n')


print('Take test complete')


