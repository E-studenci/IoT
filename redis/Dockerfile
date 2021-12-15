FROM redis:6.2.6

COPY redis.conf /usr/local/etc/redis/redis.conf

ENV REDIS_PASSWORD redis

EXPOSE 6379

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf", "--requirepass", "\"$REDIS_PASSWORD\"" ]