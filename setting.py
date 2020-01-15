import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

# load ID and password from .env file
"""
------
|.env|
------
ID   = a0000000
PASS = *************
"""

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
ID = os.environ.get("ID")
PASS = os.environ.get("PASS")
