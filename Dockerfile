FROM public.ecr.aws/lambda/python:3.11 as base

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENTRYPOINT [ "./app.py" ]
