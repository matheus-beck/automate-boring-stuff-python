'''
This function takes a list value as an argument and returns
a string with all the items separated by a comma and a space, 
with 'and' inserted before the last item.
'''

def comma_code(list):
	string = ''
	for i in list:
		if i == list[len(list)-1]: # Check last element in list
			string += 'and ' + str(i)
		else:
			string += str(i) + ' '
	return string

spam = ['apples', 'bananas', 'tofu', 'cats']
my_string = comma_code(spam)
print(my_string)
