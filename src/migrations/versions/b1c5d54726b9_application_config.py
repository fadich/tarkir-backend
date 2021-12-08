"""Application config

Revision ID: b1c5d54726b9
Revises: 1f7aee558ff2
Create Date: 2021-12-08 10:45:33.320198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1c5d54726b9'
down_revision = '1f7aee558ff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('config',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['application.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('application_id', 'name', name='unique_application_config')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('config')
    op.drop_table('application')
    # ### end Alembic commands ###
