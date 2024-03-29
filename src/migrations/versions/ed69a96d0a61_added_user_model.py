"""Added User model

Revision ID: 4b89c77c1968
Revises: f568621ad631
Create Date: 2021-12-15 13:21:12.096739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed69a96d0a61'
down_revision = 'f568621ad631'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('google_id', sa.String(length=64), nullable=True),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=1024), nullable=False),
    sa.Column('picture', sa.Text(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_google_id'), 'user', ['google_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_google_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
