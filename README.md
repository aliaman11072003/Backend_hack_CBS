# AI-Powered Negotiation Assistant

## 🚀 Complete Installation Guide

### Step 1: System Setup

- Ubuntu 20.04 or higher
- Python 3.10 or higher
- MongoDB 6.0 or higher
- Git

### Step 1: Basic Requirements
Make sure you have Ubuntu 20.04 or higher installed on your system. If not, most steps should still work on other Linux distributions.

### Step 2: Clone the Project
Open your terminal and run:
```bash
git clone [repository-url]
cd ai-negotiation-assistant
```

### Step 3: Run the Setup Script
```bash
# Method 1 (Try this first):
chmod +x setup.sh
./setup.sh

# If that doesn't work, try:
bash setup.sh
```

The setup script will automatically:
- Install Python and required system packages
- Set up MongoDB (Community Edition)
- Create a virtual environment
- Install all Python dependencies
- Download required ML models
- Create necessary project directories
### Step 4: Configure Environment Variables and OpenAI
```bash
# The setup script creates a .env file from .env.example
# Open it:
nano .env
```

Important configurations:
1. **OpenAI API Key**:
   - Visit https://platform.openai.com/api-keys
   - Create a new API key
   - Add it to your .env file:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```
   - ⚠️ NEVER commit your API key to version control
   - ⚠️ Keep your API key secure and don't share it

2. **JWT Secret**:
   - Change the JWT_SECRET to a secure random string
   - You can generate one using:
     ```bash
     openssl rand -hex 32
     ```

### Step 5: Start the Application
```bash
# Start the application using:
./run.sh
```

That's it! The application should now be running at:
- API Documentation: http://localhost:8000/docs
- Web Interface: http://localhost:8000

## ⚠️ Common Issues & Solutions

### 1. "Permission denied" when running setup.sh
```bash
# Run:
chmod +x setup.sh
```

### 2. MongoDB Issues
If MongoDB installation fails or MongoDB isn't starting:
```bash
# Check MongoDB status
sudo systemctl status mongod

# If MongoDB isn't running, start it:
sudo systemctl start mongod
sudo systemctl enable mongod

# If you see errors, try:
sudo systemctl daemon-reload
sudo systemctl restart mongod

# Check MongoDB logs:
sudo tail -f /var/log/mongodb/mongod.log
```

If MongoDB still fails to install, you can manually install it:
```bash
# Import MongoDB public key
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
    sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
    --dearmor

# Add MongoDB repository
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/6.0 multiverse" | \
    sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Update and install
sudo apt update
sudo apt install -y mongodb-org
```

### 3. Python Virtual Environment Issues
```bash
# If you see Python-related errors, try:
source venv/bin/activate  # Do this before running any Python commands
```

### 4. Dependencies Installation Failed
```bash
# Activate virtual environment and retry:
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 🔒 Security Notes

1. **API Keys**:
   - Never commit your .env file to git
   - Don't share your API keys
   - Rotate API keys if they're compromised

2. **Environment Variables**:
   - Keep your .env file secure
   - Don't expose environment variables in logs
   - Use different API keys for development and production

## 📚 Detailed Installation Steps

### Step 1: Basic Setup
