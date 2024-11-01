from sqlalchemy import Column, Integer, String, Numeric

from wkseguros.config.database import Base


class InsuranceType(Base):
    __tablename__ = 'insurance_type'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    standart_coverage_value = Column(Numeric(10,2), nullable=False)