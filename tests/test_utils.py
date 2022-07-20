import pytest


def test_is_web_url():
    """
    is_web_url() should return True for HTTP and HTTPS URL schemes only.
    """
    from pyattck.utils.utils import is_web_url
    assert is_web_url('/') == False
    assert is_web_url('/etc/passwd') == False
    assert is_web_url('file:///etc/passwd') == False
    assert is_web_url('ftp:///example.com') == False
    assert is_web_url('http:///example.com') == True
    assert is_web_url('https:///example.com') == True
