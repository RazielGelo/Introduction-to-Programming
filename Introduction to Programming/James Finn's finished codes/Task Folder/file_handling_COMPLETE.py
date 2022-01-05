# Python File Handling

#===========================
#===========================
# Make sure to include files
# in same folder as this
# ==========================
# ==========================

"""
	1.) Open and read the file q1_text.txt. Print out the entire
	contents of the file.
"""
print("\nQ 1.")
with open('q1_text.txt', mode='r', encoding='utf-8') as f1:
	print(f1.read())



"""
	2.) Open and read the file q2_text.txt. Print out only the
	first and last line in this file.
"""
print("\nQ 2.")

with open('q2_text.txt', mode='r', encoding='utf-8') as f2:
	q2_list = f2.read().split('\n')
	print(q2_list[0])
	print(q2_list[-1])



"""
	3.) Open up file q3_text.txt and at the end of it write a
	new line "- From <your name here>". Make sure not to delete 
	any of the text inside of it.
"""
print("\nQ 3.")

with open('q3_text.txt', mode='a', encoding='utf-8') as f3:
	pass
	f3.write('\n- From James Finn')


def restore_q3():
	with open('q3_text.txt', mode='w', encoding='utf-8') as f3:
		f3.write("""Dear Santa,
This year I would like a bike
because my last one was stolen
on Granville Island!""")
#############
#restore_q3()
#############



"""
	4.) Open up file q4_text.txt and print the average of all
	the numbers that appear in the file. The numbers are all 
	separated by a single space " " each
"""
print("\nQ 4.")

with open('q4_text.txt', mode='r', encoding='utf-8') as f4:
	num_list = f4.read().split()
	for i in range(len(num_list)):
		num_list[i] = int(num_list[i])
	average = sum(num_list) / len(num_list)
	print(average)



"""
	5.) Create a new file called q5_answer.txt and write
	2 lines in it reading "I made this with Python" and
	"A new file gets created if no file in the directory
	has the same name as it!". After this is created, print
	the line "q5_answer is made"
"""
print("\nQ 5.")

with open('q5_answer.txt', mode='w', encoding='utf-8') as f5:
	f5.write('I made this with Python\nA new file gets created if no file in the directory has the same name as it!')



"""
    6.) q6_tsv.tsv is a tab separated values file. It
    contains words separated by tabs \t on a single line. 
    Count how many words there are in the file and print it. 
    Also, to the end of the file add the following "there are
    X words in this file".

"""
print("\nQ 6.")

with open('q6_tsv.tsv', mode='r+', encoding='utf-8') as f6:
	tab_vals = f6.read().split('\t')
	print(len(tab_vals))
	f6.write(f'There are {len(tab_vals)} in this file')

def restore_q6():
	with open('q6_tsv.tsv', mode='w', encoding='utf-8') as f6:
		f6.write('cat\tbat\that\tmat\tfat\tchat')
#############
#restore_q6()
#############



"""
	7.) Print how many times the word "Canada" appears in 
	the q7_text.txt file. Replace all appearances of the word 
	Canada in the file with the word "CENSORED". You must 
	overwrite the file when doing this.
"""
print("\nQ 7.")

with open('q7_text.txt', mode='r+', encoding='utf-8') as f7:
	f7_text = f7.read()
	can_num = f7_text.count('Canada')
	print(f'Canada appears {can_num}')

	censored_f7_text = f7_text.replace('Canada', 'CENSORED')
	f7.seek(0)
	f7.write(censored_f7_text)

def restore_q7():
	with open('q7_text.txt', mode='w', encoding='utf-8') as f7:
		f7.write("""Canada is a country in North America. 
Canada's capital is Ottawa, and its three largest 
metropolitan areas are Toronto, Montreal, and Vancouver.
Indigenous peoples have continuously inhabited what is 
now Canada for thousands of years.
In 1867, with the union of three British North American 
colonies through Confederation, Canada was formed as a 
federal dominion of four provinces.""")
#############
#restore_q7()
#############

def update_exam_results(file):
    with open(file, mode="r+", encoding="utf-8") as active_file:
        text_string  = active_file.read()
        text_list = text_string.split("\n")
        col = text_list[0].replace(text_list[0],"Mark, Bobby, Susan, Mary, Total, Average")
        row_1 = text_list[1].split(", ")
        row_2 = text_list[2].split(", ")
        row_3 = text_list[3].split(", ")
        
        new_row_1 = []
        new_row_2 = []
        new_row_3 = []  
              
        for item in row_1:
            item = int(item)
            new_row_1.append(item)
            
        for item in row_2:
            item = int(item)
            new_row_2.append(item)
            
        for item in row_3:
            item = int(item)
            new_row_3.append(item)
            
        append_set_1 = [float(sum(new_row_1)), float(sum(new_row_1) / 4)]
        new_row_1.extend(append_set_1)
        
        append_set_2 = [float(sum(new_row_2)), float(sum(new_row_2) / 4)]
        new_row_2.extend(append_set_2)
        
        append_set_3 = [float(sum(new_row_3)), float(sum(new_row_3) / 4)]
        new_row_3.extend(append_set_3)
        
        new_row_1 = ", ".join(map(str, new_row_1))
        new_row_2 = ", ".join(map(str, new_row_2))
        new_row_3 = ", ".join(map(str, new_row_3))
        
        active_file.seek(0)
        active_file.write(f"{col}\n{new_row_1}\n{new_row_2}\n{new_row_3}")          

update_exam_results("exam_results.csv")

def restore_exam_results():
    print('exam_results HAS BEEN RESTORED TO ORIGINAL!')
    print('IF YOU DONT WANT THIS TO HAPPEN COMMENT OUT')
    print('restore_exam_results()')
    with open('exam_results.csv', mode='w', encoding='utf-8') as f_restore:
        f_restore.write("""Mark, Bobby, Susan, Mary
60, 77, 96, 81
95, 79, 60, 54
88, 81, 69, 84""")

######################
# restore_exam_results()
######################