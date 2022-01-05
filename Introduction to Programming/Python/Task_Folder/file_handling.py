# Python File Handling

import math 
import statistics as stat
import os


"""
	1.) Open and read the file q1_text.txt. Print out the entire
	contents of the file.
"""
print("\nQ 1.")

with open("q1_text.txt", mode="r", encoding="utf-8") as f1:
    
    all_text = f1.read()
    
print(all_text)



"""
	2.) Open and read the file q2_text.txt. Print out only the
	first and last line in this file.
"""
print("\nQ 2.")

with open("q2_text.txt", mode="r", encoding="utf-8") as f2:
    
    all_text = f2.read()
    list_text = all_text.split("\n")

print(list_text[0])
print(list_text[-1]) 


"""
	3.) Open up file q3_text.txt and at the end of it write a
	new line "- From <your name here>". Make sure not to delete 
	any of the text inside of it.
"""
print("\nQ 3.")

# Write Code here
with open("q3_text.txt", mode="a", encoding="utf-8") as f3:  
      
    f3.write('\n- From Angelo')
    
with open("q3_text.txt", mode="r", encoding="utf-8") as f3:   
     
	all_text = f3.read()
 
print(all_text)

def restore_q3():
	with open('q3_text.txt', mode='w', encoding='utf-8') as f3:
		f3.write("""Dear Santa,
This year I would like a bike
because my last one was stolen
on Granville Island!""")
restore_q3()
#############



"""
	4.) Open up file q4_text.txt and print the average of all
	the numbers that appear in the file. The numbers are all 
	separated by a single space " " each
"""
print("\nQ 4.")

with open("q4_text.txt", mode="r", encoding="utf-8") as f4:
    
    all_text = f4.read()
    list_text = all_text.split(" ")
    new_list = []
    for items in list_text:
        items = int(items)
        new_list.append(items)
    average = sum(new_list) / len(new_list)
    ave = stat.mean(new_list)
print(average)
print(ave)


"""
	5.) Create a new file called q5_answer.txt and write
	2 lines in it reading "I made this with Python" and
	"A new file gets created if no file in the directory
	has the same name as it!". After this is created, print
	the line "q5_answer is made"
"""
print("\nQ 5.")

# Delete file if it exists this is for question 5
if os.path.exists("q5_answer.txt"):
  os.remove("q5_answer.txt")
else:
  print("The file does not exist")

with open("q5_answer.txt", mode="x", encoding="utf-8"):
    with open("q5_answer.txt", mode="w", encoding="utf-8") as f5:
    	f5.write('I made this with python' + '\n' + 'A new file gets created if no file in the directory has the same name as it!')
with open("q5_answer.txt", mode="r", encoding="utf-8") as f5:
    all_text = f5.read()
    
print(all_text)
print("q5_answer is made")



"""
    6.) q6_tsv.tsv is a tab separated values file. It
    contains words separated by tabs \t on a single line. 
    Count how many words there are in the file and print it. 
    Also, to the end of the file add the following "there are
    X words in this file".

"""
print("\nQ 6.")

with open("q6_tsv.tsv", mode="r+", encoding="utf-8") as f6:
    
    all_text = f6.read()
    list_text = all_text.split('\t')
    count = len(list_text)
    f6.write(f"there are {count} words in this file.")
    


def restore_q6():
	with open('q6_tsv.tsv', mode='w', encoding='utf-8') as f6:
		f6.write('cat\tbat\that\tmat\tfat\tchat')
# restore_q6()
#############



"""
	7.) Print how many times the word "Canada" appears in 
	the q7_text.txt file. Replace all appearances of the word 
	Canada in the file with the word "CENSORED". You must 
	overwrite the file when doing this.
"""
print("\nQ 7.")

def restore_q7():
	with open('q7_text.txt', mode='w', encoding='utf-8') as f6:
		f6.write("""Canada is a country in North America. 
Canada's capital is Ottawa, and its three largest 
metropolitan areas are Toronto, Montreal, and Vancouver.
Indigenous peoples have continuously inhabited what is 
now Canada for thousands of years.
In 1867, with the union of three British North American 
colonies through Confederation, Canada was formed as a 
federal dominion of four provinces.""")
restore_q7()

# with open("q7_text.txt", mode="r", encoding="utf-8") as f7:
#     all_text = f7.read()
#     list_text = all_text.replace(".","").replace(",","").split()
#     count = 0 
#     for items in list_text:
#         if "Canada" in items:
#         	count += 1
#     print(count)
    
#     with open("q7_text.txt", mode="w", encoding="utf-8") as f7a:
#         replace_text = all_text.replace("Canada", "CENSORED")
#         f7a.write(replace_text)
#         print("Below is a printed version where 'Canada' is replaced with 'CENSORED'")
#         print(replace_text)

with open("q7_text.txt", mode="r+", encoding="utf-8") as f7:
    f7_text = f7.read()
    can_num = f7_text.count("Canada")
    print(f"Canada appears {can_num} times.")
    
    censored_f7_text = f7_text.replace("Canada", "CENSORED")
    f7.seek(0)
    f7.write(censored_f7_text)
		
    

#############


