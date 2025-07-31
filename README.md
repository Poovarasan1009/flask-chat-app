# Flask Chat App - WhatsApp-like Messaging Application

A modern, real-time messaging web application built with Flask, SQLAlchemy, and Socket.IO. Features a WhatsApp-inspired design with user authentication, real-time messaging, and responsive UI.

## 🚀 Features

- **📧 Email Registration & Login**: Secure user authentication system
- **💬 Real-time Messaging**: Send and receive messages instantly with WebSocket support
- **👥 Multi-user Support**: Chat with multiple users simultaneously
- **📱 WhatsApp-inspired UI**: Modern, familiar interface design with green theme
- **🔐 User Authentication**: Secure Flask-Login integration
- **💾 Database Support**: SQLite for development, PostgreSQL for production
- **📱 Responsive Design**: Mobile-first approach, works on all devices
- **✅ Message Status**: Read receipts and delivery confirmations
- **👤 User Profiles**: Avatar support and online status indicators
- **🔍 Search Functionality**: Find conversations and users quickly
- **⚡ Typing Indicators**: Real-time typing status
- **🎨 Modern CSS**: Tailwind CSS with custom WhatsApp styling

## 🛠️ Technology Stack

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - Database ORM
- **Flask-Login** - User session management
- **Flask-SocketIO** - WebSocket support for real-time features
- **Flask-WTF** - Form handling and CSRF protection
- **Werkzeug** - Password hashing and security

### Frontend
- **HTML5 & CSS3** - Modern web standards
- **JavaScript ES6+** - Interactive functionality
- **Tailwind CSS** - Utility-first styling
- **Socket.IO Client** - Real-time communication
- **Font Awesome** - Icons and visual elements

### Database
- **SQLite** - Development database (included)
- **PostgreSQL** - Production database support
- **Free Database Options**: Heroku Postgres, Supabase, ElephantSQL, Railway

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Quick Start

1. **Clone or download the project**:
   ```bash
   cd flask-chat-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional):
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Open your browser** to `http://localhost:5000`

### Alternative: Direct Run
```bash
python app.py
```

## 👥 Sample Users

For testing purposes, the application includes these sample users:

| Username | Email | Password |
|----------|-------|----------|
| john_doe | john@example.com | password123 |
| sarah_johnson | sarah@example.com | password123 |
| mike_chen | mike@example.com | password123 |

## 🗄️ Database Configuration

### SQLite (Development - Default)
No additional setup required. Database file `chat.db` is created automatically.

### PostgreSQL (Production)
1. **Install PostgreSQL** or use a free service:
   - **Heroku Postgres**: Free tier available
   - **Supabase**: Free PostgreSQL with dashboard
   - **ElephantSQL**: Free PostgreSQL hosting
   - **Railway**: Modern deployment platform

2. **Update environment variables**:
   ```bash
   DATABASE_URL=postgresql://username:password@hostname:port/database
   ```

3. **Run database migrations**:
   ```bash
   python -c "from app import db; db.create_all()"
   ```

## 🔧 Configuration

### Environment Variables
Create a `.env` file (copy from `.env.example`):

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///chat.db
FLASK_ENV=development
FLASK_DEBUG=True
```

### Configuration Classes
- `DevelopmentConfig`: Debug mode, SQLite database
- `ProductionConfig`: Optimized for production, PostgreSQL
- `TestingConfig`: For running tests

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production Deployment

#### Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
```

#### Railway
```bash
# Connect to Railway
railway login
railway init
railway add
railway deploy
```

#### Traditional Server
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn --worker-class eventlet -w 1 run:app
```

## 📁 Project Structure

```
flask-chat-app/
├── app.py                  # Main Flask application
├── run.py                  # Application entry point
├── config.py               # Configuration classes
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .env.example           # Environment variables template
├── templates/             # HTML templates
│   ├── base.html         # Base template with styles
│   ├── auth.html         # Login/Register page
│   └── chat.html         # Main chat interface
├── static/               # Static files
│   └── style.css        # Custom CSS styles
└── chat.db              # SQLite database (auto-created)
```

## 🎨 UI/UX Features

### WhatsApp-like Design
- **Green color scheme** matching WhatsApp branding
- **Message bubbles** with proper alignment
- **User avatars** and online status indicators
- **Typing indicators** for real-time feedback
- **Read receipts** with checkmark system
- **Responsive design** for all screen sizes

### Interactive Elements
- **Real-time messaging** with WebSocket
- **Search functionality** for users and conversations
- **Typing indicators** when users are typing
- **Online/offline status** tracking
- **Message timestamps** with smart formatting
- **Smooth animations** and transitions

## 🔒 Security Features

- **Password hashing** with Werkzeug
- **CSRF protection** with Flask-WTF
- **Session management** with Flask-Login
- **Input validation** and sanitization
- **SQL injection prevention** with SQLAlchemy
- **XSS protection** with template escaping

## 📊 API Endpoints

### Authentication
- `GET /` - Redirect to login or chat
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /register` - Registration page
- `POST /register` - Process registration
- `GET /logout` - Logout user

### Chat API
- `GET /chat` - Main chat interface
- `GET /api/users` - Get all users
- `GET /api/messages/<user_id>` - Get messages with user
- `POST /api/send_message` - Send new message

### WebSocket Events
- `connect` - User connection
- `disconnect` - User disconnection
- `typing` - Typing indicator
- `new_message` - Real-time message delivery

## 🧪 Testing

### Manual Testing
1. Register multiple users
2. Login with different browsers/tabs
3. Send messages between users
4. Test typing indicators
5. Check real-time updates

### Automated Testing
```bash
# Install testing dependencies
pip install pytest pytest-flask

# Run tests
pytest tests/
```

## 🔧 Development

### Adding New Features
1. **Database Models**: Add to `app.py`
2. **Routes**: Add to `app.py`
3. **Templates**: Add to `templates/`
4. **Styles**: Add to `static/style.css`
5. **JavaScript**: Add to template files

### Common Customizations
- **Change colors**: Update CSS variables in `base.html`
- **Add file upload**: Extend message model and form
- **Add group chats**: Create group model and UI
- **Add voice messages**: Integrate audio recording
- **Add video calls**: Integrate WebRTC

## 📱 Mobile Responsiveness

The application is fully responsive and works on:
- **Desktop computers** (Windows, Mac, Linux)
- **Tablets** (iPad, Android tablets)
- **Mobile phones** (iPhone, Android)
- **Different screen sizes** and orientations

## 🆘 Troubleshooting

### Common Issues

1. **Database errors**:
   ```bash
   # Reset database
   rm chat.db
   python -c "from app import db; db.create_all()"
   ```

2. **Port already in use**:
   ```bash
   # Kill process on port 5000
   lsof -ti:5000 | xargs kill
   ```

3. **Dependencies not installing**:
   ```bash
   # Upgrade pip
   python -m pip install --upgrade pip
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. **WebSocket connection issues**:
   - Check firewall settings
   - Verify Socket.IO version compatibility
   - Test with different browsers

### Debug Mode
```bash
export FLASK_DEBUG=True
python run.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Flask** - Web framework
- **Socket.IO** - Real-time communication
- **Tailwind CSS** - Styling framework
- **Font Awesome** - Icons
- **WhatsApp** - UI/UX inspiration

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Test with sample users
4. Check browser console for errors

---

**Perfect for college projects, learning web development, or building modern chat applications!** 🎓

## 🎯 Next Steps

After getting the basic app running, you can:
1. **Customize the design** to match your preferences
2. **Add more features** like file sharing or group chats
3. **Deploy to a cloud platform** for public access
4. **Extend the database** with more user information
5. **Add mobile app** support with React Native or Flutter

Happy coding! 🚀# test deploy
