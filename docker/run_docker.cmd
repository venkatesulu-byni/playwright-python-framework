# 1. Stop everything
docker-compose down

# 2. Remove the previous built image
docker rmi jenkins-playwright || true

# 3. Rebuild from scratch
docker compose build --no-cache --pull

# 4. Start fresh
docker compose up -d