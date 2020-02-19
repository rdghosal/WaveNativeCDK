import os
from aws_cdk import aws_rds, aws_ec2, aws_s3, aws_s3_assets, aws_elasticbeanstalk, core


class WaveNativeStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        
        # Configure VPC for Elastic Beanstalk (EB) + RDS subnet
        vpc = aws_ec2.Vpc(self, "wave-native_vpc")

        # Configure RDS
        # TODO: add master_username, engine, instance_class
        rds = aws_rds.DatabaseInstance(
            self, "wave-native_rds",
            database_name="wave-native",
            vpc=vpc
            )

        # Configure Bucket and upload app files as S3 asset
        s3_bucket = aws_s3.Bucket(self, "wave-native_s3")
        s3_asset = aws_s3_assets.Assets(
            self, "wave-native.zip",
            path=os.path.join(os.getcwd(), "wave-native.zip")
            )

        # Instantiate source_bundle for EB
        source_bundle = aws_elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty()
        source_bundle.S3Bucket = s3_bucket.s3BucketName
        source_bundle.S3Key = s3_asset.s3ObjectKey

        # Configure EB
        # TODO: add EB to VPC
        eb = aws_elasticbeanstalk.CfnApplicationVersion(
            self, "wave-native_eb",
            application_name="WaveNative",
            source_bundle=source_bundle
            )