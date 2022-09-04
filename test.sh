#!/bin/bash

echo "hello"
docker stack deploy -c test.yml test
