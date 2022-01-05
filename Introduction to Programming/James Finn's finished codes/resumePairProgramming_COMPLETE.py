# Python File Handling
"""
Write code that will take the resume.txt file and replace
all words surrounded by angle brackets <> with values 
to yourselves. This new resume you create should be outputted
to a new file called new-resume.txt

<USERNAME> and <JOBTITLE> values can be hardcoded 
<CURRENTYEAR> should be the current year and needs to programmed
	so that in 2022 it will read 2022 without you changing it
<YEARS> should be programatically generated so that in 2 years
	time it update to account for you being more experienced

At the end of the file I want to see a list of programming 
languages on new lines with a leading hyphen like so
- JavaScript
- Python
These languages should be inputted by asking the user for input.
Keeping asking the user to add languages until they type the
word "STOP" at which point the program should end and produce
the new file

"""
import datetime
now = datetime.datetime.now()


with open('resume.txt', mode='r', encoding='utf-8') as f:
	resume_txt = f.read()
	resume_txt = resume_txt.replace('<USERNAME>', 'James Finn')
	resume_txt = resume_txt.replace('<CURRENTYEAR>', str(now.year))
	resume_txt = resume_txt.replace('<JOBTITLE>', 'Software Engineer')

	years_experience = f'{now.year - 2013}'
	resume_txt = resume_txt.replace('<YEARS>', years_experience)

	programming_list = ['']
	user_programming = ''
	while user_programming != 'STOP':
		print('Type "STOP" to end.')
		user_programming = input('Add Programming Language: ')
		programming_list.append(user_programming)

	resume_txt += '\n- '.join(programming_list[:-1])
	

with open('new-resume.txt', mode='w', encoding='utf-8') as newFile:
	newFile.write(resume_txt)
	print('Creating new-resume.txt file')



def restore_resume():
	with open('resume.txt', mode='w', encoding='utf-8') as f:
		f.write("""<USERNAME> Resume <CURRENTYEAR>
<JOBTITLE>
=====================================================

I am an enthusiastic and hard-working programmer that 
has recently graduated from the VCC Computer Systems
Technology diploma program. I have <YEARS> years experience 
writing code.

Programming Languages""")

########################
# Call this function
# to restore resume.txt
# to original form
# ######################
# restore_resume()
