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
        if path == None or (len(excluded_paths) == 0 or excluded_paths == None):
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return True
        if path in excluded_paths:
            return False
        else:
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
        