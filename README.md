***SQLAlchemy starting point***

**What work was done with alembic:**    
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


**How use it:**   
1. Copy repository:   
```git clone https://github.com/leggongum/sqlalchemy_starting_point.git```
2. Download requirements:
```
cd sqlalchemy_starting_point
virtualenv venv
```
Activate venv for Windows: ```venv\scripts\activate```   
For Linux: ```. venv/bin/activate```   
```pip install requirements.txt```    
3. Create .env file and fill it with your db params (You can skip this step to use sqlite db)   
4. Create your models into src/models.py   
5. Create alembic revision:   
```alembic revision --autogenerate```   
6. Use revision:   
```alembic upgrade head```   
