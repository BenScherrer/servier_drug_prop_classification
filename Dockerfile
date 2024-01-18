FROM python:3.9


COPY ./requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn


COPY src /app/src
COPY models /app/models
COPY data /app/data
COPY templates /app/templates
COPY utils /app/utils

COPY main.py /app/main.py
COPY tests.py /app/tests.py

# Expose port 5000
EXPOSE 5000

WORKDIR /app/src
ENV PYTHONPATH=/app/src

# # Command to run the flask application
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]