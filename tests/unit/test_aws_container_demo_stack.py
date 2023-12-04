import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_container_demo.aws_container_demo_stack import AwsContainerDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_container_demo/aws_container_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsContainerDemoStack(app, "aws-container-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
