FROM python:3-alpine
COPY MainScores.py /MainScores.py
COPY utils.py /utils.py
COPY err.txt /err.txt
COPY scores.txt /scores.txt
RUN pip install flask
EXPOSE 4444
CMD ["python", "/MainScores.py", "1"]
