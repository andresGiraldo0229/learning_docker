# Usa la imagen base de Python slim
FROM python:3.12.5-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia solo el archivo de requisitos y instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Define variables de entorno para la base de datos
ENV MONGODB_HOST=mongodb
ENV MONGODB_PORT=27017

# Documenta el puerto en el que la aplicación se ejecuta
EXPOSE 8000

# Comando para ejecutar la aplicación
ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]