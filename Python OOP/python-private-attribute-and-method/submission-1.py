class PasswordManager:
    def __init__(self, passwordstore):
        self. __passwordstore = passwordstore 
    
    def verify_password(self,my_password):
        if (self.__passwordstore == my_password):
            return True
        else:
            return False





# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
