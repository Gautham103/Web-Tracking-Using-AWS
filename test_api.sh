#!/bin/sh

aws configure set aws_access_key_id $1
aws configure set aws_secret_access_key $2
aws configure set default.region us-east-2

aws apigateway test-invoke-method --rest-api-id jatiyhpnlj --resource-id mp0z6k --http-method GET --path-with-query-string "/user?id=$3"

