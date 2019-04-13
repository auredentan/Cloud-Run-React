#!/usr/bin/env sh
set -eu

echo ${PORT}
envsubst '${PORT}' < /etc/nginx/conf.d/default.conf > /etc/nginx/conf.d/default.conf

exec "$@"
