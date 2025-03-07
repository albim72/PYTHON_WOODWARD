FROM python:3.11
LABEL authors="Marcin Albiniak"

WORKDIR /app

COPY main.py data_procession.py data_struct.py /app/

RUN pip install pandas numpy

CMD ["python","main.py"]
