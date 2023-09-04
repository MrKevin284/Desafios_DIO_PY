def authenticate(username, password, auth_code, login_username, login_password, provided_auth_code):
    # Check if the login username is registered
    if login_username == username:
        # Check if the provided password is correct
        if login_password == password:
            # Check if the provided authentication code is correct
            if provided_auth_code == auth_code:
                return "Access granted for {}.".format(login_username)
            else:
                return "Incorrect authentication code for {}. Access denied.".format(login_username)
        else:
            return "Incorrect password for {}. Access denied.".format(login_username)
    else:
        return "User {} not found. Access denied.".format(login_username)

def main():
    # User information registration
    username = input()
    password = input()
    
    # Authentication code setup
    auth_code = input()
    
    # Login attempt
    login_username = input()
    login_password = input()
    
    # Provided authentication code input
    provided_auth_code = input()
    
    # Authenticate with provided authentication code
    result = authenticate(username, password, auth_code, login_username, login_password, provided_auth_code)  
    print(result)

if __name__ == "__main__":
    main()