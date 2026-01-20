FROM selenium/standalone-chrome:4.18

USER root

# Устанавливаем Python
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-distutils \
    curl \
    && ln -sf /usr/bin/python3.10 /usr/bin/python \
    && ln -sf /usr/bin/pip3 /usr/bin/pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/seluser/autotests

# Копируем скрипт запуска
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# Копируем зависимости и проект
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Меняем владельца
RUN chown -R seluser:seluser /home/seluser/autotests

USER seluser

# Используем наш скрипт как точку входа
ENTRYPOINT ["./docker-entrypoint.sh"]