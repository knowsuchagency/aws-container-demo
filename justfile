# initialize development
init:
    npm i -g aws-cdk
    pkgx python@3.11 -m venv .venv ; .venv/bin/pip install -r requirements-dev.txt

# run the web server locally
fastapi:
    #!/bin/zsh
    . .venv/bin/activate
    cd src
    uvicorn app:app --reload

# deploy the stack
deploy:
    cdk deploy

# get weather via the CLI
get-weather location="San Francisco":
    .venv/bin/python src/entrypoint.py "{{location}}"
