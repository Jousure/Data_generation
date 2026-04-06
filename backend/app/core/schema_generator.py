"""
Enhanced schema generator with intelligent data type mapping
"""

import re
from typing import List, Dict, Any
from .data_types import get_supported_data_types

# Comprehensive data type mapping based on user descriptions
DATA_TYPE_MAPPING = {
    # Location & Address
    "address": ["Address Line 2", "Street Address", "Street Name", "Street Number", "Street Suffix"],
    "city": ["City"],
    "country": ["Country", "Country Code"],
    "postal": ["Postal Code", "State", "State (abbrev)"],
    "airport": ["Airport Code", "Airport Continent", "Airport Country Code", "Airport Elevation (Feet)", 
               "Airport GPS Code", "Airport Latitude", "Airport Longitude", "Airport Municipality", 
               "Airport Name", "Airport Region Code"],
    "coordinates": ["Latitude", "Longitude"],
    "timezone": ["Time Zone"],
    
    # Person & Demographics
    "name": ["First Name", "Last Name", "Full Name", "First Name (Female)", "First Name (Male)", 
             "First Name (European)", "Family Name (Chinese)", "Given Name (Chinese)"],
    "gender": ["Gender", "Gender (abbrev)", "Gender (Binary)", "Gender (Facebook)"],
    "title": ["Title", "Job Title"],
    "username": ["Username"],
    "race": ["Race"],
    "animal": ["Animal Common Name", "Animal Scientific Name"],
    
    # Business & Finance
    "company": ["Company Name", "Fake Company Name", "Bank Name", "Bank City", "Bank State", 
               "Bank Street Address", "Bank Country Code"],
    "bank": ["Bank LEI", "Bank RIAD Code", "Bank Routing Number", "Bank SWIFT BIC"],
    "credit": ["Credit Card #", "Credit Card Type"],
    "currency": ["Currency", "Currency Code", "Money"],
    "stock": ["Stock Industry", "Stock Market", "Stock Market Cap", "Stock Name", 
               "Stock Sector", "Stock Symbol"],
    "department": ["Department (Corporate)", "Department (Retail)"],
    "identification": ["DUNS Number", "EIN"],
    
    # Technology & Digital
    "app": ["App Bundle ID", "App Name", "App Version"],
    "crypto": ["Bitcoin Address", "Ethereum Address", "Tezos Account", "Tezos Block", 
               "Tezos Contract", "Tezos Operation", "Tezos Signature"],
    "network": ["Domain Name", "IP Address v4", "IP Address v4 CIDR", "IP Address v6", 
                "IP Address v6 CIDR", "MAC Address", "URL", "User Agent"],
    "hash": ["MD5", "SHA1", "SHA256"],
    "device": ["Mobile Device Brand", "Mobile Device Model", "Mobile Device OS", "Mobile Device Release Date"],
    "mime": ["MIME Type"],
    "avatar": ["Avatar"],
    
    # Automotive
    "car": ["Car Make", "Car Model", "Car Model Year", "Car VIN"],
    
    # Healthcare & Medical
    "drug": ["Drug Company", "Drug Name (Brand)", "Drug Name (Generic)", "FDA NDC Code"],
    "hospital": ["Hospital City", "Hospital Name", "Hospital NPI", "Hospital Postal Code", 
                "Hospital State", "Hospital Street Address"],
    "medical": ["ICD10 Diagnosis Code", "ICD10 Dx Desc (Long)", "ICD10 Dx Desc (Short)",
                "ICD10 Proc Desc (Long)", "ICD10 Proc Desc (Short)", "ICD10 Procedure Code",
                "ICD9 Diagnosis Code", "ICD9 Dx Desc (Long)", "ICD9 Dx Desc (Short)",
                "ICD9 Proc Desc (Long)", "ICD9 Proc Desc (Short)", "ICD9 Procedure Code",
                "Medicare Beneficiary ID", "NHS Number"],
    
    # Construction
    "construction": ["Construction Heavy Equipment", "Construction Material", "Construction Role",
                   "Construction Standard Cost Code", "Construction Subcontract Category", "Construction Trade"],
    
    # Entertainment & Media
    "movie": ["Movie Genres", "Movie Title"],
    
    # Food & Grocery
    "grocery": ["Product (Grocery)"],
    
    # Products & Retail
    "product": ["Product Category", "Product Description", "Product Name", "Product Price", 
                "Product Subcategory", "Shirt Size"],
    
    # Identification Numbers
    "id": ["GUID", "ISBN", "MongoDB ObjectID", "SSN", "ULID"],
    
    # Aviation
    "flight": ["Flight Airline Code", "Flight Airline Name", "Flight Arrival Airport", 
               "Flight Arrival Airport Code", "Flight Arrival City", "Flight Arrival Country",
               "Flight Departure Airport", "Flight Departure Airport Code", "Flight Departure City", 
               "Flight Departure Country", "Flight Departure Time", "Flight Duration (Hours)", 
               "Flight Number"],
    
    # Education
    "education": ["University"],
    
    # Professional Skills
    "skills": ["LinkedIn Skill"],
    
    # Nature & Biology
    "nature": ["Plant Common Name", "Plant Family", "Plant Scientific Name"],
    
    # Data & Programming
    "data": ["Base64 Image URL", "Blank", "Boolean", "Character Sequence", "Color",
             "Custom List", "Dataset Column", "Digit Sequence", "Dummy Image URL", 
             "Encrypt", "File Name", "Formula", "JSON Array", "Number", 
             "Regular Expression", "Repeating Element", "Row Number", "Scenario", 
             "Sequence", "SQL Expression", "Template", "Top Level Domain"],
    
    # Text & Content
    "text": ["Buzzword", "Catch Phrase", "Email Address", "Frequency", "HCPCS Code", 
              "HCPCS Name", "Hex Color", "Language", "Language Code", "Nato Phonetic",
              "Naughty String", "Paragraphs", "Password", "Password Hash", 
              "Sentences", "Short Hex Color", "Slogan", "Words"],
    
    # Statistical Distributions
    "statistics": ["Binomial Distribution", "Exponential Distribution", "Geometric Distribution",
                  "Normal Distribution", "Poisson Distribution"],
    
    # Dates & Times
    "datetime": ["Datetime", "Time"]
}

def extract_keywords_from_description(description: str) -> List[str]:
    """Extract relevant keywords from user description"""
    keywords = []
    description_lower = description.lower()
    
    # Extract common patterns
    patterns = {
        r'\b(customer|clients?|users?|accounts?)\b': 'customer',
        r'\b(product|item|goods?|merchandise)\b': 'product',
        r'\b(employee|staff|worker|personnel)\b': 'employee',
        r'\b(order|purchase|sale|transaction)\b': 'order',
        r'\b(address|location|place|venue)\b': 'address',
        r'\b(contact|phone|email)\b': 'contact',
        r'\b(flight|airport|airline|travel)\b': 'flight',
        r'\b(hospital|medical|health|patient|doctor)\b': 'medical',
        r'\b(bank|finance|money|payment|credit)\b': 'finance',
        r'\b(car|vehicle|automotive|vin)\b': 'car',
        r'\b(company|business|corporation)\b': 'company',
        r'\b(student|education|university|school)\b': 'education',
        r'\b(movie|film|cinema|entertainment)\b': 'movie',
        r'\b(animal|plant|nature|biology)\b': 'nature',
        r'\b(drug|medicine|pharmacy|pharmaceutical)\b': 'drug',
        r'\b(construction|building|architecture)\b': 'construction',
        r'\b(app|software|mobile|device)\b': 'app',
        r'\b(crypto|bitcoin|ethereum|blockchain)\b': 'crypto',
        r'\b(network|ip|domain|url|website)\b': 'network',
        r'\b(id|identifier|code|number)\b': 'id',
        r'\b(name|first|last|full|title)\b': 'name',
        r'\b(date|time|datetime|timestamp)\b': 'datetime',
        r'\b(text|content|description|comment)\b': 'text',
        r'\b(number|amount|quantity|count)\b': 'number',
        r'\b(gender|sex|male|female)\b': 'gender'
    }
    
    for pattern, keyword in patterns.items():
        if re.search(pattern, description_lower):
            keywords.append(keyword)
    
    return keywords

def map_column_name_to_data_type(column_name: str, keywords: List[str]) -> str:
    """Map column name to appropriate data type"""
    column_name_lower = column_name.lower()
    
    # Direct keyword matching
    for keyword in keywords:
        if keyword in DATA_TYPE_MAPPING:
            for data_type in DATA_TYPE_MAPPING[keyword]:
                if any(word in column_name_lower for word in data_type.lower().split()):
                    return data_type
    
    # Column name pattern matching
    if any(word in column_name_lower for word in ['name', 'first', 'last', 'full']):
        if 'first' in column_name_lower:
            return "First Name"
        elif 'last' in column_name_lower:
            return "Last Name"
        else:
            return "Full Name"
    
    if any(word in column_name_lower for word in ['email', 'mail']):
        return "Email Address"
    
    if any(word in column_name_lower for word in ['phone', 'tel', 'mobile']):
        return "Phone Number"
    
    if any(word in column_name_lower for word in ['address', 'street', 'city', 'country']):
        if 'street' in column_name_lower:
            return "Street Address"
        elif 'city' in column_name_lower:
            return "City"
        elif 'country' in column_name_lower:
            return "Country"
        else:
            return "Address Line 2"
    
    if any(word in column_name_lower for word in ['date', 'time', 'created', 'updated']):
        return "Datetime"
    
    if any(word in column_name_lower for word in ['id', 'identifier', 'code']):
        return "GUID"
    
    if any(word in column_name_lower for word in ['price', 'cost', 'amount']):
        return "Money"
    
    if any(word in column_name_lower for word in ['description', 'content', 'text']):
        return "Paragraphs"
    
    # Default fallback
    return "Text"

def generate_enhanced_schema(description: str) -> List[Dict[str, Any]]:
    """Generate enhanced schema based on user description with intelligent data type mapping"""
    keywords = extract_keywords_from_description(description)
    
    # Determine domain context
    domain = "general"
    if 'customer' in keywords:
        domain = "customer"
    elif 'product' in keywords:
        domain = "product"
    elif 'employee' in keywords:
        domain = "employee"
    elif 'order' in keywords:
        domain = "order"
    
    # Generate schema based on domain and keywords
    schemas = {
        "customer": [
            {"name": "Customer ID", "type": "GUID"},
            {"name": "First Name", "type": "First Name"},
            {"name": "Last Name", "type": "Last Name"},
            {"name": "Email Address", "type": "Email Address"},
            {"name": "Phone Number", "type": "Phone Number"},
            {"name": "Street Address", "type": "Street Address"},
            {"name": "City", "type": "City"},
            {"name": "State", "type": "State"},
            {"name": "Postal Code", "type": "Postal Code"},
            {"name": "Country", "type": "Country"},
            {"name": "Registration Date", "type": "Datetime"},
            {"name": "Last Purchase Date", "type": "Datetime"},
            {"name": "Total Spent", "type": "Money"},
            {"name": "Membership Level", "type": "Custom List"}
        ],
        "product": [
            {"name": "Product ID", "type": "GUID"},
            {"name": "Product Name", "type": "Product Name"},
            {"name": "Product Description", "type": "Product Description"},
            {"name": "Product Category", "type": "Product Category"},
            {"name": "Product Subcategory", "type": "Product Subcategory"},
            {"name": "Price", "type": "Money"},
            {"name": "Stock Quantity", "type": "Number"},
            {"name": "SKU", "type": "Custom List"},
            {"name": "Brand", "type": "Company Name"},
            {"name": "Supplier", "type": "Company Name"},
            {"name": "Weight", "type": "Number"},
            {"name": "Dimensions", "type": "Text"},
            {"name": "Rating", "type": "Number"},
            {"name": "Reviews Count", "type": "Number"}
        ],
        "employee": [
            {"name": "Employee ID", "type": "GUID"},
            {"name": "First Name", "type": "First Name"},
            {"name": "Last Name", "type": "Last Name"},
            {"name": "Email Address", "type": "Email Address"},
            {"name": "Phone Number", "type": "Phone Number"},
            {"name": "Job Title", "type": "Job Title"},
            {"name": "Department", "type": "Department (Corporate)"},
            {"name": "Hire Date", "type": "Datetime"},
            {"name": "Salary", "type": "Money"},
            {"name": "Manager ID", "type": "GUID"},
            {"name": "Office Location", "type": "Street Address"},
            {"name": "Work Phone", "type": "Phone Number"},
            {"name": "Status", "type": "Custom List"}
        ],
        "order": [
            {"name": "Order ID", "type": "GUID"},
            {"name": "Customer ID", "type": "GUID"},
            {"name": "Order Date", "type": "Datetime"},
            {"name": "Ship Date", "type": "Datetime"},
            {"name": "Delivery Date", "type": "Datetime"},
            {"name": "Order Status", "type": "Custom List"},
            {"name": "Payment Method", "type": "Custom List"},
            {"name": "Subtotal", "type": "Money"},
            {"name": "Tax", "type": "Money"},
            {"name": "Shipping", "type": "Money"},
            {"name": "Total", "type": "Money"},
            {"name": "Shipping Address", "type": "Street Address"},
            {"name": "Billing Address", "type": "Street Address"}
        ],
        "flight": [
            {"name": "Flight Number", "type": "Flight Number"},
            {"name": "Airline Code", "type": "Flight Airline Code"},
            {"name": "Airline Name", "type": "Flight Airline Name"},
            {"name": "Departure Airport", "type": "Flight Departure Airport"},
            {"name": "Departure Airport Code", "type": "Flight Departure Airport Code"},
            {"name": "Departure City", "type": "Flight Departure City"},
            {"name": "Departure Country", "type": "Flight Departure Country"},
            {"name": "Arrival Airport", "type": "Flight Arrival Airport"},
            {"name": "Arrival Airport Code", "type": "Flight Arrival Airport Code"},
            {"name": "Arrival City", "type": "Flight Arrival City"},
            {"name": "Arrival Country", "type": "Flight Arrival Country"},
            {"name": "Departure Time", "type": "Flight Departure Time"},
            {"name": "Duration (Hours)", "type": "Flight Duration (Hours)"},
            {"name": "Aircraft Type", "type": "Custom List"},
            {"name": "Gate Number", "type": "Custom List"}
        ],
        "medical": [
            {"name": "Patient ID", "type": "GUID"},
            {"name": "First Name", "type": "First Name"},
            {"name": "Last Name", "type": "Last Name"},
            {"name": "Date of Birth", "type": "Datetime"},
            {"name": "Gender", "type": "Gender"},
            {"name": "Blood Type", "type": "Custom List"},
            {"name": "Diagnosis Code", "type": "ICD10 Diagnosis Code"},
            {"name": "Diagnosis Description", "type": "ICD10 Dx Desc (Long)"},
            {"name": "Procedure Code", "type": "ICD10 Procedure Code"},
            {"name": "Procedure Description", "type": "ICD10 Proc Desc (Long)"},
            {"name": "Attending Physician", "type": "Full Name"},
            {"name": "Hospital Name", "type": "Hospital Name"},
            {"name": "Admission Date", "type": "Datetime"},
            {"name": "Discharge Date", "type": "Datetime"},
            {"name": "Room Number", "type": "Custom List"},
            {"name": "Insurance Provider", "type": "Company Name"}
        ],
        "finance": [
            {"name": "Account ID", "type": "GUID"},
            {"name": "Account Holder", "type": "Full Name"},
            {"name": "Account Type", "type": "Custom List"},
            {"name": "Bank Name", "type": "Bank Name"},
            {"name": "Bank Address", "type": "Bank Street Address"},
            {"name": "Routing Number", "type": "Bank Routing Number"},
            {"name": "Account Number", "type": "Custom List"},
            {"name": "Balance", "type": "Money"},
            {"name": "Available Balance", "type": "Money"},
            {"name": "Credit Limit", "type": "Money"},
            {"name": "Card Number", "type": "Credit Card #"},
            {"name": "Card Type", "type": "Credit Card Type"},
            {"name": "Expiration Date", "type": "Datetime"},
            {"name": "CVV", "type": "Custom List"}
        ]
    }
    
    # Get the appropriate schema or generate a general one
    if domain in schemas:
        return schemas[domain]
    
    # Generate general schema based on keywords
    general_schema = []
    
    if 'address' in keywords:
        general_schema.extend([
            {"name": "Street Address", "type": "Street Address"},
            {"name": "City", "type": "City"},
            {"name": "State", "type": "State"},
            {"name": "Postal Code", "type": "Postal Code"},
            {"name": "Country", "type": "Country"}
        ])
    
    if 'contact' in keywords:
        general_schema.extend([
            {"name": "First Name", "type": "First Name"},
            {"name": "Last Name", "type": "Last Name"},
            {"name": "Email Address", "type": "Email Address"},
            {"name": "Phone Number", "type": "Phone Number"}
        ])
    
    if 'company' in keywords:
        general_schema.extend([
            {"name": "Company Name", "type": "Company Name"},
            {"name": "Industry", "type": "Custom List"},
            {"name": "Website", "type": "URL"},
            {"name": "Phone", "type": "Phone Number"}
        ])
    
    # If no specific schema, return a basic one
    if not general_schema:
        general_schema = [
            {"name": "ID", "type": "GUID"},
            {"name": "Name", "type": "Full Name"},
            {"name": "Description", "type": "Paragraphs"},
            {"name": "Created Date", "type": "Datetime"},
            {"name": "Status", "type": "Custom List"}
        ]
    
    return general_schema
