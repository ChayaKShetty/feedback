FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir -r requriments.txt
EXPOSE 5000
ENV FLASK_APP=app.python
CMD ["flask","run","--host=0.0.0.0"]