import os

from dotenv import load_dotenv
from split_settings.tools import include


load_dotenv()

include(
    'common.py',
    'local.py'
)

if 'development' in os.environ.get('DJANGO_ENV', ''):
    include('development.py')
elif 'production' in os.environ.get('DJANGO_ENV', ''):
    include('production.py')
print('None')
