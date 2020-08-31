import random
import string

def generate_id(string_length=8):
    """Generate a random string of letters and digits """
    allowed_characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(allowed_characters) for _ in range(string_length))

if __name__ == "__main__":
    print(generate_id())