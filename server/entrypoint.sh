#!/bin/sh

set -eu

echo Starting server
exec nc -nvl 8888
