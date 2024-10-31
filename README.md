
```markdown
# Password Generator

A simple password generator that creates secure passwords based on user-defined length. The generated passwords include uppercase letters, lowercase letters, special characters, and digits, ensuring a strong combination of characters.

## Features

- Generates passwords of specified length.
- Ensures the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
- Avoids using the same character more than once in the generated password.
- Validates user input to ensure the length is within acceptable limits.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the code file.

    ```bash
    git clone https://github.com/osamagmex/password-generator.git
    cd password-generator
    ```

2. Run the script using Python:

    ```bash
    python password_generator.py
    ```

3. Enter the desired length of the password when prompted.

4. The generated password will be displayed on the screen.

## Example

```
How long is your password: 12
Your password is: aB3$zE7qHdP
```

## Code Explanation

- **Imports:** The `random` module is imported to generate random numbers for selecting characters.
- **Character Sets:** The code defines sets of uppercase letters, lowercase letters, special characters, and digits.
- **Function:** The `pass_gen` function generates the password while ensuring the inclusion of all required character types.
- **Input Handling:** The script prompts the user for the desired password length, checks for valid input, and displays an appropriate message if the input is invalid.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you wish to contribute to this project, feel free to submit a pull request or open an issue for discussion.

## Acknowledgments

- Inspired by the need for strong, secure passwords in the digital age.
```

