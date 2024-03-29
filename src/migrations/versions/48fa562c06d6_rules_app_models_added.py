"""Rules App models added

Revision ID: 48fa562c06d6
Revises: 9513d7a55435
Create Date: 2021-12-16 20:29:44.720864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48fa562c06d6'
down_revision = '9513d7a55435'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rule',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('image', sa.String(length=1024), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('rule_to_tag',
    sa.Column('rule_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.Column('tag_id', sa.Integer(), nullable=False, on_delete='CASCADE'),
    sa.ForeignKeyConstraint(['rule_id'], ['rule.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('rule_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rule_to_tag')
    op.drop_table('tag')
    op.drop_table('rule')
    # ### end Alembic commands ###
