import os
import logging

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from gpgBackup.models import BackupDetail
from gpgBackup.settings import DEBUG, DATABASE_URI, APP_DIR, GPG_KEY, \
    BACKUP_DETAILS, DB_FILE, OUT_DIR


class Backup():


    def __init__(self):

        self.engine = self.get_engine()
        self.base = Base
        self.session = self.get_session(Base, self.engine)

        self.logger = logging.getLogger('gpgBackup')
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
        stream_handler = logging.StreamHandler(stream=sys.stdout)
        stream_handler.setFormatter(formatter)
        if DEBUG:
            stream_handler.setLevel(logging.DEBUG)
            self.logger.setLevel(logging.DEBUG)
        else:
            stream_handler.setLevel(logging.INFO)
            self.logger.setLevel(logging.INFO)
        self.logger.addHandler(stream_handler)

        if os.path.exists(DB_FILE) is False:
            self.create_db()


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


    def run_backup(self):

        for backup_source in BACKUP_DETAILS:

            if os.path.isdir(backup_source):
                pass

            elif os.path.isfile(backup_source):
                pass
