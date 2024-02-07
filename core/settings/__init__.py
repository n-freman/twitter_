from .base import *
import os

if os.environ.get("ENV_TYPE") == 'PROD':
    from .prod import *
elif os.environ.get("ENV_TYPE") == 'DEV':
    from .dev import *

