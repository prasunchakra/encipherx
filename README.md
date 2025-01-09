
# The Cipher Project

A simple, but functional cipher project that supports **encryption** and **decryption** using the classic Caesar Cipher technique. This project is intended to demonstrate basic cryptographic concepts. It currently focuses on shifting letters in the alphabet by a specified number of positions. 


## Introduction

The **Caesar Cipher** is one of the oldest and simplest forms of encryption. It works by shifting each letter of the plaintext by a fixed number of positions in the alphabet. Despite its simplicity (and relative lack of security by modern standards), it illustrates fundamental concepts of encryption and decryption. 

This project aims to:
- Provide a clear, working example of Caesar Cipher encryption and decryption.
- Serve as a stepping stone to learn more robust encryption methods.
- Encourage students and developers to build upon this foundation to create more valuable and secure applications.

---

## Key Features

- **Encryption**: Convert plaintext to ciphertext by shifting the alphabet.
- **Decryption**: Convert ciphertext back to plaintext using the reverse shift.
- **Custom Shift Value**: Easily modify the shift value to experiment with different ciphers.
- **Live Demo**: The project is live, demonstrating real-time encryption and decryption.

---

## How It Works

1. **Choosing a Shift**: A numeric shift value is set (commonly between 1 and 25).
2. **Encrypting a String**:
   - Each letter of the input string is shifted forward by the shift value in the alphabet.
   - For example, with a shift of 3, **A** becomes **D**, **B** becomes **E**, and so on.
3. **Decrypting a String**:
   - Each letter of the input string is shifted backward by the shift value in the alphabet.
   - For the same shift of 3, **D** becomes **A**, **E** becomes **B**, and so on.
4. **Handling Edge Cases**:
   - Non-alphabetic characters (e.g., digits, punctuation) can be left as-is or handled based on project requirements.
   - If the shift exceeds 26, it wraps around (e.g., 30 becomes effectively 4).

---

## Installation and Setup

0. **Prerequisites**
   - Python 3.10 or later
   - Git

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/prasunchakra/cipher.git
   cd cipher
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**
   ```bash
   python manage.py runserver
   ```

4. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.
   

## Possible Improvements and Roadmap
- [ ] Add a REST API for the application.
- [ ] Add more cipher methods like Vigenère, RSA, AES, etc.
- [ ] Move towards modern encryption standards like AES, RSA, etc.
- [ ] Add more features like key management, user authentication, etc.


## Contributing

Contributions are welcome! Please feel free to submit a pull request.


