#!/usr/bin/python3
"""
   This module holds the class definition of Base which all
   other classes inherit (extend) from

"""
import uuid
import models
from datetime import datetime


class BaseModel():
    """
       class BaseModel act as a base class
       and holds common class level attributes and methods
       shared among all other classes and their objects
    """
    def __init__(self, *args, **kwrgs):
        """
           Initialize Newly Created objects
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
           Return Custom String Representation Of An Object

        """

    return ('Id: ({})\n First_name: [{}]\n Last_name: [{]]\n'.format(
        self.id, self.first_name, self.last_name))
