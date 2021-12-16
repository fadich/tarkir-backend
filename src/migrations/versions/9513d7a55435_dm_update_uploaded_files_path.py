"""DM: Update uploaded files path

Revision ID: 9513d7a55435
Revises: ed69a96d0a61
Create Date: 2021-12-16 16:15:41.209834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9513d7a55435'
down_revision = 'ed69a96d0a61'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        """
        UPDATE
            uploaded_file
        SET file = 'upload/' || file
        WHERE file IS NOT NULL
        """
    )
    conn.execute(
        """
        UPDATE
            spell
        SET image = 'upload/' || image
        WHERE image IS NOT NULL
        """
    )
    conn.execute(
        """
        UPDATE
            school
        SET image = 'upload/' || image
        WHERE image IS NOT NULL
        """
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        """
        UPDATE
            uploaded_file
        SET file = overlay(file placing '' from 1 for char_length('upload/'))
        WHERE file LIKE 'upload/%%'
        """
    )
    conn.execute(
        """
        UPDATE
            spell
        SET image = overlay(image placing '' from 1 for char_length('upload/'))
        WHERE image LIKE 'upload/%%'
        """
    )
    conn.execute(
        """
        UPDATE
            school
        SET image = overlay(image placing '' from 1 for char_length('upload/'))
        WHERE image LIKE 'upload/%%'
        """
    )
