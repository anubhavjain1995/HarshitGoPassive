import  boto3

s3 = boto3.client('s3')
response = s3.upload_file('tests.py','gopassive','data/test.py')

bucket_location = boto3.client('s3').get_bucket_location(Bucket='gopassive')
object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
    bucket_location['LocationConstraint'],
    'gopassive',
    'data/test.py')
print(object_url)