[![Python application](https://github.com/ceste/hello_docker/actions/workflows/main.yml/badge.svg)](https://github.com/ceste/hello_docker/actions/workflows/main.yml)

# hello_docker

Almost a whole CI/CD pipeline repo that show to build a docker image, publish it and deploy it. I will keep updating this repo until it reaches the complete CI/CD pipeline.


## Create a virtual environment

```python
pyhton -m venv .env
```

## Activate the virtual environment

```python
source .env/bin/activate
```

## Clone this repo

```git
git clone https://github.com/ceste/hello_docker.git
```

## Install the requirements

```python
pip install -r requirements
```

## Run the script

```python
python main.py --name nadia
```

```python
python main.py --name sarah
```

## Build docker image

```docker
docker build -t docker-greeting .
```

## Run docker image

```docker
docker run docker-greeting python main.py --name cst
```

## Tag docker image

To do this, you need to have a repo in docker hub. Essentially this will map you local image to docker hub repo.

Syntax:

```docker
docker tag local-image:tagname new-repo:tagname
```

```docker
docker tag docker-greeting:latest chandrasutrisnotjhong/docker-greeting:latest
```

## Push image to docker hub

Make sure you login using your docker account

Syntax:
```docker
docker push new-repo:tagname
```

```docker
docker push chandrasutrisnotjhong/docker-greeting:latest
```

## Run image from the repo (should run it from your production environment)

If the image is not available on local, it will download the image first and then run it.

```docker
docker run -it chandrasutrisnotjhong/docker-greeting python main.py --name abc
```

If there is new build, pull the latest build and then run above command:

```docker
docker pull chandrasutrisnotjhong/docker-greeting:latest
```

## Push local image to Heroku

Login to Heroku 

```
heroku login
```

Login to Heroku Container Registry

```
heroku container:login
```

Create an app on Heroku 

```heroku
heroku create <name-for-your-app>
```

```heroku
heroku create cst-hello-docker
```

Push the container into Heroku

```heroku
heroku container:push web --app <name-for-your-app>
```

```heroku
heroku container:push web --app cst-hello-docker
```

Deploy the container

```heroku
heroku container:release web <name-for-your-app>
```

```heroku
heroku container:release web --app cst-hello-docker
```

Open your app 

```
https://<name-for-your-app>.herokuapp.com/
```



Deploy Docker Image to Heroku App is not certified by GitHub. It is provided by a third-party and is governed by separate terms of service, privacy policy, and support documentation.
  


References:
- https://docs.github.com/en/actions/learn-github-actions#using-the-checkout-action
- https://canovasjm.netlify.app/2021/01/12/github-secrets-from-python-and-r/
- https://github.com/marketplace/actions/deploy-docker-image-to-heroku-app 
- https://github.com/marketplace/actions/build-push-and-release-a-docker-container-to-heroku
  

