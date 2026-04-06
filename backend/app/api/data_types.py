"""
API endpoint for data types reference
"""

from fastapi import APIRouter
from typing import List, Dict, Any
from ..core.generator import get_available_data_types

router = APIRouter()

@router.get("/data-types")
async def get_data_types() -> Dict[str, Any]:
    """
    Get all available data types that can be generated
    
    Returns:
        Dictionary with available data types organized by category
    """
    try:
        data_types = get_available_data_types()
        
        # Organize data types by categories for better frontend experience
        categorized_types = {
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
        
        # Simple categorization based on keywords
        for data_type in data_types:
            data_type_lower = data_type.lower()
            
            if any(keyword in data_type_lower for keyword in ["address", "city", "country", "postal", "street", "airport", "latitude", "longitude"]):
                categorized_types["Location & Address"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["name", "gender", "age", "race", "title", "username"]):
                categorized_types["Person & Demographics"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["bank", "credit", "currency", "stock", "money", "company"]):
                categorized_types["Business & Finance"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["app", "domain", "ip", "mac", "url", "email", "bitcoin", "ethereum"]):
                categorized_types["Technology & Digital"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["car", "vin", "make", "model"]):
                categorized_types["Automotive"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["drug", "hospital", "medical", "icd", "nhs"]):
                categorized_types["Healthcare & Medical"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["construction", "masonry", "equipment"]):
                categorized_types["Construction"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["movie", "entertainment"]):
                categorized_types["Entertainment & Media"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["product", "price", "category"]):
                categorized_types["Products & Retail"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["id", "guid", "isbn", "ssn", "ulid"]):
                categorized_types["Identification Numbers"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["flight", "airline", "airport"]):
                categorized_types["Aviation"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["university", "education"]):
                categorized_types["Education"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["plant", "animal"]):
                categorized_types["Nature & Biology"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["json", "file", "base64", "encrypt", "regex"]):
                categorized_types["Data & Programming"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["text", "word", "paragraph", "slogan", "password"]):
                categorized_types["Text & Content"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["distribution", "binomial", "normal", "poisson"]):
                categorized_types["Statistical Distributions"].append(data_type)
            elif any(keyword in data_type_lower for keyword in ["date", "time", "datetime"]):
                categorized_types["Dates & Times"].append(data_type)
            else:
                # Add to first category if no specific match
                categorized_types["Location & Address"].append(data_type)
        
        # Remove empty categories
        categorized_types = {k: v for k, v in categorized_types.items() if v}
        
        return {
            "success": True,
            "data": {
                "categories": categorized_types,
                "total_count": len(data_types),
                "all_types": data_types
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }
