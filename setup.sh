#!/bin/bash

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting AI Negotiation Assistant Setup...${NC}"

# Check if Python 3.10 or higher is installed
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.10.0"

if [ $(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1) != "$required_version" ]; then
    echo -e "${RED}Python 3.10 or higher is required. Installing...${NC}"
    sudo apt update
    sudo apt install -y python3.10 python3.10-venv python3-pip
fi

# Install system dependencies
echo -e "${YELLOW}Installing system dependencies...${NC}"
sudo apt update
sudo apt install -y \
    python3-dev \
    libpq-dev \
    build-essential \
    ffmpeg \
    git \
    nodejs \
    npm

# Install MongoDB (Updated method)
echo -e "${YELLOW}Setting up MongoDB...${NC}"
if ! command -v mongod &> /dev/null; then
    echo -e "${YELLOW}Installing MongoDB...${NC}"
    # Import MongoDB public key
    curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
        sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
        --dearmor
    
    # Create list file for MongoDB
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-org/6.0 multiverse" | \
        sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
    
    # Update package list and install MongoDB
    sudo apt update
    sudo apt install -y mongodb-org
    
    # Start MongoDB
    sudo systemctl start mongod
    sudo systemctl enable mongod
    
    echo -e "${GREEN}MongoDB installed and started successfully${NC}"
else
    echo -e "${GREEN}MongoDB is already installed${NC}"
    # Ensure MongoDB is started
    sudo systemctl start mongod
    sudo systemctl enable mongod
fi

# Create virtual environment
echo -e "${YELLOW}Setting up Python virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
echo -e "${YELLOW}Installing Python dependencies...${NC}"
pip install -r requirements.txt

# Create necessary directories
echo -e "${YELLOW}Creating project directories...${NC}"
mkdir -p app/{api,core,services,models,tests}
mkdir -p app/api/{routes,endpoints}
mkdir -p logs

# Download ML models
echo -e "${YELLOW}Downloading ML models...${NC}"
python download_models.py

# Set up environment variables
if [ ! -f .env ]; then
    echo -e "${YELLOW}Creating .env file...${NC}"
    cp .env.example .env
    echo -e "${RED}Please update the .env file with your OpenAI API key and other configurations${NC}"
    echo -e "${RED}Get your API key from: https://platform.openai.com/api-keys${NC}"
fi

# Make run script executable
chmod +x run.sh

# Create project structure
mkdir -p app/{api,core,services,models,tests}
mkdir -p app/api/{routes,endpoints}
mkdir -p logs

# Create __init__.py files
touch app/__init__.py
touch app/api/__init__.py
touch app/core/__init__.py
touch app/services/__init__.py
touch app/tests/__init__.py
touch app/api/routes/__init__.py
touch app/api/endpoints/__init__.py

echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${YELLOW}To start the application:${NC}"
echo -e "1. Update the .env file with your configurations"
echo -e "2. Run: ./run.sh"
echo -e "\n${YELLOW}To view the API documentation:${NC}"
echo -e "Visit: http://localhost:8000/docs" 