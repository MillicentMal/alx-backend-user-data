#!/usr/bin/python3
""" 
Auth class
"""

from typing import List, TypeVar
from flask import Flask

class Auth:
    def __init__(self):
        return self

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        to be handled
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        to be handled
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        to be handled
        """
        return None
        