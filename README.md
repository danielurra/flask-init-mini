# flask-init-mini

This project is a boilerplate for future Flask applications.

The OS we'll be using is Linux Ubuntu.

## Setup SSH key

**This step is OPTIONAL and can be omitted.**

Create ssh key and add it to GitHub's [SSH keys](https://github.com/settings/keys) settings.

```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub
```

## Installation

```bash
# Cloning the source code
git clone https://github.com/danielurra/flask-init-mini.git
cd flask-init-mini

# Building and running docker container
docker build --tag flask-mini --build-arg FLASK_DEBUG=True .
docker run --detach --name flask-app --publish 80:8080 --rm flask-mini
docker ps
```
![docker-build](https://user-images.githubusercontent.com/51704179/236870791-77265dc9-0471-4fba-9668-66b015cdae0b.png)
## API

```bash
curl "http://localhost"
```

## Unit test

```bash
docker exec flask-app pytest
```

Code coverage

```bash
docker exec flask-app coverage run -m pytest
docker exec flask-app coverage report
```

Stop container

```bash
docker stop flask-app
```
