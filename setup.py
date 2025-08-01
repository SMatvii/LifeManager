from setuptools import setup, find_packages
import os


def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "LifeManager - Фінансовий помічник Django додаток"

setup(
    name="lifemanager-core",
    version="1.0.0",
    author="SMatvii",
    description="LifeManager - Фінансовий помічник Django додаток",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/SMatvii/LifeManager",
    license="MIT",
    
    packages=find_packages(where="finassistant"),
    package_dir={"": "finassistant"},
    
    include_package_data=True,
    
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Office/Business :: Financial",
    ],
    
    python_requires=">=3.12",
    
    install_requires=[
        "Django>=5.2.4",
        "djangorestframework>=3.15.2",
        "django-allauth>=65.10.0",
        "drf-spectacular>=0.28.0",
        "Pillow>=11.3.0",
        "python-dotenv>=1.1.1",
        "psycopg2-binary>=2.9.10",
    ],
    
    extras_require={
        "dev": [
            "pytest>=8.4.1",
            "pytest-django>=4.11.1",
            "pytest-cov>=6.2.1",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
        ],
        "prod": [
            "gunicorn>=21.2.0",
            "whitenoise>=6.6.0",
        ],
    },
    
    entry_points={
        "console_scripts": [
            "lifemanager=finassistant.manage:main",
        ],
    },
    
    package_data={
        "": ["*.html", "*.css", "*.js", "*.json", "*.txt"],
        "core": ["templates/*", "static/*"],
    },
    
    zip_safe=False,
    
    keywords="django finance personal-finance budget-tracker event-planner",
    
    project_urls={
        "Bug Reports": "https://github.com/SMatvii/LifeManager/issues",
        "Source": "https://github.com/SMatvii/LifeManager",
        "Documentation": "https://github.com/SMatvii/LifeManager#readme",
    },
)