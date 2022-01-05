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





# In case you accidentally modify the original file
# call this function to restore it to its former self
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
