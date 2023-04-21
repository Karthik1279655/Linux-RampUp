import re
value = []
passwords = [i for i in input("Enter the password : ").split(',')]
for password in passwords:
    if len(password) < 7 or len(password) > 12:
        continue
    else:
        pass
    if not re.search("[a-z]", password):
        continue
    elif not re.search("[A-Z]", password):
        continue
    elif not re.search("[0-9]", password):
        continue
    elif not re.search("[#$@]", password):
        continue
    else:
        pass
    value.append(password)
print(" ".join(value))
