from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '[timestamp]_create_tables'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create user table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False, unique=True),
        sa.Column('password', sa.String(length=100), nullable=False),
        sa.Column('role', sa.String(length=10), nullable=False),
        sa.Column('history', sa.JSON, nullable=True),
    )

    # Create mcq table
    op.create_table(
        'mcqs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question', sa.Text, nullable=False),
        sa.Column('options', sa.JSON, nullable=False),
        sa.Column('correct_answer', sa.String(length=50), nullable=False),
        sa.Column('category', sa.String(length=50), nullable=False),
        sa.Column('difficulty', sa.String(length=20), nullable=False),
        sa.Column('tags', sa.JSON, nullable=True),
    )

def downgrade():
    op.drop_table('mcqs')
    op.drop_table('users')