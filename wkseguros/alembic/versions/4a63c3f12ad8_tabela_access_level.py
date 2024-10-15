"""tabela access_level

Revision ID: 4a63c3f12ad8
Revises: 3216507d2044
Create Date: 2024-10-10 21:16:47.159282

"""

from datetime import datetime, timezone
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '4a63c3f12ad8'
down_revision: Union[str, None] = '3216507d2044'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'access_level',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime,
            default=lambda: datetime.now(timezone.utc),
            onupdate=lambda: datetime.now(timezone.utc),
        ),
    )


def downgrade() -> None:
    op.drop_table('access_level')
