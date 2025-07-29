import re

STATES = {
    'alabama': 'AL', 'alaska': 'AK', 'arizona': 'AZ', 'arkansas': 'AR', 
    'california': 'CA', 'colorado': 'CO', 'connecticut': 'CT', 'delaware': 'DE', 
    'florida': 'FL', 'georgia': 'GA', 'hawaii': 'HI', 'idaho': 'ID', 
    'illinois': 'IL', 'indiana': 'IN', 'iowa': 'IA', 'kansas': 'KS', 
    'kentucky': 'KY', 'louisiana': 'LA', 'maine': 'ME', 'maryland': 'MD', 
    'massachusetts': 'MA', 'michigan': 'MI', 'minnesota': 'MN', 'mississippi': 'MS', 
    'missouri': 'MO', 'montana': 'MT', 'nebraska': 'NE', 'nevada': 'NV', 
    'new hampshire': 'NH', 'new jersey': 'NJ', 'new mexico': 'NM', 'new york': 'NY', 
    'north carolina': 'NC', 'north dakota': 'ND', 'ohio': 'OH', 'oklahoma': 'OK', 
    'oregon': 'OR', 'pennsylvania': 'PA', 'rhode island': 'RI', 'south carolina': 'SC', 
    'south dakota': 'SD', 'tennessee': 'TN', 'texas': 'TX', 'utah': 'UT', 
    'vermont': 'VT', 'virginia': 'VA', 'washington': 'WA', 'west virginia': 'WV', 
    'wisconsin': 'WI', 'wyoming': 'WY'
}
STATE_MAP = {k: v for k, v in STATES.items()}
for k, v in STATES.items():
    STATE_MAP[v.lower()] = v

ALL_STATE_NAMES = sorted(STATE_MAP.keys(), key=len, reverse=True)
STATE_PATTERN = r'(' + '|'.join(re.escape(s) for s in ALL_STATE_NAMES) + r')'
ZIP_CODE_PATTERN = r'(\d{5})'

def parse_location_text(text: str) -> dict | None:
    if not text:
        return None
    
    text = text.strip()
    
    # ^ - початок рядка, $ - кінець рядка. Це гарантує, що ми аналізуємо весь рядок.
    patterns = [
        # City, State ZIP: Houston, TX 77077 | Houston, 77077 TX
        re.compile(r"^(?P<city>.+?),\s*(?P<zip_code>" + ZIP_CODE_PATTERN + r")\s+(?P<state>" + STATE_PATTERN + r")$", re.IGNORECASE),
        re.compile(r"^(?P<city>.+?),\s*(?P<state>" + STATE_PATTERN + r")[, ]*\s*(?P<zip_code>" + ZIP_CODE_PATTERN + r")$", re.IGNORECASE),
        
        # City State ZIP: Houston TX 77077
        re.compile(r"^(?P<city>.+?)\s+(?P<state>" + STATE_PATTERN + r")\s+(?P<zip_code>" + ZIP_CODE_PATTERN + r")$", re.IGNORECASE),
        
        # ZIP City, State: 77077 Houston, TX
        re.compile(r"^(?P<zip_code>" + ZIP_CODE_PATTERN + r")\s+(?P<city>.+?),\s*(?P<state>" + STATE_PATTERN + r")$", re.IGNORECASE),
        
        # City, State: New York, NY
        re.compile(r"^(?P<city>.+?),\s*(?P<state>" + STATE_PATTERN + r")$", re.IGNORECASE),
        
        # State, ZIP: TX, 77077
        re.compile(r"^(?P<state>" + STATE_PATTERN + r")[, ]+\s*(?P<zip_code>" + ZIP_CODE_PATTERN + r")$", re.IGNORECASE),
        
        # ZIP, State: 77077, TX
        re.compile(r"^(?P<zip_code>" + ZIP_CODE_PATTERN + r")[, ]+\s*(?P<state>" + STATE_PATTERN + r")$", re.IGNORECASE),

        # City ZIP: Houston, 77077
        re.compile(r"^(?P<city>.+?)[, ]+\s*(?P<zip_code>" + ZIP_CODE_PATTERN + r")$", re.IGNORECASE),
        
        # ZIP City: 77077, Houston
        re.compile(r"^(?P<zip_code>" + ZIP_CODE_PATTERN + r")[, ]+\s*(?P<city>.+)$", re.IGNORECASE),
        
        # State City: Texas Houston | TX, Houston
        re.compile(r"^(?P<state>" + STATE_PATTERN + r")[, ]+\s*(?P<city>.+)$", re.IGNORECASE),
        
        # City State: Houston Texas
        re.compile(r"^(?P<city>.+?)\s+(?P<state>" + STATE_PATTERN + r")$", re.IGNORECASE),
        
        # ZIP only: 77077
        re.compile(r"^\s*(?P<zip_code>" + ZIP_CODE_PATTERN + r")\s*$", re.IGNORECASE),
    ]

    for pattern in patterns:
        match = pattern.match(text)
        if match:
            data = {key: (value.strip() if value else None) for key, value in match.groupdict().items()}
            
            city = data.get('city')
            if city: city = city.strip().replace(',', '').title()

            state = data.get('state')
            if state: state = STATE_MAP.get(state.lower(), state.upper())

            zip_code = data.get('zip_code')

            return {"city": city, "state": state, "zip_code": zip_code}
            
    return None