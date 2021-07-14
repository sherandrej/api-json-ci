FROM python:3
MAINTAINER Andrei Sharstniou 'sherandrej@gmail.com'
#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#RUN python3 get-pip.py
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y
RUN apt-get install -y python-pip 
ADD requirements.txt /
RUN pip install -r requirements.txt
#RUN pip install virtualenv
#RUN pip install requests
ADD main.py /
#EXPOSE 5000
CMD ["python3", "./main.py"]
