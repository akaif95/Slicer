#This program is designed to take someone's email address
#And then slice it into two parts: the username and domain name

#Get the user email address
email = input("What is your email address?: ").strip()


#Slice out user name
user = email[:email.index("@")]


#slice domain name
domain = email[email.index("@") + 1 :]

             

#format message
output = "Your username is {} and your domain name is {}".format(user, domain)


#deisplay output message

print(output)
