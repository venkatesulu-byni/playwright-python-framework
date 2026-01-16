# Playwright Python Test Automation Framework

A robust and scalable test automation framework built with Playwright and Python, featuring Page Object Model (POM) design pattern, BDD, and CI/CD integration with Jenkins.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Docker Support](#docker-support)
- [Jenkins CI/CD Integration](#jenkins-cicd-integration)
- [Writing Tests](#writing-tests)
- [Reporting](#reporting)
- [Best Practices](#best-practices)
- [Contributing](#contributing)

## ✨ Features

- **Page Object Model (POM)**: Clean separation of test logic and page interactions
- **BDD Support**: Write tests in Gherkin syntax
- **Multiple Browser Support**: Test across Chromium, Firefox, and WebKit
- **Parallel Execution**: Run tests in parallel for faster feedback
- **HTML Reports**: Generate detailed test execution reports
- **Docker Integration**: Containerized test execution environment
- **Jenkins CI/CD**: Automated pipeline for continuous testing
- **Cross-Platform**: Works on Windows and macOS
- **Screenshot & Video Capture**: Automatic capture on test failures
- **Reusable Utilities**: Helper functions for common operations

## 📁 Project Structure

```
playwright-python-framework/
├── docker/                     # Docker configuration files
│   ├── Dockerfile              # Custom Jenkins image with Playwright
│   └── docker-compose.yml      # Docker Compose configuration
├── features/                   # BDD feature files (Gherkin)
│   └── *.feature               # Feature files
├── pages/                      # Page Object Model classes
│   ├── base_page.py            # Base page with common methods
│   └── *_page.py               # Individual page objects
├── tests/                      # Test files (Pytest)
│   ├── conftest.py             # Pytest fixtures and configuration
│   └── test_*.py               # Test cases
├── utils/                      # Utility functions and helpers
│   ├── utils.py                # Utility functions
├── .gitignore                  # Git ignore file
├── Jenkinsfile                 # Jenkins pipeline configuration
├── jenkins_complete_setup.md   # Jenkins setup guide
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (comes with Python)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Docker** (Optional): [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/venkatesulu-byni/playwright-python-framework.git
cd playwright-python-framework
```

### 2. Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
# Install all browsers (Chromium, Firefox, WebKit)
playwright install

# Or install specific browser
playwright install chromium
playwright install firefox
playwright install webkit

# Install with system dependencies (Linux)
playwright install --with-deps
```

### 5. Verify Installation

```bash
# List installed browsers
playwright install --list

# Check Playwright version
playwright --version
```

## 🚀 Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py

# Run specific test function
pytest tests/test_login.py::test_valid_login

# Run tests with specific marker
pytest -m smoke
```

### Browser Options

```bash
# Run in specific browser
pytest --browser_name=chrome
pytest --browser_name=firefox

# Run in headed mode (see browser)
pytest --headed

# Run with slow motion (good for debugging)
pytest --slowmo 1000
```

### Parallel Execution

```bash
# Install pytest-xdist
pip install pytest-xdist

# Run tests in parallel (4 workers)
pytest -n 4

# Run tests in parallel (auto-detect CPU count)
pytest -n auto
```

## 🐳 Docker Support

### Using Docker Compose

```bash
# Build and start Jenkins with Playwright
cd docker
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Using Dockerfile

```bash
# Build custom image
docker build -t jenkins-playwright -f docker/Dockerfile .

# Run container
docker run -d -p 8080:8080 -p 50000:50000 \
  --name jenkins \
  -v jenkins_home:/var/jenkins_home \
  jenkins-playwright
```

## 🔄 Jenkins CI/CD Integration

### Setup Jenkins Pipeline

1. Follow the detailed setup guide in [`jenkins_complete_setup.md`](jenkins_complete_setup.md)
2. Configure GitHub webhook for automatic builds
3. View test reports in Jenkins dashboard

### Pipeline Features

- Automatic checkout from GitHub
- Dependency installation
- Test execution with Playwright
- HTML report generation
- Email notifications on failure
- Artifact archiving

### Jenkinsfile Example

The repository includes a `Jenkinsfile` with:
- Code checkout from GitHub
- Python dependency installation
- Playwright test execution
- HTML report publishing
- Post-build actions

## ✍️ Writing Tests

### Page Object Example

```python
# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
    
    def navigate(self):
        self.page.goto("/login")
    
    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
```

### Test Example

```python
# tests/test_login.py
import pytest
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("user@example.com", "password123")
    
    # Assertions
    assert page.url.endswith("/dashboard")
```

## 📊 Reporting

### HTML Reports

After test execution, view reports:

```bash
# Pytest HTML report
open report.html
```

## 🎯 Best Practices

### Test Organization

- Keep tests independent and isolated
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)
- Use fixtures for test setup and teardown
- Group related tests using pytest markers

### Page Objects

- One page object per page
- Use descriptive locator names
- Avoid logic in page objects
- Return page objects for method chaining
- Use base page for common functionality

### Locator Strategy

- Prefer user-facing attributes (role, text, label)
- Use data-testid for stable selectors
- Avoid CSS selectors when possible
- Keep locators maintainable and readable

### Error Handling

- Use explicit waits instead of sleep
- Handle expected errors gracefully
- Take screenshots on failures
- Log important test steps

## 📧 Contact

**Venkatesulu Byni**
- GitHub: [@venkatesulu-byni](https://github.com/venkatesulu-byni)
- Repository: [playwright-python-framework](https://github.com/venkatesulu-byni/playwright-python-framework)

---

**Happy Testing! 🎭🐍**
