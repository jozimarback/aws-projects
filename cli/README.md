# AWS CLI

Here you can get the link for your OS https://aws.amazon.com/cli/

## COMMANDS

### S3

List Buckets
```shell
aws s3 ls
```

Create bucket
```shell
aws s3api create-bucket --bucket my-bucket --region us-east-1
```

Copy from local to bucket
```shell	
aws s3 cp /path/to/source s3://bucket-name/ --recursive
```
