
def has_teen(a, b, c):
	if a >= 13 and a <= 19 or b >= 13 and b <= 19 or c >=13 and c<= 19:
		return True
	else:
		return False

print has_teen(13, 15, 17) #True
print has_teen(13, 15, 8) #False
print has_teen(2, 4, 6) #False
print has_teen(13, 13, 15) #True
print has_teen(19, 1, 4) #True
print has_teen(19, 13, 4) #True

def not_string(str):
	if str.startswith ('not'):
		return str + "not"
	else:
		return "not" + str
print not_string('not happy ') #not happy not
print not_string(' super happy') #not super happy

def icy_hot(a, b):
	if a < 0 and b > 100:
		return True
	elif a > 100 and b < 0:
		return True
	else:
		return False

print icy_hot(-2, 102) #True
print icy_hot(2, 70) #False
print icy_hot(4, 101) #False
print icy_hot(102, -2)#True
# TODO - write closer_to
def closer_to(t, a, b):
	if abs(t-a) < abs(t-b):
		return a
	if abs (t-b) < abs(t-a):
		return b
	if abs(t-a) == abs(t-b):
		return 0

print closer_to(5, 8, 4) #4
print closer_to(5, 3, 1) #3
print closer_to(5, 7, 3) #0

def two_as_one(a, b, c):
	if a + b == c:
		return True
	if a + c == b:
		return True
	if b + c == a:
		return True
	else:
		return False

print two_as_one(1, 2, 3) #True
print two_as_one(2, 5, 3) #True
print two_as_one(1, 3, 9) #False
print two_as_one(7, 4, 3) #True

# TODO - write pig_latinify
