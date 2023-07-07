# Flask mini
![flask-python-docker](https://github.com/danielurra/flask-init-mini/assets/51704179/7455583b-a4eb-43f3-ae34-98e2ec984dce)

This project is a **boilerplate** for future `Flask applications`, the OS we'll be using is Linux Ubuntu.

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
![coverage](https://user-images.githubusercontent.com/51704179/236873575-7dd5e38f-cd6e-49fe-898d-88f9504e81d8.png)

![report](https://user-images.githubusercontent.com/51704179/236873734-888b8372-6608-4f25-ad48-5ecd2179d591.png)

Stop container

```bash
docker stop flask-app
docker ps
```
![stop](https://user-images.githubusercontent.com/51704179/236874118-5317d034-0106-4e5a-9779-b82d50973442.png)

