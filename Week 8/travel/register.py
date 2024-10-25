def register_user():
    print("=== Register User ===")
    
    # Getting input from the user
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    # Validate inputs
    if not username or not password or not email:
        print("All fields are required!")
        return
    
    # Store user information in a file
    with open("users.txt", "a") as f:
        f.write(f"{username},{password},{email}\n")
    
    print("Registration Successful!")

# Main function to start the registration process
if __name__ == "__main__":
    register_user()