FROM python:3.9

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install pip -U \
    & pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    & pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py","runserver" ,"0.0.0.0:8000"]