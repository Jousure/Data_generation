import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


def generate_value(column: str):
    col = column.lower()

    # ---------- IDENTIFIERS ----------
    if col == "id" or col.endswith("_id"):
        return random.randint(1, 1_000_000)

    # ---------- NAMES ----------
    if "name" in col:
        if "planet" in col:
            return fake.word().title() + "-" + str(random.randint(1, 99))
        if "user" in col or "person" in col:
            return fake.name()
        if "company" in col:
            return fake.company()
        return fake.word().title()

    # ---------- TEXT ----------
    if any(k in col for k in ["description", "summary", "notes", "comment", "review"]):
        return fake.sentence(nb_words=12)

    # ---------- CATEGORY / TYPE ----------
    if "category" in col or "type" in col:
        return fake.word()

    if "status" in col or "state" in col:
        return random.choice(["active", "inactive", "pending", "archived"])

    # ---------- NUMBERS ----------
    if any(k in col for k in ["price", "amount", "cost", "salary"]):
        return round(random.uniform(10, 5000), 2)

    if "percent" in col or "percentage" in col:
        return round(random.uniform(0, 100), 2)

    if "score" in col or "rating" in col:
        return round(random.uniform(1, 5), 1)

    if "level" in col or "rank" in col:
        return random.randint(1, 10)

    if "quantity" in col or "count" in col:
        return random.randint(1, 1000)

    # ---------- BOOLEAN ----------
    if col.startswith("is_") or col.startswith("has_"):
        return random.choice([True, False])

    # ---------- DATES ----------
    if "date" in col or "time" in col or col.endswith("_at"):
        days_ago = random.randint(0, 365)
        return (datetime.utcnow() - timedelta(days=days_ago)).isoformat()

    # ---------- CONTACT ----------
    if "email" in col:
        return fake.email()

    if "phone" in col or "mobile" in col:
        return fake.phone_number()

    # ---------- LOCATION ----------
    if "city" in col:
        return fake.city()

    if "country" in col:
        return fake.country()

    if "address" in col:
        return fake.address().replace("\n", ", ")

    # ---------- WEB ----------
    if "url" in col or "link" in col:
        return fake.url()

    if "ip" in col:
        return fake.ipv4()
    
    if "website" in col:
        return fake.url()

    # ---------- META ----------
    if "version" in col:
        return f"v{random.randint(0,3)}.{random.randint(0,9)}.{random.randint(0,9)}"

    if "currency" in col:
        return random.choice(["USD", "EUR", "INR", "GBP", "JPY"])
    
    # age and year
    if "age" in col:
        return random.randint(18, 80)

    if "year" in col:
        return random.randint(1990, datetime.utcnow().year)
    
    #gender
    if "gender" in col:
        return random.choice(["Male", "Female", "Other"])   
    
    #File / Document fields
    if "file" in col or "document" in col:
        return fake.file_name()
    
    # organization
    if "organization" in col or "organisation" in col:
        return fake.company()
    
    #Bank / Account-like identifiers
    if "account" in col or "bank" in col or "iban" in col:
        return fake.bban()
    
    if "transaction" in col:
        return fake.uuid4()
    
    # ---------- FINANCE ----------
    if "price" in col or "amount" in col or "cost" in col:
        return round(random.uniform(10, 10000), 2)
    
    if "balance" in col or "total" in col:
        return round(random.uniform(0, 50000), 2)
    
    if "tax" in col or "vat" in col:
        return round(random.uniform(0, 5000), 2)
    
    #Priority / Severity
    if "priority" in col:
        return random.choice(["low", "medium", "high", "critical"])
    if "severity" in col:
        return random.choice(["minor", "major", "critical", "blocker"])
    
    # ---------- TECHNOLOGY ----------
    if "ip_address" in col or "ipaddress" in col:
        return fake.ipv4()
    
    if "mac_address" in col or "macaddress" in col:
        return fake.mac_address()
    
    # ---------- EDUCATION ----------
    if "course" in col or "subject" in col:
        return fake.word().title()
    
    if "degree" in col or "qualification" in col:
        return random.choice(["BSc", "BA", "MSc", "MA", "PhD", "MBA"])
    
    # ---------- HEALTH ----------
    if "disease" in col or "illness" in col:
        return fake.word().title()

    if "symptom" in col:
        return fake.word().title()

    # ---------- SPORTS ----------
    if "sport" in col:
        return random.choice(["Soccer", "Basketball", "Tennis", "Cricket", "Baseball", "Hockey"])
    
    if "team" in col:
        return fake.word().title() + " " + random.choice(["FC", "United", "Stars", "Rangers", "Warriors"])
    
    # ---------- ENTERTAINMENT ----------
    if "movie" in col or "film" in col:
        return fake.word().title()
    
    if "music" in col or "song" in col or "album" in col:
        return fake.word().title()
    
    # ---------- FOOD ----------
    if "food" in col or "dish" in col or "cuisine" in col:
        return fake.word().title()
    
    # ---------- ANIMALS ----------
    if "animal" in col or "pet" in col:
        return fake.word().title()
    
    # ---------- VEHICLES ----------
    if "vehicle" in col or "car" in col or "bike" in col:
        return fake.word().title()
    
    # ---------- WEATHER ----------
    if "weather" in col or "climate" in col:
        return random.choice(["Sunny", "Rainy", "Cloudy", "Windy", "Stormy", "Snowy"])
    
    # ---------- HOBBIES ----------
    if "hobby" in col or "interest" in col:
        return fake.word().title()
    
    # ---------- PROFESSIONS ----------
    if "profession" in col or "occupation" in col or "career" in col:
        return fake.job()
    
    # ---------- RELIGION ----------
    if "religion" in col or "faith" in col:
        return random.choice(["Christianity", "Islam", "Hinduism", "Buddhism", "Judaism", "Sikhism"])
    
    # ---------- LANGUAGES ----------
    if "language" in col or "lang" in col:
        return random.choice(["English", "Spanish", "Mandarin", "Hindi", "French", "German"])
    
    # ---------- COLORS ----------
    if "hex_color" in col or "hexcode" in col:
        return fake.hex_color()
    
    if "rgb_color" in col:
        return f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"
    
    # ---------- SPECIALS ----------
    if "color" in col:
        return fake.color_name()
    
    if "job" in col or "occupation" in col:
        return fake.job()
    
    # ---------- PERCENT / CHEMICAL ----------
    if "alcohol" in col or "abv" in col:
        return round(random.uniform(8.0, 15.0), 1)

    if "ph" in col:
        return round(random.uniform(2.8, 4.2), 2)

    # ---------- RATING / SCORE ----------
    if "rating" in col or "quality" in col:
        return round(random.uniform(1, 5), 1)
    
    if "winery" in col:
        return fake.company() + " Winery"

    if "grape" in col or "variety" in col:
        return fake.word().title()

    # ---------- FALLBACK ----------
    return fake.word()


def generate_row(columns: list[str]) -> dict:
    """
    Generate a single row of data.
    """
    return {col: generate_value(col) for col in columns}


def generate_rows(columns: list[str], rows: int) -> list[dict]:
    """
    Generate multiple rows of data.
    """
    return [generate_row(columns) for _ in range(rows)]