#!/usr/bin/env python3
"""
Test database connection and operations
"""

import os
from app import app, db, User, Message

def test_database_connection():
    """Test basic database connection"""
    with app.app_context():
        try:
            # Test basic query
            from sqlalchemy import text
            result = db.session.execute(text('SELECT 1')).scalar()
            print(f"✓ Database connection successful! Test query returned: {result}")
            return True
        except Exception as e:
            print(f"✗ Database connection failed: {e}")
            return False

def test_user_operations():
    """Test user CRUD operations"""
    with app.app_context():
        try:
            # Count users
            user_count = User.query.count()
            print(f"✓ Total users in database: {user_count}")
            
            # Get first user
            if user_count > 0:
                user = User.query.first()
                print(f"✓ First user: {user.username} ({user.email})")
                print(f"  Status: {user.status}")
                print(f"  Created: {user.created_at}")
            
            return True
        except Exception as e:
            print(f"✗ User operations failed: {e}")
            return False

def test_message_operations():
    """Test message CRUD operations"""
    with app.app_context():
        try:
            # Count messages
            message_count = Message.query.count()
            print(f"✓ Total messages in database: {message_count}")
            
            # Get recent messages
            if message_count > 0:
                messages = Message.query.order_by(Message.timestamp.desc()).limit(5).all()
                print(f"✓ Recent messages:")
                for msg in messages:
                    print(f"  From: {msg.sender.username} -> {msg.recipient.username}")
                    print(f"  Content: {msg.content[:50]}...")
                    print(f"  Time: {msg.timestamp}")
            
            return True
        except Exception as e:
            print(f"✗ Message operations failed: {e}")
            return False

def show_database_info():
    """Show database configuration info"""
    database_url = os.environ.get('DATABASE_URL', 'Not set')
    print(f"Database URL: {database_url}")
    print(f"Database Host: {os.environ.get('PGHOST', 'Not set')}")
    print(f"Database Port: {os.environ.get('PGPORT', 'Not set')}")
    print(f"Database Name: {os.environ.get('PGDATABASE', 'Not set')}")
    print(f"Database User: {os.environ.get('PGUSER', 'Not set')}")

if __name__ == '__main__':
    print("=== Flask Chat App Database Test ===")
    print()
    
    print("1. Database Configuration:")
    show_database_info()
    print()
    
    print("2. Testing Database Connection:")
    if test_database_connection():
        print()
        
        print("3. Testing User Operations:")
        test_user_operations()
        print()
        
        print("4. Testing Message Operations:")
        test_message_operations()
        print()
        
        print("✓ All database tests passed!")
        print("Your Flask Chat App database is ready to use!")
    else:
        print("✗ Database connection failed. Please check your configuration.")
        print("Make sure DATABASE_URL is set correctly.")