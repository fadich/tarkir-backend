"""Added Passive Bonus ralations

Revision ID: 504843d6b728
Revises: 2482f0618219
Create Date: 2021-12-01 15:43:14.607142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '504843d6b728'
down_revision = '2482f0618219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('passive_bonus',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('name_en', sa.String(length=256), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('cycle', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name_en')
    )
    op.create_table('passive_bonus_to_school',
    sa.Column('passive_bonus_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.Column('school_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.ForeignKeyConstraint(['passive_bonus_id'], ['passive_bonus.id'], ),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.PrimaryKeyConstraint('passive_bonus_id', 'school_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('passive_bonus_to_school')
    op.drop_table('passive_bonus')
    # ### end Alembic commands ###
