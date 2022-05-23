# Infrastructure

- not work on m1 mac

## Deploy

```shell
docker-compose exec app bash

# in the container
cd infrastructure

# list stack
cdk ls

# deploy
cdk deploy Automation--MainStack
```
