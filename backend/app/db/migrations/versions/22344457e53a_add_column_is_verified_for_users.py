"""Add column is_verified for users


Revision ID: 22344457e53a
Revises: fdf8821871d7
Create Date: 2023-03-03 17:40:58.197167

"""
from alembic import op
import sqlalchemy as sa


revision = '22344457e53a'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('is_verified', sa.Boolean,
                  nullable=False, server_default="false"))


def downgrade() -> None:
    op.drop_column('users', 'is_verified')
