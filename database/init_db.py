from database import engine, Base
import models

print("Creating tables...")

Base.metadata.create_all(engine)

print("Done!")