# Cloud run, cloud build sample app


* A frontend (react)
* A backend (python)


## To come
* Cloud functions (with versionning)


## Quickstart

### docker-compose
You need docker and docker-compose installed and just run

```bash
    docker-compose up --build
```

The developement will hot reload if source change but for the react app you'll need to run yarn build by hand to update the page.

### Skaffold


```bash
    skaffold dev
```
This will allow you to develop and the images 

To regenerate the yamls and skaffold.yaml to reflect the docker-compose you will need kompose and do

```bash
    kompose convert -o k8s
    skaffold init
```
