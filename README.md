# us_capitals_quiz
Get Python to create a multiple choice test, guess the answers, mark the attempt, and write the score to a CSV.

make_test.py utilises a method defined in my own module gt_module_1.py. I did this to understand how modules, classes and methods work. NOTE - this project is designed to work on OSX or Windows. This version is configured to OSX. To make it work on Windows, in make_test.py you must change the GtFileStats method from Mac to Windows. Both methods are contained in gt_module_1.py.

run_cycle.py is a script which runs the scripts one by one from the terminal. NOTE - this is just for Mac. I haven't written a Windows equivalent yet. BUG - currently the scores CSV doesn't populate any scores when run_cycle.py executes the mark_tests.py script. If I run the scripts by hand in Sublime, it works. I need to solve this issue.

The objectives on this project are
- Learn how to wield multiple scripts in one project
- Develop automation skills
- Develop skills in file/folder creation and navigation
- Use my own module and method
