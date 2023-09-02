# Read through the following expressions and predict the output printed output.
# Justify your predictions in a comment below each expression

# 1.
30 > 12
print(True)

# 2.
4 < 4
print(False)

# 3.
12 == '12'
print(False, "int and string are different types")

# 4.
7 < 7.0
print(False, "int and string are different types")



# 5.
if 'Python' > 'JavaScript':
    current_thoughts = '🐍🐍🐍'
else:
    current_thoughts = 'Take me back to Node!'
print(current_thoughts,"comparison is done lexicographically")

# 6.
1 == True
print(1 == True, 'truthy value')


# 7.
0.9 < True
print(0.9 < True, " as True is ==1 when compared")


# 8.
fav_animal = '🐈' if 36**2 > 1300 else '🐕'
print(fav_animal, "last dog")

# 9.
print(14 > 5 and len('tree') == 8/2, "True as both statements are true")


# 10.
print(5 or 0.7,'<----5 as its the first truthy value')


# 11.
print(5 > 10 or 4,'<------ 4 as its the first truthy value')
