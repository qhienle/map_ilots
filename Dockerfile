FROM python:latest
WORKDIR /app
RUN pip install --no-cache-dir pandas folium geopy
COPY main.py /app/
CMD ["python", "/app/main.py", '&&', 'bash']