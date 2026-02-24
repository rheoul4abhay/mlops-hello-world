# Stage 1
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .


# Create a virtual environment inside the builder
RUN python -m venv /app/venv

# Install dependencies inside the venv
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /app/venv /app/venv

# Copy the application code
COPY . .

# To activate venv automatically, i.e
# BEFORE: PATH=/usr/local/bin:/usr/bin:/bin
# AFTER : PATH=/app/venv/bin:/usr/local/bin:/usr/bin:/bin
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 5001

CMD ["python", "app.py"]