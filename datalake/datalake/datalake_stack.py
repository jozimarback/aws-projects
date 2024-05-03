from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    # aws_sqs as sqs,
    aws_glue as glue,
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

        glue_database = glue.CfnDatabase(
            self, "datalake-aws-database",
            catalog_id="058264114498",
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                location_uri=f"s3://{datalake_bucket.bucket_name}/bronze",
                name="datalake-aws-database"
            )
        )

        # Define the Glue crawler
        # glue_crawler = glue.CfnCrawler(
        #     self, "datalake-aws-crawler",
        #     role="arn:aws:iam::058264114498:role/service-role/AWSGlueServiceRole-my-role",
        #     database_name=glue_database.database_input.name,
        #     targets={"s3Targets": [{"path": f"s3://{datalake_bucket.bucket_name}/bronze/*"}]},
        #     table_prefix="bronze-"
        # )

        glue_table = glue.CfnTable(
            self, "bronze",
            database_name=glue_database.database_input.name,
            catalog_id=glue_database.catalog_id,
            table_input=glue.CfnTable.TableInputProperty(
                name="bronze",
                storage_descriptor=glue.CfnTable.StorageDescriptorProperty(
                    input_format="parquet",
                    location=f"s3://{datalake_bucket.bucket_name}/bronze"
                )
            )
        )

        glue_table.node.add_dependency(glue_database)

