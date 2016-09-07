
# TODO - write has_teen
def has_teen(a, b, c):
	if a >= 13 and a <= 19 and b >= 13 and b <= 19 and c >=13 and c<= 19:
		return True
	else:
		return False

print has_teen(13, 15, 17) #True
print has_teen(13, 15, 8) #False
print has_teen(2, 4, 6) #False
print has_teen(13, 13, 15) #True
# TODO - write not_string

# TODO - write icy_hot
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

# TODO - write two_as_one

# TODO - write pig_latinify
