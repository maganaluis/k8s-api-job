FROM python:3.7.3-stretch

RUN mkdir /job
WORKDIR /job
ADD job.py /job/job.py
RUN pip install kubernetes

CMD ["python", "/job/job.py"]