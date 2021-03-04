#!/usr/bin/env bash

images=(
    'quay.io/guanwang/server-name:v1.0'
)
for image in ${images[@]}; do
    docker build -t "$image" .
    docker push "$image"
done
