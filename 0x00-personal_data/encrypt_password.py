#!/usr/bin/env python3
"""
Password hashing
"""

import bcrypt
def hash_password(password: str) -> str:
    """ 
    Hshing passwords
    """
    
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed
