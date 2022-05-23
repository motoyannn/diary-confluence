# Dairy Confluence

## Get start

```shell
docker-compose build --no-cache
docker-compose up -d

# ps check
docker-compose ps
```

## deployment

```shell
docker-compose exec app bash

# inside of the python container
cd diary-confluence
chalice deploy
```

## delete all stack

```shell
docker-compose exec app bash

# inside of the python container
cd diary-confluence
chalice delete
```

## Run locally

```shell
docker-compose exec app bash

# inside of the python container
cd diary-confluence
chalice local --stage=local --host=0.0.0.0
```
