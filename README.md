# Password Security Suite

**Password Security Suite** is a comprehensive web-based application designed to educate users about password security through both offensive and defensive demonstrations. This tool provides an interactive platform to understand password vulnerabilities and best practices for protection.

## Overview

The application is built with Flask and offers two primary modes: **Attack** and **Defense**, allowing users to explore password security from multiple angles.

### Attack Mode
Test the resilience of passwords using three advanced cracking methodologies:

- **Brute Force Attack**: Exhaustively tries all possible character combinations up to a specified length, demonstrating why simple passwords are vulnerable
- **Rainbow Table Attack**: Leverages precomputed hash tables for instant lookup of commonly used passwords, showcasing the importance of salting
- **Hybrid Attack**: Combines wordlist-based attacks with character mutations, simulating sophisticated real-world attack scenarios with custom wordlist uploads

### Defense Mode
Learn how to strengthen password security:

- **Password Strength Checker**: Analyzes passwords against industry standards, providing detailed feedback on complexity, length, and character diversity
- **Hashing Algorithms**: Support for SHA256 and bcrypt encryption methods, demonstrating modern password protection techniques and the advantages of bcrypt's salting mechanism

## Key Features

- **User-Friendly Interface**: Intuitive web-based UI for both educational purposes and practical demonstrations
- **Educational Focus**: Clear explanations of attack methods and defense strategies
- **Multiple Methods**: Support for various cracking and protection techniques
- **Real-Time Analysis**: Instant feedback on password strength and attack feasibility
- **Security Best Practices**: Illustrates why certain practices (salting, strong hashing) matter

## Use Cases

Perfect for cybersecurity students, IT professionals, and anyone wanting to understand password vulnerabilities and protection mechanisms. Whether you're conducting security awareness training or learning about cryptography, this suite provides practical, hands-on experience.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mr-reyansh/password-security-suite.git
cd password-security-suite
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

### Attack Mode
- Choose an attack method (Brute Force, Rainbow Table, or Hybrid)
- For Hybrid attacks, upload a custom wordlist
- Enter the target hash to crack
- View results instantly

### Defense Mode
- Enter a password to check its strength
- Choose a hashing method (SHA256 or bcrypt)
- See the hashed output and strength analysis

## Project Structure

```
password-security-suite/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── static/
│   ├── style.css              # CSS styling
│   ├── matrix.js              # JavaScript utilities
│   ├── rainbow.txt            # Precomputed rainbow table
│   └── wordlist.txt           # Common passwords wordlist
├── templates/
│   ├── index.html             # Home page
│   ├── attack.html            # Attack mode interface
│   └── defense.html           # Defense mode interface
├── utils/
│   ├── brute.py               # Brute force cracking
│   ├── rainbow.py             # Rainbow table lookup
│   ├── hybrid.py              # Hybrid attack method
│   ├── bcrypt_utils.py        # Bcrypt hashing utilities
│   └── strength_check.py      # Password strength analysis
└── uploads/                   # Temporary upload directory
```

## Educational Disclaimer

This project is for educational purposes only. Do not use this tool for unauthorized access to systems or accounts. Always follow applicable laws and ethical guidelines.

## License

This project is open source and available under the MIT License.
