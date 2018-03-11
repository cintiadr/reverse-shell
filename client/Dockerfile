FROM alpine:3.7

RUN apk add --no-cache bash gawk sed grep bc coreutils curl wget && rm -rf /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
