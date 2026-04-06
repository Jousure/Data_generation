from fastapi import APIRouter
from app.models.request import SchemaRequest
from openai import OpenAI
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

router = APIRouter()

# Enhanced rule-based schema generator with more patterns
RULE_BASED_SCHEMAS = {
    "customer": ["customer_id", "first_name", "last_name", "email", "phone", "address", "city", "country", "registration_date", "last_purchase_date", "total_spent"],
    "product": ["product_id", "product_name", "category", "price", "stock_quantity", "supplier", "sku", "description", "weight", "brand"],
    "employee": ["employee_id", "first_name", "last_name", "email", "department", "position", "salary", "hire_date", "manager_id", "status"],
    "order": ["order_id", "customer_id", "order_date", "shipping_date", "delivery_date", "status", "total_amount", "payment_method"],
    "student": ["student_id", "first_name", "last_name", "email", "grade", "enrollment_date", "major", "gpa", "credits"],
    "inventory": ["item_id", "item_name", "category", "quantity", "location", "last_updated", "supplier", "cost", "reorder_level"],
    "sales": ["sale_id", "product_id", "customer_id", "sale_date", "quantity", "unit_price", "total_price", "salesperson"],
    "hospital": ["patient_id", "first_name", "last_name", "dob", "admission_date", "discharge_date", "diagnosis", "doctor", "department"],
    "financial": ["transaction_id", "account_id", "transaction_date", "amount", "type", "category", "description", "balance"],
    "user": ["user_id", "username", "email", "first_name", "last_name", "created_at", "last_login", "status", "role"],
    "contact": ["contact_id", "first_name", "last_name", "email", "phone", "company", "position", "created_at"],
    "transaction": ["transaction_id", "date", "amount", "type", "description", "category", "account_id"],
    "booking": ["booking_id", "customer_id", "service", "date", "time", "status", "amount", "created_at"],
    "review": ["review_id", "product_id", "customer_id", "rating", "comment", "date", "verified"],
    "project": ["project_id", "name", "description", "start_date", "end_date", "status", "budget", "manager_id"],
    "task": ["task_id", "project_id", "title", "description", "status", "priority", "due_date", "assignee_id"],
}

@router.post("/")
async def generate_schema(req: SchemaRequest):
    topic = req.prompt.strip().lower()
    
    # Instant rule-based response first
    columns = get_rule_based_schema(topic)
    
    # Return immediately with rule-based schema
    response = {
        "title": req.prompt.strip()[:60] if req.prompt.strip() else "Custom Dataset",
        "columns": columns[:10]  # Limit to 10 columns
    }
    
    # Optional: Try to enhance with OpenAI in background (non-blocking)
    # This won't affect the instant response
    try:
        if os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "sk-test-key":
            # Run OpenAI call in background without blocking response
            asyncio.create_task(enhance_with_openai_background(topic))
    except:
        pass  # Ignore OpenAI errors, we already have instant response
    
    return response

def get_rule_based_schema(topic):
    """Enhanced rule-based schema generation with instant matching"""
    topic = topic.lower()
    
    # Check for exact matches first
    for key, schema in RULE_BASED_SCHEMAS.items():
        if key in topic:
            return schema
    
    # Enhanced keyword matching with priority
    if any(word in topic for word in ["customer", "client", "user", "account"]):
        return RULE_BASED_SCHEMAS["customer"]
    elif any(word in topic for word in ["product", "item", "inventory", "goods"]):
        return RULE_BASED_SCHEMAS["product"]
    elif any(word in topic for word in ["employee", "staff", "worker", "personnel"]):
        return RULE_BASED_SCHEMAS["employee"]
    elif any(word in topic for word in ["order", "sale", "purchase", "transaction"]):
        return RULE_BASED_SCHEMAS["order"]
    elif any(word in topic for word in ["student", "education", "school", "university"]):
        return RULE_BASED_SCHEMAS["student"]
    elif any(word in topic for word in ["hospital", "patient", "medical", "health"]):
        return RULE_BASED_SCHEMAS["hospital"]
    elif any(word in topic for word in ["financial", "money", "payment", "billing"]):
        return RULE_BASED_SCHEMAS["financial"]
    elif any(word in topic for word in ["contact", "lead", "prospect"]):
        return RULE_BASED_SCHEMAS["contact"]
    elif any(word in topic for word in ["booking", "reservation", "appointment"]):
        return RULE_BASED_SCHEMAS["booking"]
    elif any(word in topic for word in ["review", "rating", "feedback"]):
        return RULE_BASED_SCHEMAS["review"]
    elif any(word in topic for word in ["project", "task", "work"]):
        return RULE_BASED_SCHEMAS["project"]
    
    # Generic fallback schemas based on common patterns
    if any(word in topic for word in ["data", "record", "information"]):
        return ["id", "name", "type", "value", "description", "status", "created_at", "updated_at"]
    elif any(word in topic for word in ["list", "directory", "catalog"]):
        return ["id", "name", "category", "description", "url", "status", "created_at"]
    elif any(word in topic for word in ["log", "event", "activity"]):
        return ["id", "event_type", "description", "timestamp", "user_id", "ip_address", "details"]
    
    # Default fallback
    return ["id", "name", "description", "value", "created_at"]

async def enhance_with_openai_background(topic):
    """Background task to enhance schema with OpenAI (optional)"""
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """You are a database schema generator. Based on the user's topic, generate a list of appropriate column names for a dataset. 
                    Return only a JSON array of column names (strings). Make them realistic and relevant to the topic.
                    Examples:
                    - "customer data" -> ["customer_id", "first_name", "last_name", "email", "phone", "address", "city", "country", "registration_date", "last_purchase_date", "total_spent"]
                    - "product inventory" -> ["product_id", "product_name", "category", "price", "stock_quantity", "supplier", "sku", "description", "weight", "dimensions"]
                    - "employee records" -> ["employee_id", "first_name", "last_name", "email", "department", "position", "salary", "hire_date", "manager_id", "status"]"""
                },
                {
                    "role": "user", 
                    "content": f"Generate column names for: {topic}"
                }
            ],
            temperature=0.7,
            max_tokens=300
        )
        
        # This runs in background, doesn't affect response time
        content = response.choices[0].message.content.strip()
        # Could store enhanced schema for future use if needed
        
    except Exception as e:
        # Silently ignore OpenAI errors in background
        pass
