from random import choices

def generate_unique_id():
    return str(choices('0123456789', k=6))
