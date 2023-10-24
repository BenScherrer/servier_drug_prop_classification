FROM python:3.9


COPY ./src/requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn


COPY src /app/src

# Expose port 5000
EXPOSE 5000

WORKDIR /app/src
ENV PYTHONPATH=/app/src

# Command to run the flask application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]