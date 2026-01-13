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