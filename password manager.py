
from cryptography.fernet import Fernet

#def write_key():
    #key = fernet.generate_key()
    #with open("key.key","wb") as key_file:
        #key_file.write(write)
#write_key()


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("what is the master password")
#key = load_key()
#fer = Fernet(key)





def view():
    with open('passwords.txt'+fer.decrypt(passw.encode()).decode(),'r') as f:
         for line in f.readline():
             print(line.rstrip())
           #  data = line.rstrip()
            #user,passw = data.split("|")
            #print("user:",user,"password:",passw)


def add():
    name = input('Account Name: ')
    pwd = input("password: ")

    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()) + "\n")

while True:
    mode = input("would you like to add a new password or view existing ones (view,add),press q to quit? ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue
