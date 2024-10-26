# استفاده از تصویر سبک Python
FROM python:3.8-slim

# نصب Flask
RUN pip install Flask

# تعیین دایرکتوری کاری
WORKDIR /app

# کپی فایل‌های پروژه به کانتینر
COPY . /app

# اجرای برنامه پایتون
CMD ["python3", "app.py"]
