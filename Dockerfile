FROM python:3.10-slim

WORKDIR /app

COPY model/xgboost_model.pkl app/front.py app/House.py app/main.py requirements.txt start.sh /app/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh

CMD ["./start.sh"]
