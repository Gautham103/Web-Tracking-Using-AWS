# Web-Tracking-Using-AWS

The goal of this project is to create an web tracking service, which allows the user to register web pages to be downloaded into the storage and later be tracked by the backend service to identify modification of the web content. 

## Files Implemented:
1. lambda_function.py - downloads the web pages pointed to by the links and store inside the object storage. This function will be triggered by the API gateway

2. monitor_s3.py - monitors the change in the S3 storage. Each time a new web page being downloaded and stored in the S3 storage, this program will retrieve the content from the S3 storage, hash the page content with SHA256 algorithm. The hash value will be stored as an object in the same S3 storage, with the original URL + “/hash” as the key. This program will be running non-stop as a backend service in AWS EC2 machine

3. test_api.sh - script which takes the url as input and sends to API gateway

## Steps to run:
Run ./test_api.sh url. For example
```
./test_api.sh engineering.tamu.edu/cse/index.html
```

Start a EC2 machine and run the below program
```
python3 monitor_s3_bucket.py
```
