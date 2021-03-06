import random
import os
import time
import shutil
import gt_module_1
from pathlib import Path
from datetime import date

'''Create n number of multiple choice test and answer files. Organise files into folders on disk'''

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
   'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
   'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

def make_test_data(number):

   '''Accepts int 'number' and makes n data sets and string test titles'''

   # Set test title
   title = str(date.today()).replace('-','_') + '_' + 'test' + f'_{number:03}'

   # Make a list of dictionaries, containing the state, the correct ans for the capital and three incorrect ans
   quiz_data = []
   for i in capitals:
      data_group = {'State':i,'Capitals':[capitals[i]]}
      for i in range(3):
         wrong_ans = random.choice([capitals[i] for i in capitals if capitals[i] not in data_group['Capitals']])
         data_group['Capitals'].append(wrong_ans)
      quiz_data.append(data_group)

   # Randomise quiz_data order
   random.shuffle(quiz_data)

   # Shuffle the four options per question
   for i in quiz_data:
      random.shuffle(i['Capitals'])
      # Check for duplicates in answer
      if len(set(i['Capitals'])) < len(i['Capitals']):
         print('Duplicates in {0}'.format(i['Capitals']))

   # Return a string for test title, and a list of lists for question data
   return title, quiz_data

def make_test(title, data_list):
   
   '''Accepts str 'title' and list 'data list' generated by make_test_data()
   Converts data_list to a set of questions in a txt file'''

   with open(f'{title}.txt','w+') as test_file:

      # Write file name as first line of document
      test_file.write(f'{title}\n\n')

      # Iterate through data_list list, populating file with questions and answer options
      for i in range(len(data_list)):
         test_file.write('\n{0}. What is the capital of {1}?\n'.format(i+1, data_list[i]['State']))
         q_options = data_list[i]['Capitals']
         test_file.write(f'\n{", ".join(q_options)}\n\n\n')

def make_answer_sheet(title, data_list):
   
   '''Accepts str 'title' and list 'data_list' generated from make_test_data()
   Converts data_list to an answer file'''

   title = title + '_ans'

   with open(f'{title}.txt','w+') as ans_sheet:
      ans_sheet.write(f'{title}\n\n')
      for i in range(len(data_list)):
         ans_sheet.write('{0}. {1}\n\n'.format(i+1,capitals[data_list[i]['State']]))

def file_list(path):

   '''Accepts str 'path'. Returns a list of files contained in path'''

   f_list = []
   
   for i in os.listdir(path):
      if os.path.isfile(i):
         f_list.append(i)
      else:
         continue

   return(f_list)

def dated_folder(path):
   
   '''Moves all files in a loc (except .DS_Store files) into folders named the date the file was created'''
   
   # Make a list of files
   f_list = file_list(path)
   
   # print(f_list)

   for i in f_list:
      
      # Ignore .DS_Store
      if '.DS_Store' in i:
         print('Ignore DS files')
      
      else:
         # Define path of file in dir
         file_path = Path(path,i)

         # Get date created. NOTE - for Windows, use windows_date_created()
         fmtd_date_created = gt_module_1.GtFileStats.mac_date_created(file_path)

         # Make dated dir if it does not exist
         if fmtd_date_created in os.listdir():
            pass
         else:
            os.mkdir(fmtd_date_created)

         # Move file to dated folder
         shutil.move(str(file_path),str(Path(path,fmtd_date_created,i)))


'''Begin program'''

top_folder = Path.cwd()

# Make dirs unless they already exist
for directory in ['attempts','test_papers','answer_sheets']:
   try:
      os.makedirs(f'output/{directory}')
   except FileExistsError:
      pass

for i in range(1,2):
   # Generate test data
   data = make_test_data(i)

   os.chdir(top_folder/'output'/'test_papers')
   
   # Make test using data
   make_test(data[0],data[1])

   # Move any files to a date created folder
   dated_folder(top_folder/'output'/'test_papers')

   os.chdir(top_folder/'output'/'answer_sheets')
   
   # Make an answer sheet
   make_answer_sheet(data[0],data[1])

   # Move any files to a date created folder
   dated_folder(top_folder/'output'/'answer_sheets')

print('Make test complete')
