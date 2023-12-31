"""remove extra rooms columns

Revision ID: 7fd1eebc4984
Revises: 07548c762ed4
Create Date: 2023-11-16 22:59:09.386630

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7fd1eebc4984"
down_revision: Union[str, None] = "07548c762ed4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "bookings",
        "price",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=2),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    op.alter_column(
        "hotels",
        "rating",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=1),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    op.alter_column(
        "rooms",
        "price",
        existing_type=sa.REAL(),
        type_=sa.Float(precision=2),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    op.drop_column("rooms", "rating")
    op.drop_column("rooms", "city")
    op.drop_column("rooms", "rooms_quantity")
    op.drop_column("rooms", "country")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "rooms", sa.Column("country", sa.VARCHAR(), autoincrement=False, nullable=False)
    )
    op.add_column(
        "rooms",
        sa.Column("rooms_quantity", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "rooms", sa.Column("city", sa.VARCHAR(), autoincrement=False, nullable=False)
    )
    op.add_column(
        "rooms",
        sa.Column(
            "rating",
            sa.REAL(),
            server_default=sa.text("'0'::real"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.alter_column(
        "rooms",
        "price",
        existing_type=sa.Float(precision=2),
        type_=sa.REAL(),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    op.alter_column(
        "hotels",
        "rating",
        existing_type=sa.Float(precision=1),
        type_=sa.REAL(),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    op.alter_column(
        "bookings",
        "price",
        existing_type=sa.Float(precision=2),
        type_=sa.REAL(),
        existing_nullable=False,
        existing_server_default=sa.text("'0'::real"),
    )
    # ### end Alembic commands ###
