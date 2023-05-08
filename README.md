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
docker container ls
docker ps
```
![docker-build](https://user-images.githubusercontent.com/51704179/236870791-77265dc9-0471-4fba-9668-66b015cdae0b.png)
![docker-run](https://user-images.githubusercontent.com/51704179/236872077-884b0925-989f-4ff6-9ece-551297cba46d.png)
![docker-container-ls](https://user-images.githubusercontent.com/51704179/236872042-a01d2d16-c49f-47dc-977f-206a65f1da29.png)

## API

```bash
curl "http://localhost"
```
![curl](https://user-images.githubusercontent.com/51704179/236872616-806e6b67-a2d2-404a-b659-5e9666b07b47.png)

## Unit test

```bash
docker exec flask-app pytest
```
![pytest](https://user-images.githubusercontent.com/51704179/236872958-c0233897-961a-4e02-84a8-0e6d2060b44f.png)

Code coverage

```bash
docker exec flask-app coverage run -m pytest
docker exec flask-app coverage report
```

Stop container

```bash
docker stop flask-app
```
