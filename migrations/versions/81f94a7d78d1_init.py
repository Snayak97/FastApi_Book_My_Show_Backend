"""init

Revision ID: 81f94a7d78d1
Revises: 1a4a3297c625
Create Date: 2025-02-23 11:42:44.525723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from src.models import Base


# revision identifiers, used by Alembic.
revision: str = '81f94a7d78d1'
down_revision: Union[str, None] = '1a4a3297c625'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
