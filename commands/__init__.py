

class AuthCommands:
    LOGIN = "SELECT * FROM admin WHERE username = %s AND PASSWORD = %s;"