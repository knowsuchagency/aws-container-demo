#!/usr/bin/env python3
import os
import subprocess

from cli import cli

if os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    # we're running in AWS Lambda
    subprocess.run(["/lambda-entrypoint.sh", "lambda_handler.handler"])
else:
    cli()
