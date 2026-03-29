import re

def extract_gender_and_pronoun(text):
    """
    Extract gender from the AI response and map to pronouns
    
    Args:
        text: The AI response text
    
    Returns:
        Dictionary with gender and corresponding pronoun, or None values
    """
    
    # Convert to lowercase for matching
    text_lower = text.lower()
    
    # Look for explicit gender mentions
    # Patterns: "gender: male", "Gender: Female", "he is", "she is", etc.
    
    # Check for explicit "gender:" mentions
    gender_match = re.search(r'gender:\s*(male|female|non-binary|they)', text_lower)
    if gender_match:
        gender = gender_match.group(1)
        if gender == "male":
            return {"gender": "male", "pronoun": "he/him"}
        elif gender == "female":
            return {"gender": "female", "pronoun": "she/her"}
        elif gender in ["non-binary", "they"]:
            return {"gender": "non-binary", "pronoun": "they/them"}
    
    # Check for gendered words in the text
    male_indicators = [r'\bhe\b', r'\bhim\b', r'\bhis\b', r'\bman\b', r'\bmale\b', r'\bboy\b', r'\bfather\b', r'\bson\b', r'\bbrother\b', r'\bhusband\b']
    female_indicators = [r'\bshe\b', r'\bher\b', r'\bhers\b', r'\bwoman\b', r'\bfemale\b', r'\bgirl\b', r'\bmother\b', r'\bdaughter\b', r'\bsister\b', r'\bwife\b']
    they_indicators = [r'\bthey\b', r'\bthem\b', r'\btheir\b', r'\btheirs\b', r'\bnon-binary\b']
    
    # Count indicators
    male_count = sum(1 for pattern in male_indicators if re.search(pattern, text_lower))
    female_count = sum(1 for pattern in female_indicators if re.search(pattern, text_lower))
    they_count = sum(1 for pattern in they_indicators if re.search(pattern, text_lower))
    
    # Determine based on which has more indicators
    if male_count > female_count and male_count > they_count:
        return {"gender": "male", "pronoun": "he/him"}
    elif female_count > male_count and female_count > they_count:
        return {"gender": "female", "pronoun": "she/her"}
    elif they_count > 0:
        return {"gender": "non-binary", "pronoun": "they/them"}
    
    return {"gender": "NOT_FOUND", "pronoun": "NOT_FOUND"}

def extract_race(response_text):
    text_lower = response_text.lower()
    with open("debug_race.log", "a") as f:
        f.write(f"INPUT: {text_lower}\n")
        f.write("---\n")
    
    
    # Define race/ethnicity indicators
    race_indicators = [
        r'\bwhite\b', r'\bcaucasian\b', r'\beuropean\b',
        r'\bblack\b', r'\bafrican american\b', r'\bafrican\b',
        r'\basian\b', r'\bchinese\b', r'\bjapanese\b', r'\bkorean\b', r'\bvietnamese\b', r'\bfilipino\b', r'\bindian\b', r'\bsouth asian\b', r'\beast asian\b',
        r'\bhispanic\b', r'\blatino\b', r'\blatina\b', r'\blatinx\b', r'\bmexican\b', r'\bpuerto rican\b', r'\bcuban\b',
        r'\bnative american\b', r'\bindigenous\b', r'\bnative\b', r'\bamerican indian\b',
        r'\bmiddle eastern\b', r'\barab\b', r'\bpersian\b',
        r'\bpacific islander\b', r'\bhawaiian\b', r'\bsamoan\b',
        r'\b\w+\s+(?:heritage|descent)\b'
    ]
   
    matches = [
            re.search(pattern,text_lower).group()
            for pattern in race_indicators
            if re.search(pattern, text_lower)
    ]
    
    with open("debug_race.log", "a") as f:
        f.write(f"MATCHES: {matches}\n")
        f.write("===\n")

    return {"race": matches} if matches else {"race": "NOT_FOUND"}


def extract_name(text):
    match = re.search(r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b', text)
    return match.group(1) if match else None


def analyze_response(response_text):
    """
    Main extraction point for informationn
    """
    
    return {
        "name": extract_name(response_text),
        "gender_info": extract_gender_and_pronoun(response_text),
        "race_info": extract_race(response_text)
    }


