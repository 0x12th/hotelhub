"""format columns

Revision ID: 47b506ff8445
Revises: 7fd1eebc4984
Create Date: 2023-11-17 20:47:51.442906

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "47b506ff8445"
down_revision: Union[str, None] = "7fd1eebc4984"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "bookings",
        "price",
        existing_type=sa.REAL(),
        type_=sa.Integer(),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    op.alter_column(
        "rooms",
        "price",
        existing_type=sa.REAL(),
        type_=sa.Integer(),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "rooms",
        "price",
        existing_type=sa.Integer(),
        type_=sa.REAL(),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    op.alter_column(
        "bookings",
        "price",
        existing_type=sa.Integer(),
        type_=sa.REAL(),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    # ### end Alembic commands ###
