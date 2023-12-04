# initialize development
init:
    pkgx python@3.11 -m venv .venv ; .venv/bin/pip install -r requirements-dev.txt

# run the web server locally
litestar:
    #!/bin/zsh
    . .ven/bin/activate
    cd src
    litestar run --debug --reload
