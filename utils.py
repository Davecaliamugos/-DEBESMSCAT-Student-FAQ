def find_best_match(user_input, faq_dict):
    user_input = user_input.lower().strip()
    
    # List of common variations for key terms
    variations = {
        'founding year': ['founding year', 'established', 'when was it founded', 'year established'],
        'school colors': ['school colors', 'colors', 'official colors', 'color'],
        'named after': ['named after', 'who is it named after', 'name origin', 'who is'],
        'school motto': ['school motto', 'motto', 'what is the motto'],
        'mission': ['mission', 'what is the mission'],
        'vision': ['vision', 'what is the vision'],
        'hymn': ['hymn', 'school song', 'alma mater song'],
        'rodeo': ['rodeo', 'rodeo team'],
        'emergency': ['emergency', 'help', 'medical emergency'],
        'peaceful': ['peaceful', 'peace', 'quiet campus', 'serene'],
        'environment': ['environment', 'eco', 'green campus', 'environmental'],
        'nature': ['nature', 'natural', 'scenery', 'land'],
        'enrollment': ['enrollment', 'enroll', 'register', 'admission'],
        'portal': ['portal', 'student portal', 'online portal'],
        'registrar': ['registrar', 'records', 'tor'],
        'grades': ['grades', 'final grades', 'scores', 'results'],
        'clearance': ['clearance', 'signing', 'requirements'],
        'scholarship': ['scholarship', 'financial aid', 'tes', 'scholars'],
        'osas': ['osas', 'student affairs', 'student services'],
        'ssc': ['ssc', 'student council', 'student government'],
        'orgs': ['orgs', 'organizations', 'clubs', 'student orgs'],
        'wifi': ['wifi', 'internet', 'connection', 'network'],
        'ccit': ['ccit', 'computing', 'it college', 'college of computing'],
        'It': ['it', 'industrial technology', 'tech course'],
        'agri': ['agri', 'agriculture', 'farming', 'ioa'],
        'educ': ['educ', 'education', 'teaching', 'ioe'],
        'engineering': ['engineering', 'engg', 'biosystems'],
        'colleges': ['colleges', 'institutes', 'how many colleges'],
        'mandaon': ['mandaon', 'main campus', 'cabitan'],
        'cawayan': ['cawayan', 'cawayan campus'],
        'masbate city': ['masbate city', 'city campus', 'graduate campus'],
        'library': ['library', 'lib', 'study area'],
        'cafeteria': ['cafeteria', 'canteen', 'food', 'meals'],
        'gym': ['gym', 'gymnasium', 'sports', 'basketball'],
        'clinic': ['clinic', 'medical', 'health center', 'infirmary'],
        'security': ['security', 'guards', 'safety', 'main gate'],
        'id': ['id', 'identification', 'school id', 'no id'],
        'uniform': ['uniform', 'dress', 'attire', 'clothing'],
        'dress code': ['dress code', 'clothing rules', 'attire rules'],
        'behavior': ['behavior', 'conduct', 'discipline', 'rules'],
        'smoking': ['smoking', 'cigarette', 'vape', 'smoke'],
        'alcohol': ['alcohol', 'drinking', 'liquor', 'beverage'],
        'haircut': ['haircut', 'hair', 'grooming'],
    }
    
    # Check for variations first
    for key, variants in variations.items():
        for variant in variants:
            if variant in user_input:
                # Find the matching FAQ key
                for faq_key in faq_dict:
                    if key in faq_key.lower():
                        return faq_dict[faq_key]
    
    # Exact match
    if user_input in faq_dict:
        return faq_dict[user_input]

    # Partial match
    for question in faq_dict:
        if user_input in question:
            return faq_dict[question]

    # Keyword-based match
    for question in faq_dict:
        for word in user_input.split():
            if word in question:
                return faq_dict[question]

    return None