FROM public.ecr.aws/lambda/python:3.11

ARG OPENAI_API_KEY=""

ENV OPENAI_API_KEY=${OPENAI_API_KEY}

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENTRYPOINT [ "./entrypoint.py" ]
