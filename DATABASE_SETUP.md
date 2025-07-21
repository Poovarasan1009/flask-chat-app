# Database Setup Guide for Flask Chat App

## 🗄️ Database Configuration

Your Flask Chat App now supports both **SQLite** (development) and **PostgreSQL** (production) databases.

### Current Database Setup
- **Environment**: PostgreSQL database is now configured
- **Connection**: Available via DATABASE_URL environment variable
- **Tables**: User, Message models with relationships
- **Sample Data**: Automatic creation of test users

## 🚀 Database Setup Commands

### Initialize Database
```bash
# Create tables and sample data
python database_setup.py

# Reset database (drop and recreate)
python database_setup.py reset
```

### Manual Database Operations
```bash
# Access Python shell with app context
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Tables created!')"

# Check database connection
python -c "from app import app, db, User; app.app_context().push(); print(f'Users: {User.query.count()}')"
```

## 📊 Database Schema

### User Table
```sql
CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(120) NOT NULL,
    avatar VARCHAR(200) DEFAULT 'https://via.placeholder.com/50',
    status VARCHAR(200) DEFAULT 'Hey there! I am using ChatApp',
    is_online BOOLEAN DEFAULT FALSE,
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Message Table
```sql
CREATE TABLE message (
    id SERIAL PRIMARY KEY,
    sender_id INTEGER REFERENCES user(id) NOT NULL,
    recipient_id INTEGER REFERENCES user(id) NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_read BOOLEAN DEFAULT FALSE
);
```

## 👥 Sample Users Created

After database setup, these test accounts are available:

| Username | Email | Password |
|----------|-------|----------|
| john_doe | john@example.com | password123 |
| sarah_johnson | sarah@example.com | password123 |
| mike_chen | mike@example.com | password123 |
| emma_wilson | emma@example.com | password123 |
| alex_rodriguez | alex@example.com | password123 |

## 🔧 Database Configuration

### Environment Variables
```bash
# PostgreSQL (production)
DATABASE_URL=postgresql://username:password@host:port/database
PGHOST=hostname
PGPORT=5432
PGUSER=username
PGPASSWORD=password
PGDATABASE=database_name

# SQLite (development fallback)
DATABASE_URL=sqlite:///chat.db
```

### Configuration in Code
```python
# config.py
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
SQLALCHEMY_DATABASE_URI = database_url or 'sqlite:///chat.db'
```

## 🔍 Database Operations

### Check Database Status
```bash
# Test database connection
python -c "
from app import app, db
with app.app_context():
    try:
        db.engine.execute('SELECT 1')
        print('Database connection successful!')
    except Exception as e:
        print(f'Database error: {e}')
"
```

### View Database Data
```bash
# Count users
python -c "
from app import app, db, User
with app.app_context():
    print(f'Total users: {User.query.count()}')
    for user in User.query.all():
        print(f'  {user.username} - {user.email}')
"

# Count messages
python -c "
from app import app, db, Message
with app.app_context():
    print(f'Total messages: {Message.query.count()}')
"
```

## 🔄 Database Migration

### From SQLite to PostgreSQL
```bash
# 1. Export SQLite data (if needed)
python -c "
from app import app, db, User, Message
import json
with app.app_context():
    users = [{'username': u.username, 'email': u.email} for u in User.query.all()]
    with open('users_backup.json', 'w') as f:
        json.dump(users, f)
    print('Data exported to users_backup.json')
"

# 2. Switch to PostgreSQL
export DATABASE_URL=postgresql://username:password@host:port/database

# 3. Initialize new database
python database_setup.py
```

### Backup Database
```bash
# PostgreSQL backup
pg_dump $DATABASE_URL > backup.sql

# SQLite backup
cp chat.db chat_backup.db
```

## 🛠️ Troubleshooting

### Common Database Issues

#### 1. Connection Errors
```bash
# Check DATABASE_URL
echo $DATABASE_URL

# Test connection
python -c "
import os
from sqlalchemy import create_engine
engine = create_engine(os.environ['DATABASE_URL'])
print('Connection successful!')
"
```

#### 2. Table Creation Errors
```bash
# Reset database
python database_setup.py reset

# Check tables
python -c "
from app import app, db
with app.app_context():
    print(db.engine.table_names())
"
```

#### 3. Permission Errors
```bash
# Check database permissions
python -c "
from app import app, db
with app.app_context():
    try:
        db.engine.execute('CREATE TABLE test_table (id INTEGER)')
        db.engine.execute('DROP TABLE test_table')
        print('Database permissions OK')
    except Exception as e:
        print(f'Permission error: {e}')
"
```

## 🚀 Production Database Setup

### Heroku PostgreSQL
```bash
# Add Heroku Postgres addon
heroku addons:create heroku-postgresql:hobby-dev

# Initialize database
heroku run python database_setup.py
```

### Railway PostgreSQL
```bash
# Add PostgreSQL service
railway add postgresql

# Initialize database
railway run python database_setup.py
```

### Supabase
```bash
# Get connection string from Supabase dashboard
export DATABASE_URL=postgresql://username:password@host:port/database

# Initialize database
python database_setup.py
```

## 📊 Database Performance

### Indexing (for production)
```sql
-- Add indexes for better performance
CREATE INDEX idx_user_email ON user(email);
CREATE INDEX idx_message_sender ON message(sender_id);
CREATE INDEX idx_message_recipient ON message(recipient_id);
CREATE INDEX idx_message_timestamp ON message(timestamp);
```

### Connection Pooling
```python
# config.py - Add for production
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
    'pool_timeout': 20,
    'max_overflow': 0
}
```

## 🔐 Security Notes

### Database Security
- **Never commit** DATABASE_URL to version control
- **Use environment variables** for sensitive data
- **Enable SSL** in production PostgreSQL
- **Regular backups** of production data

### User Data Protection
- **Passwords are hashed** using Werkzeug
- **SQL injection prevention** with SQLAlchemy
- **Input validation** on all user data
- **Session security** with Flask-Login

## 📚 Additional Resources

### PostgreSQL Documentation
- **Official Docs**: postgresql.org/docs/
- **Python psycopg2**: psycopg.org/docs/
- **SQLAlchemy**: docs.sqlalchemy.org/

### Flask Database Integration
- **Flask-SQLAlchemy**: flask-sqlalchemy.palletsprojects.com/
- **Flask-Migrate**: flask-migrate.readthedocs.io/
- **Database Design**: realpython.com/flask-databases/

---

**Your Flask Chat App now has a robust database setup!** The PostgreSQL database is configured and ready for both development and production use.

## Quick Start with Database

1. **Initialize database**: `python database_setup.py`
2. **Run application**: `python run.py`
3. **Test with sample users**: Login with john@example.com / password123
4. **Start chatting**: Real-time messaging with persistent data storage

The database will automatically handle user authentication, message storage, and real-time chat functionality.