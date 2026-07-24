import sys
import os
# Add the 'backend' directory to Python's module search path
#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import engine, Base
from database import models

def init_database():
    print("Creating tables...")

    Base.metadata.create_all(engine)

    print("Done!")