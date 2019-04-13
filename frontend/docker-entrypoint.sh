#!/usr/bin/env sh
set -eu

envsubst '${PORT}' < /etc/nginx/conf.d/default.conf > /etc/nginx/conf.d/default.conf

exec "$@"