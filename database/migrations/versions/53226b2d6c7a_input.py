"""input

Revision ID: 53226b2d6c7a
Revises: 
Create Date: 2022-03-27 07:53:33.104606

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '53226b2d6c7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'input',
        Column('text', Text()),
        Column('id_texto',  String(100)),

        Column('created_at', DateTime(timezone=True), server_default=func.now()),
        Column('updated_at', DateTime(timezone=True), onupdate=func.now())
    )

def downgrade():
    op.drop_table('input')
