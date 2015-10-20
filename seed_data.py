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

print(check_parens("{{[[]}]}"))
print(check_parens("(())()[][{}]"))

def piece(depth):
	if depth == 0:
		return ""
	elif random.choice([True, False]):
		opening = random.choice(bracket_open)
		closing = bracket_close[bracket_open.find(opening)]
		return "{}{}{}".format(opening, piece(depth - 1), closing)
	else:
		return "{}{}".format(piece(depth - 1), piece(depth - 1))

for i in range(10):
	this_string = piece(i)
	print(this_string, check_parens(this_string))

