FROM python:3.9

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn


COPY src /app/src

# Expose port 5000
EXPOSE 5000

ENV PYTHONPATH=/app/src

# TODO : make volumes readable by scripts

# Command to run the flask application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]