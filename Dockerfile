# Usa a imagem base do Python
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o conteúdo do backend para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pela aplicação
EXPOSE 5000

# Comando para iniciar o app
CMD ["python", "app.py"]
