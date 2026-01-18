print("LETS BEGIN😝")

password = input("Enter your password!: ")

if len(password) < 6:
    print("Weak password!😔")
elif any(char.isdigit() for char in password) and any(not char.isalnum() for char in password):
    print("WOAH! Strong password🗣️")
else:
    print("hmmm, Medium password👾")