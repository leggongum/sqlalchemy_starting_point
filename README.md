***SQLAlchemy starting point***

What work was done with alembic:    
1. Initialization:   
   ```alembic init -t async migrations```
   
2. migrations/env.py has been adjusted; add code:
```
import sys
sys.path = ['', 'src'] + sys.path[1:]

from config import settings
from models import Base

section = config.config_ini_section
config.set_section_option(section, 'DB_URL', settings.DB_URL_POSTGRES if settings.DB_MODE == 'prod' else settings.DB_URL_SQLite)

target_metadata = Base.metadata
```

3. alembic.ini has been adjusted; change sqlalchemy.url:
```sqlalchemy.url = %(DB_URL)s```
