# SPDX-FileCopyrightText: 2022 Renaissance Computing Institute. All rights reserved.
# SPDX-FileCopyrightText: 2023 Renaissance Computing Institute. All rights reserved.
# SPDX-FileCopyrightText: 2024 Renaissance Computing Institute. All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-License-Identifier: LicenseRef-RENCI
# SPDX-License-Identifier: MIT

# This Dockerfile is used to build THE apsviz-ui-data python image

FROM python:3.12.6-slim

# update the image base
RUN apt-get update && apt-get -y upgrade

# update pip
RUN pip install --upgrade pip

# clear the apt cache
RUN apt-get clean

# get some credit
LABEL maintainer="powen@renci.org"

# Copy in just the requirements first for caching purposes
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

## create a new non-root user and switch to it
#RUN useradd --create-home -u 1000 nru
#USER nru

# Create the directory for the code and cd to it
WORKDIR /test/geopoints.url

# Copy in the rest of the code
COPY . .

# start the service entry point
ENTRYPOINT ["/bin/sh", "-c", "sleep infinity"]
