import random

bracket_open = "([<{“‘«"
bracket_close = ")]>}”’»"

def check_parens(test_string):
	stack = []
	for c in test_string:
		if c in bracket_open:
			stack.append(c)
		if c in bracket_close:
			if not stack:
				return False	
			if bracket_open.find(stack.pop()) != bracket_close.find(c):
				return False
	else:
		return not stack

def good_piece(depth):
	if depth == 0:
		return ""
	idx = random.randint(0, 1)
	if idx == 0:
		opening = random.choice(bracket_open)
		closing = bracket_close[bracket_open.find(opening)]
		return "{}{}{}".format(opening, good_piece(depth - 1), closing)
	elif idx == 1:
		return "{}{}".format(good_piece(depth - 1), good_piece(depth - 1))

def bad_piece(depth):
	result = good_piece(depth)

	if len(result) == 0:
		return result

	for i in range(5):
		index = random.randint(0, len(result) - 1)
		insert = random.choice(random.choice([bracket_close, bracket_open]))
		return result[:index-1] + insert + result[index:]

print("The good!")

for i in range(10):
	this_string = good_piece(i)
	print(check_parens(this_string), this_string)

print()
print("The bad!")

for i in range(10):
	this_string = bad_piece(i)
	print(check_parens(this_string), this_string)

