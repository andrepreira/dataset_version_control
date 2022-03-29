"""classificacao_modelo

Revision ID: c5d77fd21e89
Revises: 271656316ad5
Create Date: 2022-03-27 16:10:58.658488

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.sql.sqltypes import Float, DateTime
from sqlalchemy.schema import Sequence, Column
from sqlalchemy.types import DateTime, DATE, JSON, Integer, Text, String
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'c5d77fd21e89'
down_revision = '271656316ad5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'classificacao_modelo',
        Column('predict_classification', Text()),
        Column('id_texto',  String(100)),

        Column('created_at', DateTime(timezone=True), server_default=func.now()),
        Column('updated_at', DateTime(timezone=True), onupdate=func.now())
    )

def downgrade():
    op.drop_table('classificacao_modelo')