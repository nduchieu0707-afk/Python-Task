import hashlib

def hexpas(password):
    return hashlib.md5(password.encode()).hexdigest()

def login():
    user = input("username: ")
    pas = input("password: ")
    try:
        with open("save.txt", "r") as file:
            for index, line in enumerate(file):
                use, hex = line.strip().split(";")
                if use == user and hex == hexpas(pas):
                    print("Welcome")
                    return user, index
    except:
        pass
    print("Wrong")
    return None, None

def register():
    user = input("username: ")
    pas = input("password: ")

    try:
        with open("save.txt", "r") as file:
            if any(user in line for line in file):
                print("User exists")
                return
    except:
        pass
    with open("save.txt", "a") as file:
        file.write(f"{user};{hexpas(pas)}\n")
    print("Register")

def menu(username, userid):
    while True:
        print(f"User: {username}")
        choice = input("Choice: ")
        if choice == "1":
            print(f"ID: {userid}, Name: {username}")
        elif choice == "0":
            break

def main():
    while True:
        choice = input("Choice: ")

        if choice == "1":
            user, userid = login()
            if user:
                menu(user, userid)
        elif choice == "2":
            register()
        elif choice == "0":
            break
if __name__ == "__main__":
    main()