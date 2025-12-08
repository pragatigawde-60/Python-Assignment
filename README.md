🔐 Password Strength Checker (Python)
This is a simple Python script that checks the strength of a user-entered password using regular expressions.
It validates whether the password meets strong security requirements such as length, uppercase letters, lowercase letters, numbers, and special characters.


✅ Features
Checks if the password:
✔️ Is at least 8 characters long
✔️ Contains an uppercase letter
✔️ Contains a lowercase letter
✔️ Contains a number (0–9)
✔️ Contains a special character (e.g., ! @ # $ % ^ & * etc.)
Provides user-friendly output:
Prints Strong password if all criteria are met Otherwise shows a list of missing requirements


📁 Project Structure
├── password_checker.py
└── README.md


🧠 How It Works
The script uses Python’s built-in re module (regular expressions) to test the given password against multiple security rules.
If all rules pass, the password is considered strong.


▶️ How to Run
save and Run the script using: python password_checker.py
Enter a password when prompted.


🧪 Example Output

Strong Password Example

Enter your password to check its strength: Hello@123
✅ Strong password! Your password meets all security requirements.


Weak Password Example

<img width="610" height="152" alt="image" src="https://github.com/user-attachments/assets/a926a0ad-4f31-4451-adfb-3d5dd8cf4e10" />
