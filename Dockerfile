FROM python:latest-slim
WORKDIR /app
RUN pip install --no-cache-dir pandas folium
COPY . .
CMD bash