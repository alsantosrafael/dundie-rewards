from random import sample
from string import ascii_letters, digits


def generate_simple_password(length: int = 8) -> str:
    """Generate a simple random password
    [A-Z],[a-z][0-9]
    """
    return "".join(sample(ascii_letters + digits, length))
