FROM python:latest
WORKDIR /app
RUN pip install --no-cache-dir pandas folium
COPY main.py /app/
#CMD ["python", "/app/main.py"]
CMD bash