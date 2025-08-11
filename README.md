### Installation
- Create Overlay network `docker network create -d overlay --attachable app-net`
- build image 
    - nginx : `docker build -t swapp-nginx:dev -f nginx/Dockerfile .`
    - backend : `docker build -t swapp-backend:dev ./backend`
- deploy stack `docker stack deploy -c stack.docker-compose.yaml web-swapp` 