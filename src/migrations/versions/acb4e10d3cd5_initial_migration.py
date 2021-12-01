"""Initial migration.

Revision ID: acb4e10d3cd5
Revises: 
Create Date: 2021-12-01 12:46:01.459527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acb4e10d3cd5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('shortcut', sa.String(length=1), nullable=False),
    sa.Column('hex_code', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('shortcut')
    )
    op.create_table('spell',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('name_en', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=1024), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('requirements', sa.Text(), nullable=True),
    sa.Column('time_to_create', sa.String(length=1024), nullable=True),
    sa.Column('cost', sa.String(length=1024), nullable=True),
    sa.Column('duration', sa.String(length=1024), nullable=True),
    sa.Column('items', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name_en')
    )
    op.create_table('school',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('shortcut', sa.String(length=2), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('cycle_bonus_zero', sa.Text(), nullable=True),
    sa.Column('cycle_bonus_one', sa.Text(), nullable=True),
    sa.Column('cycle_bonus_two', sa.Text(), nullable=True),
    sa.Column('cycle_bonus_three', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('shortcut')
    )
    op.create_table('spell_to_color',
    sa.Column('spell_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.Column('color_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.ForeignKeyConstraint(['spell_id'], ['spell.id'], ),
    sa.PrimaryKeyConstraint('spell_id', 'color_id')
    )
    op.create_table('spell_to_school',
    sa.Column('spell_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.Column('school_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.Column('cycle', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.ForeignKeyConstraint(['spell_id'], ['spell.id'], ),
    sa.PrimaryKeyConstraint('spell_id', 'school_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spell_to_school')
    op.drop_table('spell_to_color')
    op.drop_table('school')
    op.drop_table('spell')
    op.drop_table('color')
    # ### end Alembic commands ###
