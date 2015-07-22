import os

__VERSION__ = '0.1'

DEBUG = True

APP_DIR = os.path.join(os.path.expanduser('~'), '.gpg_backup/')
if os.path.exists(APP_DIR) is False:
    os.mkdir(APP_DIR)

DATABASE_URI = 'sqlite:///' + os.path.join(APP_DIR, 'backups.db')

GPG_KEY = 'AEASDASD'

BACKUP_DETAILS = [
                  '/home/file',
                 ]

# Loading it from the user's directory here so it overwrites the defaults
if os.path.exists(os.path.join(APP_DIR, 'settings.py'):
    sys.path.append(APP_DIR)
    from settings import *
