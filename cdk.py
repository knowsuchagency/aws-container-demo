#!/usr/bin/env python3
import logging
import os
import platform

import aws_cdk as cdk
from aws_cdk import (
    aws_lambda,
    aws_batch as batch,
    aws_ecs as ecs,
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

        openai_api_key = os.getenv("OPENAI_API_KEY", "")

        if not openai_api_key:
            logging.warning("OPENAI_API_KEY not set")

        build_args = {
            "OPENAI_API_KEY": openai_api_key,
        }

        self.lambda_function = aws_lambda.DockerImageFunction(
            self,
            "AwsContainerDemoFunction",
            code=aws_lambda.DockerImageCode.from_image_asset(
                directory=os.path.dirname(__file__),
                build_args=build_args,
            ),
            architecture=architecture,  # noqa
            memory_size=256,
            timeout=cdk.Duration.seconds(10),
            function_name="aws-container-demo",
        )

        self.function_url = self.lambda_function.add_function_url(
            auth_type=aws_lambda.FunctionUrlAuthType.NONE,
        )

        cdk.CfnOutput(
            self,
            "FunctionUrl",
            value=self.function_url.url,
        )

        self.container_definition = batch.EcsFargateContainerDefinition(
            self,
            "AwsContainerDemoContainerDefinition",
            image=ecs.ContainerImage.from_asset(
                directory=os.path.dirname(__file__),
                build_args=build_args,
            ),
            cpu=0.5,
            memory=cdk.Size.gibibytes(1),
        )

        self.job_definition = batch.EcsJobDefinition(
            self,
            "AwsContainerDemoJobDefinition",
            job_definition_name="aws-container-demo",
            container=self.container_definition,
        )


app = cdk.App()
AwsContainerDemoStack(
    app,
    "AwsContainerDemoStack",
)

app.synth()
