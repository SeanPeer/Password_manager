
# Password Manager

Password Manager is a simple, user-friendly application built with Python and Tkinter. It helps users generate strong passwords and store them securely. With an easy-to-use interface, Password Manager ensures that your passwords are both strong and securely saved for future reference.

## Features

- **Generate Strong Passwords**: Automatically generate strong passwords that include uppercase and lowercase letters, digits, and special characters.
- **Save Passwords Securely**: Save your passwords along with your website and username information securely in a local file.
- **Easy to Use**: Simple graphical user interface for generating and saving passwords with just a few clicks.

## Prerequisites

Before running Password Manager, ensure you have Python installed on your system. Python 3.6 or higher is recommended.

## Installation

1. Clone the repository or download the source code to your local machine.
2. Ensure you have Python installed. If not, download and install Python from [python.org](https://www.python.org/).
3. (Optional) Create a virtual environment for the project and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. No additional libraries are required as the project uses Tkinter, which is included with Python.

## Running the Application

To run Password Manager, navigate to the directory containing the script and run the following command:

```sh
python main.py
```

Make sure to replace `main.py` with the actual filename if it's different.

## Usage

1. **Generating a Password**: Click on the "Generate" button to automatically fill the password field with a strong, randomly generated password.
2. **Saving Credentials**: Enter the website and your email/username, then either manually enter a password or generate one. Click "Save" to store the credentials.
3. **Viewing Saved Passwords**: Currently, passwords are saved to `Data.txt` in the same directory as the application. Open this file in a text editor to view your saved credentials.

## Customization

- You can adjust the length of the generated password by modifying the `create_strong_password` function in the source code.
- The password and credentials are stored in a plaintext file named `Data.txt`. For additional security, consider implementing encryption for stored passwords.

## Contributing

Contributions to improve Password Manager are welcome. Please feel free to fork the repository and submit a pull request with your enhancements.

## License

This project is open-source and available under the MIT License.
