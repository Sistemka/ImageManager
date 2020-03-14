import os

from dotenv import load_dotenv

from settings.paths import BASE_DIR

load_dotenv(
    os.path.join(BASE_DIR, 'settings', 'env')
)

MONGO_CONN = {
    'host': os.environ.get('MONGO_HOST', 'localhost'),
    'port': os.environ.get('MONGO_PORT', 27017),
}

MONGO_DB = os.environ.get('MONGO_DB', 'parsed_data')
