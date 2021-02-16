def validate(prompt, char_type):
    """ Validates input, returns validated input
    Types: A = Alpha, I = Int."""
    if char_type == 'A':
        while True:
            user_input = input(prompt).upper()
            try:
                if len(user_input) > 245:
                    print(f'\n.............\n'
                          f'Invalid input you entered {len(user_input)} characters\n'
                          f'Character limit is 245.\n')
                elif user_input.replace(" ", "").isalpha():
                    return user_input
                print("\n.............\n"
                      "Invalid input, non letter character.\n")
            except (ValueError, TypeError):
                print("\n.............\n"
                      "Invalid input, non letter character.\n")
    elif char_type == 'I':
        while True:
            user_input = input(prompt)
            try:
                if 26 > int(user_input) > 0:
                    return int(user_input)
                print("\n.............\n"
                      "Invalid input, outside range of 1-25.\n")
            except (ValueError, TypeError):
                print("\n.............\n"
                      "Invalid input, not a number.\n")


def yes_or_no(prompt):
    """ Validates input, returns Y or N."""
    print(prompt)
    user_input = input("[Y]es or [N]o? ")[0].upper()
    while True:
        try:
            if user_input.isalpha() and (user_input == "Y" or user_input == "N"):
                return user_input
            print("\n.............\n"
                  "Invalid input\n")
            print(prompt)
            print("Y for yes, N for no.")
            user_input = input("[Y]es or [N]o? ").upper()
        except TypeError:
            print("\n.............\n"
                  "Invalid input\n")
            print(prompt)
            print("Y for yes, N for no.")
            user_input = input("[Y]es or [N]o? ").upper()
