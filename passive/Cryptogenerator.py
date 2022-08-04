import base64
import logging
import traceback

from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    print(key)
    with open("secret.txt", "wb") as key_file:
        key_file.write(key)


def load_key():
    # print('acd '+open("secret.key", "rb").read())
    return open("secret.txt", "rb").read()


def endocedata(passwordKey):
    key = load_key()

    f = Fernet(key)
    encoded_message = passwordKey.encode()
    enc = f.encrypt(encoded_message)
    # print(enc)
    return enc


def decodedata(passwordKey):
    # try:
        key = load_key()
        f = Fernet(key)
        print('dec ' + passwordKey)
        # passwordKey1 = f.decrypt(passwordKey)
        # print('dec byte' + passwordKey1)
        dec = f.decrypt(passwordKey.encode())
        print('dec1 ' + dec.decode())
        return dec

    # except Exception as e:
    #     print('excp '+ str(e))
# generate_key()
# b'_IJaBCO2nFnVx3IS5JIePkfabi-0YJmqncDDN4HMpkg='

def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(load_key()) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        # log the error if any
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(txt):
    try:
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(load_key())
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception as e:
        # log the error
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None