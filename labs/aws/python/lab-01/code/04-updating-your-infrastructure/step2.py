import pulumi
import pulumi_aws as aws
import os
import mimetypes

bucket = aws.s3.Bucket("my-bucket",
    website={
        "index_document": "index.html"
})

filepath = os.path.join("site", "index.html")
mine_type = mimetypes.guess_type(filepath)
obj = aws.s3.BucketObject("index.html",
        bucket=bucket.name,
        source=pulumi.FileAsset(filepath),
        acl="public_read",
        content_type=mine_type
)

pulumi.export('bucket_name', bucket.bucket)
