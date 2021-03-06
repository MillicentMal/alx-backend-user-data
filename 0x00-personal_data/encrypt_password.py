#!/usr/bin/env python3
"""
Password hashing
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hshing passwords
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
  checks if hashed password unhashed is equal to a string password
    """
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False
