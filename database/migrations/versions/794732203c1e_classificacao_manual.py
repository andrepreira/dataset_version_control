"""classificacao_manual

Revision ID: 794732203c1e
Revises: 53226b2d6c7a
Create Date: 2022-03-27 07:54:04.034117

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '794732203c1e'
down_revision = '53226b2d6c7a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'classificacao_manual',
        Column('annotation', Text()),
        Column('annotation_agent', Text()),
        Column('prediction', Text()),
        Column('prediction_agent', Text()),
        Column('id_texto',  String(100)),

        Column('created_at', DateTime(timezone=True), server_default=func.now()),
        Column('updated_at', DateTime(timezone=True), onupdate=func.now())
    )

def downgrade():
    op.drop_table('classificacao_manual')