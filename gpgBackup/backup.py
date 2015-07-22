
import logging

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from gpgBackup.models import BackupDetail

class Backup():


    def __init__(self):

        self.engine = self.get_engine()
        self.base = Base
        self.session = self.get_session(Base, self.engine)

        self.logger = logging.getLogger('gpgBackup')


    def get_engine(self):

        return create_engine(DATABASE_URI)


    def get_session(self, base, engine):

        Session = sessionmaker()
        Session.configure(bind=engine)
        base.metadata.create_all(engine)

        return Session()


    def create_db(self):

        self.base.metadata.create_all(self.engine)


    def delete_db(self):

        self.base.metadata.drop_all(self.engine)
