import pytest
from phishing_detector.url_analyzer import validate_url

def test_valid_url():
    url = "https://www.example.org"
    is_valid, message, parsed = validate_url(url)
    assert is_valid is True
    assert message == "valid URL"
    assert parsed["scheme"] == "https"
    assert parsed["subdomain"] == "www"
    assert parsed["domain"] == "example.org"
    
def test_valid_url_with_subdomain_and_path():
    url = "https://sub.example.org/path"
    is_valid, message, parsed = validate_url(url)
    assert is_valid is True
    assert message == "valid URL"
    assert parsed["scheme"] == "https"
    assert parsed["subdomain"] == "sub"
    assert parsed["domain"] == "example.org"
    assert parsed["path"] == "/path"
    
def test_invalid_url():
    url = "invalide-url"
    is_valid, message, parsed = validate_url(url)
    assert is_valid is False
    assert message == "invalid URL"
    assert parsed is None
    
def test_url_missing_scheme():
    url = "example.org"
    is_valid, message, parsed = validate_url(url)
    assert is_valid is False
    assert message == "invalid URL"
    assert parsed is None
    
def test_valid_ftp_url():
    url = "ftp://example.org"
    is_valid, message, parsed = validate_url(url)
    assert is_valid is True
    assert message == "valid URL"
    assert parsed["scheme"] == "ftp"
    assert parsed["subdomain"] == ""
    assert parsed["domain"] == "example.org"
    
def test_invalid_url_with_query():
    url = "https://example.org?query"
    is_valid, message, parsed = validate_url(url)
    assert is_valid is True
    assert message == "valid URL"
    assert parsed["scheme"] == "https"
    assert parsed["subdomain"] == ""
    assert parsed["domain"] == "example.org"
    assert parsed["query"] == "query"