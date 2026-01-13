# Jenkins Docker Setup Guide

## Prerequisites

- Docker Desktop installed and running

## Step 1: Pull the Jenkins Docker Image

Open your terminal/command prompt and run:

```bash
docker pull jenkins/jenkins:lts
```
This downloads the official Jenkins LTS (Long Term Support) version.

---

## Step 2: Create a Docker Volume for Jenkins Data

Create a volume to persist Jenkins data even if the container is removed:

```bash
docker volume create jenkins_home
```

---

## Step 3: Run Jenkins Container

Start the Jenkins container with the following command:

```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  --name jenkins \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

**Command breakdown:**
- `-d` - Runs container in detached mode (background)
- `-p 8080:8080` - Maps Jenkins web interface port
- `-p 50000:50000` - Maps port for Jenkins agents
- `-v jenkins_home:/var/jenkins_home` - Mounts volume for data persistence
- `--name jenkins` - Names your container "jenkins"

---
## Alternative: Using Docker Compose (Recommended)

### Step 3A: Create a Dockerfile for Custom Jenkins Image

If you need additional tools (like Python, Playwright, etc.) in your Jenkins container, create a custom image.

Create a file named `Dockerfile` in your project directory:

```dockerfile
FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create venv in a location accessible to the jenkins user
ENV VIRTUAL_ENV=/opt/playwright-venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python tools
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir pytest pytest-playwright pytest-html

# Install Browsers and system dependencies as root
RUN playwright install chromium
RUN playwright install-deps chromium

# Ensure the jenkins user owns the venv
RUN chown -R jenkins:jenkins $VIRTUAL_ENV

USER jenkins
```

---

### Step 3B: Create Docker Compose File

Create a `docker-compose.yml` file in your project directory:

```yaml
version: '3.8'

services:
  jenkins:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: jenkins
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home
    restart: unless-stopped

volumes:
  jenkins_home:
```

**Configuration breakdown:**
- `jenkins/jenkins:lts` - Base Jenkins LTS image
- `jenkins_home` volume - Persists Jenkins data
- Port `8080` - Jenkins web interface
- Port `50000` - Jenkins agent communication

---
**To use Docker Compose:**

```bash
# 1. Stop everything
docker-compose down

# 2. Remove the previous built image
docker rmi jenkins-playwright || true

# 3. Rebuild from scratch
docker compose build --no-cache --pull

# 4. Start fresh
docker compose up -d
```
---

## Step 4: Get the Initial Admin Password

Retrieve the initial administrator password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

**Copy the password** that appears in the terminal.

---

## Step 5: Open Jenkins Web Interface

1. Open your web browser
2. Navigate to: `http://localhost:8080`
3. Paste the initial admin password you copied
4. Click **Continue**

---

## Step 6: Install Plugins

You'll be presented with two options:

- **Install suggested plugins** (Recommended for beginners)
- **Select plugins to install** (For custom setup)

**Choose "Install suggested plugins"** and wait for the installation to complete.

---

## Step 7: Create First Admin User

Fill in the admin user creation form:

- Username
- Password
- Confirm Password
- Full Name
- Email Address

Click **Save and Continue**.

---

## Step 8: Configure Jenkins URL

The default URL `http://localhost:8080` should be displayed.

Click **Save and Finish**.

---

## Step 9: Start Using Jenkins

Click **Start using Jenkins** to access the Jenkins dashboard.

---

## Step 10: Add GitHub Credentials in Jenkins

If your repository is private, you'll need to add credentials:

1. From the Jenkins dashboard, go to **Manage Jenkins** → **Credentials**
2. Click on **(global)** domain
3. Click **Add Credentials** in the left sidebar
4. Configure the credentials:
   - **Kind**: Select "Username with password" or "Secret text" (for token)
   - **Scope**: Global
   - **Username**: Your GitHub username (if using username/password)
   - **Password/Secret**: Your GitHub Personal Access Token
   - **ID**: `github-creds` (or any identifier you prefer)
   - **Description**: "GitHub Access Token" (optional)
5. Click **Create**

**To create a GitHub Personal Access Token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click **Generate new token (classic)**
3. Give it a name and select scopes: `repo` (full control of private repositories)
4. Click **Generate token** and copy it immediately

---


## Step 11: Create Your First Pipeline Job

1. From the Jenkins dashboard, click **New Item**
2. Enter a name for your job (e.g., "playwright-python-tests")
3. Select **Pipeline** as the job type
4. Click **OK**

---

## Step 12: Configure Pipeline

In the pipeline configuration page:

1. **General Section**: Add a description (optional)
2. **Build Triggers**: Check options like:
   - "GitHub hook trigger for GITScm polling" (for automatic builds on push)
   - "Poll SCM" with schedule (e.g., `H/5 * * * *` for every 5 minutes)
3. **Pipeline Section**:
   - **Definition**: Select "Pipeline script from SCM"
   - **SCM**: Select "Git"
   - **Repository URL**: Enter your GitHub repository URL (e.g., `https://github.com/venkatesulu-byni/playwright-python-framework.git`)
   - **Credentials**: Select the `github-creds` you created earlier
   - **Branch Specifier**: `*/main` or `*/master` (depending on your default branch)
   - **Script Path**: `Jenkinsfile` (default location in your repo)
4. Click **Save**

---

## Step 13: Create a Jenkinsfile in Your Repository

Create a file named `Jenkinsfile` in the root of your GitHub repository:

```groovy
pipeline {
    agent any
     environment {
        VIRTUAL_ENV = "/var/jenkins_home/venv"
        PATH = "${VIRTUAL_ENV}/bin:${env.PATH}"
        PYTHONPATH = "${WORKSPACE}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version
                    pip3 install -r requirements.txt
                 '''
            }
        }
        stage('Run Playwright Tests') {
            steps {
                sh '''
                    pytest tests --html=report.html
                '''
            }
        }
    }
    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Playwright Test Report'
            ])
        }
        failure {
            echo 'Tests failed'
        }
        success {
            echo 'Tests passed'
        }
    }
}

```

Commit and push this file to your repository.

---
## Step 14: Run Your First Build

1. Go to your pipeline job in Jenkins
2. Click **Build Now** in the left sidebar
3. Watch the build progress in the **Build History**
4. Click on the build number to see details and console output

---

## Useful Docker Commands for Jenkins

**Stop Jenkins container:**
```bash
docker stop jenkins
```

**Start Jenkins container:**
```bash
docker start jenkins
```

**View Jenkins logs:**
```bash
docker logs -f jenkins
```

**Remove Jenkins container:**
```bash
docker rm -f jenkins
```

**Access Jenkins container shell:**
```bash
docker exec -it jenkins bash
```

---
