from random import choices

def generate_unique_id():
    return ''.join(choices('0123456789', k=6))
