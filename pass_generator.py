import random

def generate_password():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    simbols = ['!', '#', '$', '%', '^', '&','*']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracters = upper + lower + simbols + numbers

    password = []

    for i in range(15):
        caracters_random = random.choice(caracters)
        password.append(caracters_random)

    password = ''.join(password)
    return password


def run():
    password = generate_password()
    print('Your new password is: ' + password)



if __name__ == "__main__":
    run()