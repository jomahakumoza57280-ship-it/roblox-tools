def validate_user_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) < 1:
        raise ValueError('Input cannot be empty')
    if len(user_input) > 100:
        raise ValueError('Input cannot exceed 100 characters')
    return True


def main_processing_loop():
    user_inputs = []
    while True:
        user_input = input('Enter user input (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            break
        try:
            validate_user_input(user_input)
            user_inputs.append(user_input)
            print(f'Valid input received: {user_input}')
        except ValueError as e:
            print(f'Error: {e}')
    print('Exiting loop. Collected inputs:', user_inputs)


if __name__ == '__main__':
    main_processing_loop()