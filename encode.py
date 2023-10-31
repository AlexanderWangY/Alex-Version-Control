# Written by Lucas Gavrielides
# Takes an 8 number password and shifts it by 3!
def encode(password):
    return ''.join([str((int(item) + 3) % 10) for item in password])
