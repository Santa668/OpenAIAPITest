import json
from base64 import b64decode, b64encode
from cryptography.fernet import Fernet
import os
#import openai_secret_manager


CONFIG_FILE = "config.json"

# load the secrets
#assert "openai" in openai_secret_manager.#ena apip list#
# secrets = openai_secret_manager.get_secret("openai")

# set environment variable for open# apip list#os.environ["OPENAI_API_KEY"] = secrets["api_key"]


def get_api_key():
    """
    Retrieves the OpenAI API key from the environment variables.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        config = read_config()
        api_key = config.get("api_key")
        if not api_key:
            api_key = prompt_api_key()
            os.environ["OPENAI_API_KEY"] = api_key
            config["api_key"] = encrypt(api_key)
            write_config(config)
        else:
            api_key = decrypt(api_key)
            os.environ["OPENAI_API_KEY"] = api_key
    return api_key


def prompt_api_key():
    """
    Prompts the user to enter their OpenAI API key.
    """
    api_key = input("Please enter your OpenAI API key: ")
    return api_key


def read_config():
    """
    Reads the configuration file and returns its contents.
    """
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    return config


def write_config(config):
    """
    Writes the configuration to the configuration file.
    """
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def encrypt(value):
    """
    Encrypts a value using a secret key and returns the encrypted value.
    """
    key = get_secret_key()
    f = Fernet(key)
    encrypted = f.encrypt(value.encode())
    return b64encode(encrypted).decode()


def decrypt(value):
    """
    Decrypts a value using a secret key and returns the decrypted value.
    """
    key = get_secret_key()
    f = Fernet(key)
    decrypted = f.decrypt(b64decode(value.encode()))
    return decrypted.decode()


def get_secret_key():
    """
    Returns a secret key used for encrypting and decrypting values.
    """
    key_path = os.environ.get("SECRET_KEY_PATH")
    if key_path:
        with open(key_path, "rb") as f:
            key = f.read()
    else:
        key = os.environ.get("SECRET_KEY")
        if not key:
            raise ValueError("SECRET_KEY or SECRET_KEY_PATH environment variable must be set")
        key = key.encode()
    return key
