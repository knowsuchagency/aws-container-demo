#!/usr/bin/env python3
import os
import platform

import aws_cdk as cdk
from aws_cdk import (
    aws_lambda,
)
from constructs import Construct


class AwsContainerDemoStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        architecture = (
            aws_lambda.Architecture.ARM_64
            if "arm" in platform.machine()
            else aws_lambda.Architecture.X86_64
        )

        self.lambda_function = aws_lambda.DockerImageFunction(
            self,
            "AwsContainerDemoFunction",
            code=aws_lambda.DockerImageCode.from_image_asset(
                directory=os.path.dirname(__file__)
            ),
            architecture=architecture,  # noqa
            memory_size=1024,
            timeout=cdk.Duration.seconds(30),
        )

        self.function_url = self.lambda_function.add_function_url(
            auth_type=aws_lambda.FunctionUrlAuthType.NONE,
        )

        cdk.CfnOutput(
            self,
            "FunctionUrl",
            value=self.function_url.url,
        )


app = cdk.App()
AwsContainerDemoStack(
    app,
    "AwsContainerDemoStack",
)

app.synth()
