'''
------From Mit Mirani------
  """"Password Manager""""
'''

from cryptography.fernet import Fernet


#execute write_key function just for once
#  to generate the key to use it in encryption
# So execute the write_key function for once and then 
# you can comment the function or remove it.
'''

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

#Function to view the username and password from the saved file.
def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("Username:",user, ", Password:",fer.decrypt(passw.encode()).decode())

#Function to add the info to the file
def add():
    u_name = input("Account name / Username: ")
    pwd = input("Password: ")

    with open('passwords.txt','a') as f:
        f.write(u_name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

#User menu 
while True:
    mode = input("Would you like to add a new password or view existing one's (view, add), or press q to quit? ")
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print ("Invalid Mode.")

