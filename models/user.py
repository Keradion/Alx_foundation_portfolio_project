#!/usr/bin/python3
"""
   This module contains the definition of class User

"""

import models


class User(BaseModel):
    """
       Class User Holds Basic Attributes And Methods
       To Work With User Object

    """
    first_name = ""
    middle_name = ""
    last_name = ""
    gender = ""
    age = 0
    city = ""
    country = ""
    phone_number = ""
