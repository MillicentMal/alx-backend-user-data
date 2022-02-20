#!/usr/bin/env python3
""" 
Auth class
"""

from typing import List, TypeVar
from flask import request

class Auth:
    """ 
    Documenting Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        to be handled
        """
        if path == None or not excluded_paths:
            return True
        for i in excluded_paths:
            if i.endswith('*') and path.startswith(i[:1]):
                return True
            elif i in {path, path + '/'}:
                return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        checks for authorization header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        to be handled
        """
        return None
        