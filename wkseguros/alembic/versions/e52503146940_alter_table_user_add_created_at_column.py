"""alter_table_user_add_created_at_column

Revision ID: e52503146940
Revises: 4a63c3f12ad8
Create Date: 2024-10-10 21:34:24.855456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime, timezone


# revision identifiers, used by Alembic.
revision: str = 'e52503146940'
down_revision: Union[str, None] = '4a63c3f12ad8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Adiciona nova coluna na tabela users
    op.add_column(
        "user", sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False, 
            default=lambda: datetime.now(timezone.utc), 
            onupdate=lambda: datetime.now(timezone.utc)),
        )


def downgrade() -> None:
    op.drop_column("user", "created_at")
