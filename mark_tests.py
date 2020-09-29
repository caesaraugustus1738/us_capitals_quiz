import os
import re
import traceback
from pathlib import Path

'''
# Create score folder
# Make a score csv
# Go to attempts
# Mark attempts
# Add scores to a csv
'''

# Define folder this script is in
script_folder = Path(os.path.dirname(__file__))

print(script_folder)

# Move to output dir
os.chdir(script_folder/'output')

# Make scores dir
try:
    os.mkdir('scores')
except FileExistsError:
    pass

# Move to scores dir
os.chdir('scores')

# Create scores CSV
try:
    with open('scores.csv','w') as score_sheet:
        score_sheet.write('score_sheet\n')
        score_sheet.write('Test, Score \n')
except FileExistsError:
    pass

os.chdir(script_folder)


for root, dirs, files in os.walk(script_folder/'output'/'attempts'):
    for file in files:
        # print('Progress check')
        if '.DS_Store' in file:
            pass
        else:
            try:
                ans_file_name = file.replace('atmpt','ans')

                # Open answer sheet for given attempt file 
                with open(script_folder/'output'/'answer_sheets'/f'{file[:10]}'/f'{ans_file_name}','r') as ans_sheet:
                    print(f'Answer sheet found for {file}!')
                    
                    # Define pattern - digits at start of line until a period
                    line_pattern = re.compile(r'^\d+[.]')

                    # Define pattern - capital letter until end of line
                    ans_pattern = re.compile(r'[A-Z].+$')

                    # Get list of answers from answer paper
                    correct_answers = {}
                    for line in ans_sheet.readlines():
                        if line_pattern.search(line):
                            correct_answers[int(line_pattern.search(line).group()[:-1])] = ans_pattern.search(line).group()


                # Open attempt file
                with open(script_folder/'output'/'attempts'/f'{file[:10]}'/file,'r') as atmpt_file:
                
                    # Get list of answers from atmpt paper
                    atmpt_answers = {}
                    for line in atmpt_file.readlines():
                        if line_pattern.search(line):
                            atmpt_answers[int(line_pattern.search(line).group()[:-1])] = ans_pattern.search(line).group().rstrip()

                
                # Add up score
                score = 0

                for i in range(len(correct_answers)):
                    if atmpt_answers[i+1] == correct_answers[i+1]:
                        score += 1

                print('Progress update')

                # Write score to file
                with open(script_folder/'output'/'scores'/'scores.csv','a') as score_file:
                    test_file_name = file.replace('_atmpt','')
                    score_file.write(f'{test_file_name},{score}\n')


            except FileNotFoundError:
                print(f'Answer sheet not found for {file}')
                # print(traceback.format_exc())
                continue

print('Mark tests complete')

