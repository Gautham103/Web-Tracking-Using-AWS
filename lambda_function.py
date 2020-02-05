import json
import boto3
from botocore.exceptions import ClientError
import urllib.request

def lambda_handler(event, context):

    url = event["id"]
    url_new = "http://" + url

    response = urllib.request.urlopen(url_new)
    webContent = response.read()

    f = open('/tmp/logs.txt', 'wb')
    f.write(webContent)
    f.close

    print ("THIS IS THE EVENT PARAMETER")
    print ((event["id"]))

    s3_client = boto3.client('s3')

    file_name = "#"+ event["id"]

    with open ("/tmp/log.txt", "wb") as f:
        f.write(webContent)
    try:
        response = s3_client.upload_file("/tmp/log.txt", "python-example-bucket", file_name)
    except ClientError as e:
        logging.error(e)
        return False

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! {}' .format (url))
    }
