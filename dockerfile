FROM Ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD python3 app.py