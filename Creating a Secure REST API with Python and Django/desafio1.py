def perform_login(registered_user, username, password):
    # Check if the username is registered
    if username == registered_user["username"]:
        # Check if the provided password is correct
        if password == registered_user["password"]:
            return "Access granted for {}.".format(username)
        else:
            return "Incorrect password for {}. Access denied.".format(username)
    else:
        return "User {} not found. Access denied.".format(username)

# Main function of the program
def main():
    # Asking for the registered username
    registered_username = input()
    # Asking for the registered password
    registered_password = input()
    
    # Creating a dictionary containing the information of the registered user
    registered_user = {"username": registered_username, "password": registered_password}
    
    # Asking for the username to attempt login
    login_username_attempt = input()
    # Asking for the password to attempt login
    login_password_attempt = input()
    
    # Calling the perform_login function to check login and get the result
    result = perform_login(registered_user, login_username_attempt, login_password_attempt)
    
    # Printing the result of the login process
    print(result)

# Checking if the script is being executed as the main program
if __name__ == "__main__":
    # Calling the main function to initiate the login process
    main()