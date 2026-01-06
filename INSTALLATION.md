# 🚀 Installation Guide

Complete guide to setting up the Market Intelligence Platform on your local machine.

---

## 📋 Prerequisites

### Required
- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)

### Check Your Python Version
```bash
python --version
# or
python3 --version
```

If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/)

---

## 🔧 Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/market-intelligence.git
cd market-intelligence
```

### 2. Create Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

The app should automatically open in your browser at `http://localhost:8501`

---

## 🔑 API Keys (Optional but Recommended)

The app works with demo keys, but for better performance and no rate limits, get free API keys:

### Alpha Vantage (Recommended)
1. Go to https://www.alphavantage.co/support/#api-key
2. Enter your email to get a free key
3. **Limits**: 5 calls/minute, 500 calls/day

### Twelve Data (Optional)
1. Go to https://twelvedata.com/
2. Sign up for a free account
3. Get your API key from dashboard
4. **Limits**: 8 calls/day (free tier)

### Using Your API Keys

**Method 1: In the App UI** (Easiest)
1. Run the app
2. Go to sidebar → "🔑 API Keys"
3. Enter your keys
4. Keys are saved for the session

**Method 2: Environment Variables**
```bash
export ALPHA_VANTAGE_KEY="your-key-here"
export TWELVE_DATA_KEY="your-key-here"
```

**Method 3: Streamlit Secrets** (Persistent)
1. Create `.streamlit` folder in project root
2. Create `secrets.toml` file inside:
```toml
alpha_vantage_key = "your-key-here"
twelve_data_key = "your-key-here"
```
3. **Important**: Add `.streamlit/` to `.gitignore` (already done)

---

## 🐛 Troubleshooting

### Issue: "streamlit: command not found"
**Solution**: Make sure virtual environment is activated
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### Issue: "ModuleNotFoundError"
**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "API rate limit exceeded"
**Solution**: 
- Wait a few minutes
- Use your own API keys (see above)
- Try different data source in sidebar

### Issue: Port 8501 already in use
**Solution**: Use a different port
```bash
streamlit run app.py --server.port 8502
```

### Issue: Charts not displaying
**Solution**: 
- Clear browser cache
- Try different browser
- Check browser console for errors

### Issue: "Data not loading"
**Solution**:
- Check internet connection
- Verify API keys are correct
- Try switching data source (Alpha Vantage → Yahoo Finance)

---

## 🔄 Updating

To update to the latest version:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

---

## 🗑️ Uninstallation

### Remove Virtual Environment
```bash
deactivate  # Exit virtual environment
rm -rf venv  # Delete virtual environment folder
```

### Remove Project
```bash
cd ..
rm -rf market-intelligence
```

---

## 💻 System-Specific Notes

### macOS
- Use `python3` and `pip3` commands
- May need to install Xcode Command Line Tools: `xcode-select --install`

### Windows
- May need to enable script execution: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Use Command Prompt or PowerShell

### Linux
- May need to install python3-venv: `sudo apt-get install python3-venv`
- Install pip if needed: `sudo apt-get install python3-pip`

---

## 🐳 Docker (Advanced)

If you prefer Docker:

```dockerfile
# Dockerfile (create this file)
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t market-intelligence .
docker run -p 8501:8501 market-intelligence
```

---

## 📦 Dependencies Overview

| Package | Purpose |
|---------|---------|
| streamlit | Web framework |
| pandas | Data manipulation |
| numpy | Numerical computing |
| plotly | Interactive charts |
| requests | API calls |
| yfinance | Yahoo Finance data |
| scikit-learn | Data processing |
| scipy | Statistical functions |

---

## 🎯 Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] App runs successfully
- [ ] API keys configured (optional)
- [ ] Tested basic functionality

---

## 📞 Need Help?

- Check [Issues](https://github.com/yourusername/market-intelligence/issues)
- Create new issue if problem persists
- Include error messages and system info

---

## ✅ Verify Installation

Run this test:
```bash
python -c "import streamlit; import pandas; import plotly; print('All dependencies installed successfully!')"
```

If you see "All dependencies installed successfully!", you're ready to go! 🎉

---

**Happy Learning! 📚**
