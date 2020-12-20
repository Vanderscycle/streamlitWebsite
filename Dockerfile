# base image
FROM python:3.7-slim
# basic metadata info
LABEL maintainer="Henri Vandersleyen" email="hvandersleyen@gmail.com"
# exposing container port to be the same as streamlit default port

EXPOSE 8051
# set work directly so that paths can be relative
WORKDIR /usr/src/app
# copy to make usage of caching
COPY requirements.txt ./
#install dependencies
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
# copy code itself from context to image
COPY . .
CMD streamlit run ./src/app.py --server.port $PORT