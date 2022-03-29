"""classificacao_fraca_regex

Revision ID: 271656316ad5
Revises: 794732203c1e
Create Date: 2022-03-27 07:54:25.601501

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '271656316ad5'
down_revision = '794732203c1e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'classificacao_fraca_regex',
        Column('classificacao', Text()),
        Column('id_texto',  String(100)),

        Column('created_at', DateTime(timezone=True), server_default=func.now()),
        Column('updated_at', DateTime(timezone=True), onupdate=func.now())
    )

def downgrade():
    op.drop_table('classificacao_fraca_regex')