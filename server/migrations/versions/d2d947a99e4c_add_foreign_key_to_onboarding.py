"""add foreign key to onboarding

Revision ID: d2d947a99e4c
Revises: b37f819d5449
Create Date: 2025-06-22 16:48:37.192411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2d947a99e4c'
down_revision = 'b37f819d5449'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.create_foreign_key(
            'fk_onboardings_employee_id_employee',
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employee', type_='foreignkey')
    # ### end Alembic commands ###
    op.drop_column('onboardings', 'employee_id')
    # ### end Alembic commands ###
