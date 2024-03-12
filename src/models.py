from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from datetime import datetime

from db import Base

class SomeClassBasedTable(Base):
    __tablename__ = 'table_name'

    id: Mapped[int] = mapped_column(primary_key=True)

    ... # other table attributes

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_onupdate=func.now())
