# Written by Lucas Gavrielides
# Takes a password and decodes it using a reverse operation from encode
def decode(password):
    return ''.join([str((int(item) - 3) % 10) for item in password])
