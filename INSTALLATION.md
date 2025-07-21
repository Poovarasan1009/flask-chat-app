# Flask Chat App - Installation Guide

## Quick Start (5 minutes)

### Prerequisites
- Python 3.8+ installed on your system
- Command line/terminal access

### Step 1: Download and Extract
1. Download the `flask-chat-app` folder
2. Extract to your desired location
3. Open terminal/command prompt in the project folder

### Step 2: Install Python Dependencies
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
# Option 1: Using run.py (recommended)
python run.py

# Option 2: Using app.py directly
python app.py
```

### Step 4: Access the Application
- Open your browser to `http://localhost:5000`
- The app will automatically create sample users on first run

## Sample Users for Testing

| Username | Email | Password |
|----------|-------|----------|
| john_doe | john@example.com | password123 |
| sarah_johnson | sarah@example.com | password123 |
| mike_chen | mike@example.com | password123 |

## Free Database Options

### SQLite (Default - No Setup Required)
- Automatically creates `chat.db` file
- Perfect for development and testing
- No additional configuration needed

### PostgreSQL (Free Services)

#### 1. Heroku Postgres (Free Tier)
```bash
# Sign up at heroku.com
# Create new app
# Add Heroku Postgres add-on (free tier)
# Copy DATABASE_URL to .env file
```

#### 2. Supabase (Free Tier)
```bash
# Sign up at supabase.com
# Create new project
# Go to Settings > Database
# Copy connection string to .env file
```

#### 3. ElephantSQL (Free Tier)
```bash
# Sign up at elephantsql.com
# Create new instance (free tier)
# Copy URL to .env file
```

#### 4. Railway (Free Tier)
```bash
# Sign up at railway.app
# Create new project
# Add PostgreSQL service
# Copy DATABASE_URL to .env file
```

## Environment Configuration

### Create .env file (optional but recommended)
```bash
# Copy example file
cp .env.example .env

# Edit with your settings
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///chat.db
FLASK_ENV=development
```

### For PostgreSQL
```bash
# Update .env file
DATABASE_URL=postgresql://username:password@hostname:port/database
```

## Troubleshooting

### Common Issues

1. **Python not found**
   ```bash
   # Try these alternatives
   python3 run.py
   py run.py
   ```

2. **Permission denied**
   ```bash
   # On Windows, run as administrator
   # On macOS/Linux, use sudo if needed
   sudo python run.py
   ```

3. **Port already in use**
   ```bash
   # Kill process on port 5000
   # On Windows:
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   
   # On macOS/Linux:
   lsof -ti:5000 | xargs kill
   ```

4. **Dependencies not installing**
   ```bash
   # Upgrade pip
   python -m pip install --upgrade pip
   
   # Install dependencies
   pip install -r requirements.txt
   ```

5. **Database errors**
   ```bash
   # Reset database
   rm chat.db
   python run.py
   ```

### System-Specific Instructions

#### Windows
```bash
# Use Command Prompt or PowerShell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

#### macOS
```bash
# Use Terminal
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

#### Linux (Ubuntu/Debian)
```bash
# Install Python and pip if not available
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python run.py
```

## Advanced Setup

### Production Deployment

#### Using Gunicorn (Recommended)
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn --worker-class eventlet -w 1 run:app
```

#### Using Docker
```bash
# Create Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "run.py"]

# Build and run
docker build -t flask-chat-app .
docker run -p 5000:5000 flask-chat-app
```

### Environment Variables

#### Required
- `SECRET_KEY`: Flask secret key for sessions
- `DATABASE_URL`: Database connection string

#### Optional
- `FLASK_ENV`: Environment (development/production)
- `FLASK_DEBUG`: Debug mode (True/False)
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 5000)

### Database Migration

#### From SQLite to PostgreSQL
```bash
# Export data (if needed)
python -c "from app import db; db.create_all()"

# Update DATABASE_URL in .env
DATABASE_URL=postgresql://...

# Run migration
python run.py
```

## Development Setup

### Code Editor Setup
- **VS Code**: Install Python extension
- **PyCharm**: Open project folder
- **Sublime Text**: Install Python packages

### Debug Mode
```bash
# Enable debug mode
export FLASK_DEBUG=True
python run.py

# Or set in .env file
FLASK_DEBUG=True
```

### Hot Reload
Debug mode enables automatic reloading when code changes.

## Testing

### Manual Testing
1. Register new user
2. Login with sample users
3. Send messages between users
4. Test real-time features
5. Check mobile responsiveness

### Automated Testing
```bash
# Install testing dependencies
pip install pytest pytest-flask

# Run tests
pytest
```

## Security Notes

### Development vs Production
- **Development**: Uses SQLite, debug mode enabled
- **Production**: Use PostgreSQL, disable debug mode

### Important Security Settings
```bash
# Production environment variables
SECRET_KEY=strong-random-secret-key
FLASK_ENV=production
FLASK_DEBUG=False
SESSION_COOKIE_SECURE=True
```

## Performance Optimization

### Database Optimization
- Use PostgreSQL for production
- Add database indexes if needed
- Monitor query performance

### Static Files
- Use CDN for static assets in production
- Enable gzip compression
- Optimize images and CSS

## Monitoring

### Logs
- Check `app.log` for application logs
- Monitor database performance
- Track user activity

### Health Checks
- Test WebSocket connections
- Monitor memory usage
- Check database connections

## Support

### Getting Help
1. Check this installation guide
2. Review the main README.md
3. Check browser console for errors
4. Test with sample users first

### Common Solutions
- **Database issues**: Reset database file
- **Port conflicts**: Use different port
- **Permission errors**: Check file permissions
- **Import errors**: Verify virtual environment

---

**You're all set!** The Flask Chat App should now be running on your system. Visit `http://localhost:5000` to start chatting!

## Next Steps

1. **Test the application** with sample users
2. **Customize the design** to your liking
3. **Add new features** as needed
4. **Deploy to production** when ready
5. **Share with friends** and get feedback

Happy chatting! 🚀