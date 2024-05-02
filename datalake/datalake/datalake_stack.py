from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3
)
from constructs import Construct

class DatalakeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "DatalakeQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        datalake_bucket = s3.Bucket(self, "datalake-aws-s3",
            versioned=False,
            removal_policy=RemovalPolicy.RETAIN
        )

