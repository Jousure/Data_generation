import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Context-aware data generators for different domains
DOMAIN_SPECIFIC_GENERATORS = {
    "customer": {
        "first_name": lambda: fake.first_name(),
        "last_name": lambda: fake.last_name(),
        "email": lambda: fake.email(),
        "phone": lambda: fake.phone_number(),
        "address": lambda: fake.street_address(),
        "city": lambda: fake.city(),
        "country": lambda: fake.country(),
        "postal_code": lambda: fake.postcode(),
        "registration_date": lambda: fake.date_between(start_date='-5y').isoformat(),
        "last_purchase_date": lambda: fake.date_between(start_date='-1y').isoformat(),
        "total_spent": lambda: round(random.uniform(50, 5000), 2),
        "customer_id": lambda: f"CUST{random.randint(10000, 99999)}",
        "loyalty_points": lambda: random.randint(0, 10000),
        "membership_level": lambda: random.choice(["Bronze", "Silver", "Gold", "Platinum"]),
        "age": lambda: random.randint(18, 80),
        "gender": lambda: random.choice(["Male", "Female", "Other"]),
        "income": lambda: random.randint(25000, 150000),
    },
    "product": {
        "product_id": lambda: f"PROD{random.randint(10000, 99999)}",
        "product_name": lambda: random.choice([
            "Wireless Headphones", "Smart Watch", "Laptop Stand", "USB-C Hub", 
            "Mechanical Keyboard", "Gaming Mouse", "Monitor", "Webcam",
            "Bluetooth Speaker", "Power Bank", "Phone Case", "Tablet"
        ]),
        "category": lambda: random.choice(["Electronics", "Accessories", "Computers", "Audio", "Mobile"]),
        "price": lambda: round(random.uniform(9.99, 999.99), 2),
        "stock_quantity": lambda: random.randint(0, 1000),
        "supplier": lambda: fake.company(),
        "sku": lambda: f"SKU-{random.randint(100000, 999999)}",
        "description": lambda: f"High-quality {random.choice(['product', 'item', 'device'])} with {random.choice(['premium', 'advanced', 'basic'])} features",
        "weight": lambda: round(random.uniform(0.1, 5.0), 2),
        "dimensions": lambda: f"{random.randint(1,50)}x{random.randint(1,50)}x{random.randint(1,20)}cm",
        "brand": lambda: random.choice(["TechPro", "DigitalGear", "SmartTech", "ElectroMax", "PowerTech"]),
        "rating": lambda: round(random.uniform(3.0, 5.0), 1),
        "reviews_count": lambda: random.randint(0, 5000),
    },
    "employee": {
        "employee_id": lambda: f"EMP{random.randint(10000, 99999)}",
        "first_name": lambda: fake.first_name(),
        "last_name": lambda: fake.last_name(),
        "email": lambda: fake.company_email(),
        "department": lambda: random.choice(["Engineering", "Sales", "Marketing", "HR", "Finance", "Operations"]),
        "position": lambda: random.choice([
            "Software Engineer", "Product Manager", "Sales Representative", 
            "Marketing Specialist", "HR Coordinator", "Financial Analyst",
            "Team Lead", "Senior Developer", "Account Manager", "Data Analyst"
        ]),
        "salary": lambda: random.randint(40000, 150000),
        "hire_date": lambda: fake.date_between(start_date='-10y').isoformat(),
        "manager_id": lambda: f"EMP{random.randint(10000, 99999)}",
        "status": lambda: random.choice(["Active", "On Leave", "Terminated"]),
        "performance_score": lambda: round(random.uniform(2.5, 5.0), 1),
        "years_experience": lambda: random.randint(0, 30),
        "location": lambda: random.choice(["New York", "San Francisco", "Chicago", "Austin", "Remote"]),
    },
    "order": {
        "order_id": lambda: f"ORD{random.randint(100000, 999999)}",
        "customer_id": lambda: f"CUST{random.randint(10000, 99999)}",
        "order_date": lambda: fake.date_between(start_date='-2y').isoformat(),
        "shipping_date": lambda: fake.date_between(start_date='-2y').isoformat(),
        "delivery_date": lambda: fake.date_between(start_date='-2y').isoformat(),
        "status": lambda: random.choice(["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]),
        "total_amount": lambda: round(random.uniform(25, 1000), 2),
        "shipping_cost": lambda: round(random.uniform(5, 50), 2),
        "tax": lambda: round(random.uniform(2, 100), 2),
        "payment_method": lambda: random.choice(["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]),
        "tracking_number": lambda: f"TRK{random.randint(1000000000, 9999999999)}",
    }
}

def get_domain_context(columns):
    """Determine the domain context based on column names"""
    column_str = " ".join([col.lower() for col in columns])
    
    # Check for exact domain matches first (more specific)
    if "employee_id" in column_str or ("department" in column_str and "position" in column_str and "salary" in column_str):
        return "employee"
    elif "product_id" in column_str or ("product_name" in column_str and "stock_quantity" in column_str):
        return "product"
    elif "customer_id" in column_str or ("total_spent" in column_str and "registration_date" in column_str):
        return "customer"
    elif "order_id" in column_str or ("order_date" in column_str and "shipping_date" in column_str):
        return "order"
    
    # Fallback to keyword counting
    for domain, generators in DOMAIN_SPECIFIC_GENERATORS.items():
        domain_keywords = list(generators.keys())
        matches = sum(1 for keyword in domain_keywords if keyword in column_str)
        
        if matches >= 3:
            return domain
    
    return None

def generate_rows(columns: list[str], count: int) -> list[dict]:
    """Generate specified number of rows with given columns."""
    domain = get_domain_context(columns)
    
    return [
        {column: generate_value(column, domain) for column in columns}
        for _ in range(count)
    ]

def generate_value(column: str, domain: str = None):
    """Generate a single value for a column, optionally using domain-specific generators."""
    col = column.lower()
    
    # ---------- DOMAIN-SPECIFIC GENERATION ----------
    if domain and domain in DOMAIN_SPECIFIC_GENERATORS:
        domain_generators = DOMAIN_SPECIFIC_GENERATORS[domain]
        if col in domain_generators:
            return domain_generators[col]()

    # ---------- IDENTIFIERS ----------
    if col == "id" or col.endswith("_id"):
        return random.randint(1, 1_000_000)

    # ---------- NAMES ----------
    if "name" in col:
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
    if "url" in col or "link" in col or "website" in col:
        return fake.url()

    if "ip" in col:
        return fake.ipv4()

    # ---------- BASIC FALLBACK ----------
    return fake.word()

def generate_row(columns: list[str]) -> dict:
    """
    Generate a single row of data.
    """
    return {col: generate_value(col) for col in columns}