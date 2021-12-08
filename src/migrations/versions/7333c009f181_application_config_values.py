"""Application config values

Revision ID: 7333c009f181
Revises: b1c5d54726b9
Create Date: 2021-12-08 11:23:57.270089

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '7333c009f181'
down_revision = 'b1c5d54726b9'
branch_labels = None
depends_on = None


def upgrade():
    data_type_enum = postgresql.ENUM('NULL', 'INT', 'FLOAT', 'STRING', 'BOOLEAN', 'JSON', name='data_types_enum')
    data_type_enum.create(op.get_bind())

    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('config', sa.Column('raw_value', sa.Text(), nullable=True))
    op.add_column('config', sa.Column('data_type', sa.Enum('NULL', 'INT', 'FLOAT', 'STRING', 'BOOLEAN', 'JSON', name='data_types_enum'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('config', 'data_type')
    op.drop_column('config', 'raw_value')
    # ### end Alembic commands ###

    data_type_enum = postgresql.ENUM('NULL', 'INT', 'FLOAT', 'STRING', 'BOOLEAN', 'JSON', name='data_types_enum')
    data_type_enum.drop(op.get_bind())
