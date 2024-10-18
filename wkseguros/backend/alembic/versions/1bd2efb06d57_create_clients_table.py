"""create clients table

Revision ID: 1bd2efb06d57
Revises:
Create Date: 2024-10-17 16:43:58.651636

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1bd2efb06d57'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'clients',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, unique=True, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('cpf', sa.String(11), unique=True, nullable=False),
        sa.Column('born_date', sa.Date, nullable=False),
        sa.Column('address', sa.String(100), nullable=False),
        sa.Column('email', sa.String, unique=True, nullable=False),
        sa.Column('phone', sa.String(11), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('clients')
