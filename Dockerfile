FROM python:latest

WORKDIR /home/thierry

COPY . .

EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]
#CMD ["python", "main.py"]