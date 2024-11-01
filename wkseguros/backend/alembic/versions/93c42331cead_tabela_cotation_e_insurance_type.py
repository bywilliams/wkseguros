"""Tabela cotation e insurance_type

Revision ID: 93c42331cead
Revises: 1bd2efb06d57
Create Date: 2024-11-01 14:10:58.734852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93c42331cead'
down_revision: Union[str, None] = '1bd2efb06d57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'insurance_types',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('standard_coverage_value', sa.Numeric(10,2), nullable=False)
    )
    op.create_table(
        'cotation_status',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, unique=True, nullable=False)
    )
    op.create_table(
        'cotation',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('cotation_date', sa.TIMESTAMP, nullable=False),
        sa.Column('cotation_value', sa.Numeric(10,2), nullable=False),
        sa.Column('details', sa.Text, nullable=True),
        sa.Column('validation_date', sa.DateTime, nullable=False),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('clients.id'), nullable=False),
        sa.Column('cotation_status_id', sa.Integer, sa.ForeignKey('cotation_status.id'), nullable=False),
        sa.Column('insurance_type_id', sa.Integer, sa.ForeignKey('insurance_types.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('cotation')
    op.drop_table('cotation_status')
    op.drop_table('insurance_types')
