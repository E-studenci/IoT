FROM mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=mongo
MONGO_INITDB_DATABASE: iotDB

COPY scripts/* /docker-entrypoint-initdb.d/mongo-init.js

EXPOSE 27017