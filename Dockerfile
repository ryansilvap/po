FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install pulp
CMD ["python", "simplex.py"]

