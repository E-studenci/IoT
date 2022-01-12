FROM redis:6.2.6

COPY redis.conf /usr/local/etc/redis/redis.conf

COPY tls/redis.key /data/
COPY tls/redis.crt /data/

EXPOSE 6379

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]