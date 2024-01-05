
# Envyr Base
FROM python:alpine

# Base Deps
RUN apk add --no-cache ca-certificates bash

# Os Level Deps if any

WORKDIR /envyr/app
# Install Type Specific Deps
ADD ./requirements.txt /envyr/app/requirements.txt
RUN pip install -r requirements.txt

ADD . /envyr/app
ENTRYPOINT ["python", "pipreqs.py"]
