#!/usr/bin/env python
import os
import sys
import subprocess

def main():
    print("Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    
    print("Navigating to Django project...")
    os.chdir("finassistant")
    
    print("Collecting static files...")
    subprocess.run([sys.executable, "manage.py", "collectstatic", "--noinput"], check=True)
    
    print("Running migrations...")
    subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
    
    print("Starting gunicorn server...")
    port = os.environ.get("PORT", "8000")
    subprocess.run([
        sys.executable, "-m", "gunicorn", 
        "finassistant.wsgi:application", 
        "--bind", f"0.0.0.0:{port}"
    ], check=True)

if __name__ == "__main__":
    main()
