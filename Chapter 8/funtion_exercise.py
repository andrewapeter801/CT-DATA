def print_input(answer):
    return answer 

response = input("Are you ready to start?")

while True:
    ask = input("What do you want to do?")
    print_input(ask)

    response = input("Ready yet?")
    if response.lower() == 'quit' or 'no':
            break