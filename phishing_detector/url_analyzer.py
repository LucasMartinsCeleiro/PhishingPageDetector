from urllib.parse import urlparse
import tldextract

def validate_url(url):
    """
    Validate and parse the URL
    :param url: URL to validate and parse
    :return: A tuple (is_valid, message, parsed_url) where:
        - is_valid: True if the URL is valid, False otherwise
        - message: Explanation of the result
        - parsed_url: The parsed URL if valid, None otherwise
    """
    try:
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return False, "invalid URL", None
        
        extracted = tldextract.extract(url)
        domain = extracted.registered_domain
        subdomain = extracted.subdomain
        
        if not domain:
            return False, "invalid URL", None
        
        return True, "valid URL", {
            "scheme": parsed.scheme,
            "subdomain": subdomain,
            "domain": domain,
            "path": parsed.path,
            "query": parsed.query,
        }
        
    except Exception as e:
        return False, f"Error during the validation of URL {url}: {e}", None