#!/usr/bin/env python3
"""
Database setup script for Flask Chat App
Creates tables and initializes sample data
"""

import os
from app import app, db, User
from datetime import datetime

def init_database():
    """Initialize database with tables and sample data"""
    with app.app_context():
        print("Setting up database...")
        
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Check if users already exist
        if User.query.first():
            print("Sample users already exist. Skipping user creation.")
            return
        
        # Create sample users
        sample_users = [
            {
                'username': 'john_doe',
                'email': 'john@example.com',
                'password': 'password123',
                'avatar': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face',
                'status': 'Hey there! I am John.'
            },
            {
                'username': 'sarah_johnson',
                'email': 'sarah@example.com',
                'password': 'password123',
                'avatar': 'https://images.unsplash.com/photo-1494790108755-2616b332765c?w=100&h=100&fit=crop&crop=face',
                'status': 'Available for chat!'
            },
            {
                'username': 'mike_chen',
                'email': 'mike@example.com',
                'password': 'password123',
                'avatar': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face',
                'status': 'Developer and coffee lover'
            },
            {
                'username': 'emma_wilson',
                'email': 'emma@example.com',
                'password': 'password123',
                'avatar': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop&crop=face',
                'status': 'Student and traveler'
            },
            {
                'username': 'alex_rodriguez',
                'email': 'alex@example.com',
                'password': 'password123',
                'avatar': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face',
                'status': 'Tech enthusiast'
            }
        ]
        
        print("Creating sample users...")
        for user_data in sample_users:
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                avatar=user_data['avatar'],
                status=user_data['status']
            )
            user.set_password(user_data['password'])
            db.session.add(user)
        
        try:
            db.session.commit()
            print(f"Successfully created {len(sample_users)} sample users!")
            print("\nSample users created:")
            for user_data in sample_users:
                print(f"  - {user_data['email']} / password123")
        except Exception as e:
            db.session.rollback()
            print(f"Error creating sample users: {e}")
            
        print("\nDatabase setup complete!")

def reset_database():
    """Reset database - drop all tables and recreate"""
    with app.app_context():
        print("Resetting database...")
        db.drop_all()
        init_database()

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'reset':
        reset_database()
    else:
        init_database()