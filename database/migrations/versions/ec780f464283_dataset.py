"""dataset

Revision ID: ec780f464283
Revises: 
Create Date: 2022-03-31 21:42:16.599853

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = 'ec780f464283'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'dataset',
        Column('id',Integer, primary_key=True, autoincrement=True, nullable=False),
        Column('nome', String(250)),
        Column('tipo', String(250))
    )


def downgrade():
    op.drop_table('dataset')
