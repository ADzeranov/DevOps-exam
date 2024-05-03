#!/exam/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "prod/Desktop/DevOps-exam/forum/app/")
from app import app as application
application.secret_key = 'sec'
