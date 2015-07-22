"""
 Our basic database model for keeping track of last backed up datetime.
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BackupDetail(Base):

    id = Column(Integer, autoincrement=True, primary_key=True)
    file_path = Column(String(255))
    last_backup = Column(DateTime)
