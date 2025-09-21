import pandas as pd
import tldextract
from urllib.parse import urlparse
import re

def extract_url_features(url):
    """
    Extract enhanced numeric features from a URL string.
    Returns a DataFrame with a single row.
    """
    # Initialize features dictionary
    features = {}

    # Basic URL characteristics
    features['URLLength'] = len(url)
    features['IsHTTPS'] = 1 if url.startswith('https') else 0

    # Parse domain and path
    parsed = tldextract.extract(url)
    domain = parsed.domain
    subdomain = parsed.subdomain
    suffix = parsed.suffix
    path = urlparse(url).path

    # Domain features
    features['DomainLength'] = len(domain)
    features['SubdomainLength'] = len(subdomain)
    features['TLDLength'] = len(suffix)
    features['NumSubdomains'] = len(subdomain.split('.')) if subdomain else 0
    features['NumDotsInDomain'] = domain.count('.') + subdomain.count('.') if domain else 0
    features['HyphenCount'] = domain.count('-') + subdomain.count('-')
    features['DigitInDomain'] = int(any(c.isdigit() for c in domain + subdomain))
    features['LongDomain'] = int(len(domain) > 15)
    features['IsDomainIP'] = int(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', domain) is not None)

    # Path features
    features['NumPathSegments'] = path.count('/')
    features['PathLength'] = len(path)

    # Character composition
    letters = sum(c.isalpha() for c in url)
    digits = sum(c.isdigit() for c in url)
    special_chars = sum(c in ['?', '=', '&', '@', '-', '_', '%'] for c in url)

    features['NumLetters'] = letters
    features['LetterRatio'] = letters / len(url) if len(url) > 0 else 0
    features['NumDigits'] = digits
    features['DigitRatio'] = digits / len(url) if len(url) > 0 else 0
    features['NumSpecialChars'] = special_chars
    features['SpecialCharRatio'] = special_chars / len(url) if len(url) > 0 else 0

    # Suspicious keywords in URL
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'bank', 'account', 'pay', 'password']
    features['SuspiciousKeywordCount'] = sum(1 for kw in suspicious_keywords if kw in url.lower())

    # Check for obfuscation characters
    obfuscated_chars = sum(c in ['@', '-', '_'] for c in url)
    features['ObfuscationCount'] = obfuscated_chars
    features['HasObfuscation'] = int(obfuscated_chars > 0)
    features['ObfuscationRatio'] = obfuscated_chars / len(url) if len(url) > 0 else 0

    # Convert to DataFrame
    df_features = pd.DataFrame([features])

    return df_features
