"""Initial migration tabela User

Revision ID: 3216507d2044
Revises:
Create Date: 2024-10-09 17:30:43.534656

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3216507d2044'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column(
            'username', sa.String, unique=True, index=True, nullable=False
        ),
        sa.Column('email', sa.String, unique=True, index=True, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('access_level', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('user')
