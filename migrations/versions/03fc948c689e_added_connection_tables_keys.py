"""Added connection tables keys

Revision ID: 03fc948c689e
Revises: 2312a54381c8
Create Date: 2020-11-27 00:15:53.855359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03fc948c689e'
down_revision = '2312a54381c8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_primary_key('spell_color_pk', 'spell_to_color', [
        'spell_id',
        'color_id',
    ])
    op.create_primary_key('spell_school_cycle_pk', 'spell_to_school', [
        'spell_id',
        'school_id',
        'cycle',
    ])


def downgrade():
    op.drop_constraint(
        constraint_name='spell_school_cycle_pk',
        table_name='spell_to_school',
        type_='primary'
    )
    op.drop_constraint(
        constraint_name='spell_color_pk',
        table_name='spell_to_color',
        type_='primary'
    )
