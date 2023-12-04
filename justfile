# initialize development
init:
    npm i -g aws-cdk
    pkgx python@3.11 -m venv .venv ; .venv/bin/pip install -r requirements-dev.txt

# run the web server locally
litestar:
    #!/bin/zsh
    . .venv/bin/activate
    cd src
    litestar run --debug --reload
