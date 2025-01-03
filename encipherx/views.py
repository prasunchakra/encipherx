from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    """
    Receives text, key, cipher type, and encryption mode (encrypt/decrypt).
    Calls the appropriate cipher function.
    Renders the result page with the processed text.
    """
    # Get data from the form
    plaintext = request.POST['plaintext']
    key = request.POST['key']         
    cipher = request.POST['cipher']  
    mode = request.POST['mode']       

    if cipher == 'caesar':
        output_text = caesar_cipher(plaintext, int(key), mode)
    elif cipher == 'vigenere':
        output_text = vigenere_cipher(plaintext, key, mode)
    elif cipher == 'aes':
        output_text = aes_cipher(plaintext, key, mode)
    else:
        output_text = "Invalid cipher selected."

    return render(request, 'result.html', {'encrypted_text': output_text})


def caesar_cipher(text, shift, mode='encrypt'):
    """
    Simple Caesar cipher that shifts alphabetical characters by 'shift'.
    Non-alphabetic characters remain unmodified.
    """
    # For decryption, invert the shift
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        # Encrypt uppercase letters
        if char.isalpha():
            # Choose ASCII offset based on uppercase/lowercase
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')

            original_position = ord(char) - offset
            new_position = (original_position + shift) % 26
            new_char = chr(offset + new_position)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)


def vigenere_cipher(text, key, mode='encrypt'):
    pass


def aes_cipher(text, key, mode='encrypt'):
    pass
