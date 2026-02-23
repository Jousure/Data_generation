import random
import uuid
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def generate_value(col: str):
    c = col.lower()

    if "id" in c:
        return str(uuid.uuid4())

    if "name" in c:
        return fake.word().capitalize()

    if "flavor" in c:
        return random.choice(["Sweet", "Bitter", "Spicy", "Mystic", "Cosmic"])

    if "origin" in c or "world" in c or "planet" in c:
        return random.choice(["Eldoria", "Zypheron", "Nova Prime", "Aether"])

    if "price" in c or "cost" in c:
        return round(random.uniform(5, 500), 2)

    if "potency" in c or "level" in c:
        return random.randint(1, 100)

    if "date" in c or "time" in c:
        start = datetime.now() - timedelta(days=365)
        return start + timedelta(seconds=random.randint(0, 31_536_000))

    return fake.word()
