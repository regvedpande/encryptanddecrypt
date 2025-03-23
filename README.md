
# CipherVault

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A secure file encryption and decryption web application built using **Flask** and **React**. This project allows users to encrypt DOC, DOCX, and PDF files with a password and then decrypt them to retrieve the original file. The application uses AES encryption with PBKDF2 key derivation for strong security.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **File Encryption:** Securely encrypt your files using a user-supplied password.
- **File Decryption:** Decrypt files encrypted by the application.
- **Web Interface:** A user-friendly UI built with React and Thymeleaf (if applicable) for ease of use.
- **Secure Algorithms:** Implements AES encryption in CBC mode with PBKDF2 key derivation.
- **Cross-Platform:** Designed to work on Windows, macOS, and Linux environments.

## Tech Stack

- **Backend:** Python, Flask, Cryptography
- **Frontend:** React, Axios, Bootstrap
- **Database (Optional):** H2 (if using the extended version with DB storage)
- **Build Tool:** Maven (for Spring Boot projects) / Node.js & npm for the React frontend

## Installation

## Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)
- [Node.js and npm](https://nodejs.org/)
- [Git](https://git-scm.com/)
- (Optional) [Maven](https://maven.apache.org/) if you extend the project with a Spring Boot version

## Clone the Repository

```bash
git clone https://github.com/regvedpande/encryptanddecrypt.git
cd encryptanddecrypt
```

## Setting Up the Flask Backend

1. Navigate to the `backend` folder:

    ```bash
    cd backend
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

   - On Windows (PowerShell):

     ```powershell
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application:

    ```bash
    python app.py
    ```

   The server should start on [http://localhost:5000](http://localhost:5000).

### Setting Up the React Frontend

1. Open a new terminal window and navigate to the `frontend` folder:

    ```bash
    cd frontend
    ```

2. Install the Node.js dependencies:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

   The React app will run on [http://localhost:3000](http://localhost:3000).

## Usage

1. **Encrypt a File:**  
   - Visit [http://localhost:3000](http://localhost:3000).
   - Navigate to the "Encrypt File" section.
   - Upload a DOC, DOCX, or PDF file and provide a password.
   - Click the **Encrypt** button and download the encrypted file (in `.enc` format).

2. **Decrypt a File:**  
   - Go to the "Decrypt File" section.
   - Upload the previously encrypted `.enc` file and enter the same password.
   - Click **Decrypt** to download the original file.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact me at [regregd@outlook.com](mailto:regregd@outlook.com).

---

Happy encrypting and decrypting!
```
