"""Add new column is_verified

Revision ID: 49251043f993
Revises: fdf8821871d7
Create Date: 2023-03-03 19:05:14.465665

"""
from alembic import op
import sqlalchemy as sa


revision = '49251043f993'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users', sa.Column(
            'is_verified',
            sa.Boolean,
            nullable=False,
            server_default="false"
        )
    )


def downgrade() -> None:
    op.drop_column('users', 'is_verified')
