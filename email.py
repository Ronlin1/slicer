# email input
email = input("Please enter your email: \n").strip()

# index
index = email.index("@")

# username
username = email[:index]

# domain
domain = email[index+1:]

print(f"Your username is {username} and domain is {domain}!")
