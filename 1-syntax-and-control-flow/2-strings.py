# Take a look at the following variables



tutor = 'david john bartlett'

title = 'Mr'

dob = "30/12/1996"

job_title = "Senior Tutor"

pronouns =  'he/him'


# Use them to create new strings with the following values:


# 1. first_name = David
first_name = tutor[0].capitalize()+tutor[1:5]
print(first_name)
# 2. surname = Bartlett
surname = tutor[11].capitalize()+tutor[12:]
print(surname)

# 3. reverse_reverse = tteltraB divaD
print(surname[::-1], first_name[::-1])

# 4. digital_signature = David J. Bartlett
print(first_name, tutor[6].capitalize() + '.',surname)

# 5. side_hustle = DJ Bartlett
print(first_name[0] + tutor[6].capitalize(), surname)

# 6. us_dob = 12/30/96
print(dob[3:6]+dob[:3]+dob[-2:])

# 7. slack_handle = David-NC
print(first_name+'-NC')

# 8. twitter_handle = @dbart3012
print('@'+first_name[0].lower()+surname[:4].lower()+dob[:2]+dob[3:5])

# 9. formal_salutation = Mr D Bartlett
print(title, first_name[0], surname)

# 10. email_signature = David Bartlett (he/him) - Senior Tutor
print(f'{first_name} {surname} ({pronouns}) - {job_title}')

# 11. sandwich = bartdavidlett
print(surname[:4].lower()+first_name.lower()+surname[-4:])

# 12. pig_latin = Avidday Artlettbay
