FROM alpine:3.7

RUN apk add --no-cache python && rm -rf /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
COPY server.py /server.py

RUN chmod a+x /entrypoint.sh
RUN chmod a+x /server.py

EXPOSE 8888

ENTRYPOINT ["/entrypoint.sh"]
