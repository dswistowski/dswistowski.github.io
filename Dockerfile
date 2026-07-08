FROM python:3.14-slim

LABEL org.opencontainers.image.source="https://github.com/dswistowski/dswistowski.github.io"

WORKDIR /app

RUN pip install --no-cache-dir click==8.4.2 jinja2==3.1.6 pyyaml==6.0.3

COPY build.py /app/build.py
COPY templates /app/templates

ENTRYPOINT ["python", "/app/build.py", "latex"]
