#!/bin/bash

if [ $# -eq 3 ]
then
	docker network create -d $1 $2 $3
else
	docker network create -d $1 $2
fi
