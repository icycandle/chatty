# chatty

## install
```
pip install pip-tools
pip-compile && pip-sync
```

## run redis-server
`docker run --name dj-chat-redis -p 6380:6379 -d arm64v8/redis`

## run cassandra
`docker run --name cassandra-1 -d -e CASSANDRA_BROADCAST_ADDRESS=192.168.0.1 -p 7070:7070 -p 9042:9042 -p 9160:9160 cassandra`

## init DB
`python manage.py syncdb`

## run django
`python manage.py runserver`
