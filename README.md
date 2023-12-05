## Overview

This repository demonstrates how to build a Docker container for deployment on AWS Lambda and AWS Batch. It showcases a flexible setup where a FastAPI ASGI application can be converted for Lambda execution using Mangum, and also supports direct Lambda invocation.

## Features

- **AWS Lambda Compatibility:** Run as a web application via FastAPI and Mangum or invoke the Lambda function directly.
- **AWS Batch Integration:** Utilize AWS Batch for managing and running batch computing workloads.
- **Docker Support:** Build and deploy using Docker containers.

## Prerequisites

- AWS Account
- Docker installed
- Node.js and npm installed
- Python 3.11
- AWS CDK

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:knowsuchagency/aws-container-demo.git
   cd aws-container-demo
   ```

2. **Initialize the environment:**

   Use the `justfile` for environment setup:

   ```bash
   just init
   ```

## Usage

### Running Locally

- **Start FastAPI server:**

  ```bash
  just fastapi
  ```

### Deployment

- **Deploy to AWS:**

  ```bash
  just deploy
  ```

### Command-Line Interface

- **Get weather information:**

  ```bash
  just get-weather "your-location"
  ```

## Repository Structure

- `cdk.py`: Defines the AWS CDK stack for deploying the application.
- `justfile`: Contains commands for environment setup, local development, and deployment.
- `Dockerfile`: Specifies the Docker container configuration.
- `src/`: Contains the source code for the application.
  - `app.py`: FastAPI application setup.
  - `entrypoint.py`: Entry point for AWS Lambda and CLI.
  - `cli.py`: CLI for getting weather information.
  - `lambda_handler.py`: Lambda handler with Mangum for FastAPI integration.


## License

[MIT](LICENSE)
