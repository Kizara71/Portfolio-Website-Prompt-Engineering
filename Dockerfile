FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 7860

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create a non-root user with UID 1000 (Required for Hugging Face Spaces)
RUN useradd -m -u 1000 user

# Copy project files
COPY . /app/

# Create staticfiles and media directories, and change ownership of the entire /app directory
RUN mkdir -p /app/staticfiles /app/media \
    && chown -R user:user /app/

# Switch to the non-root user
USER user

# Collect static files
RUN python manage.py collectstatic --noinput

# Make sure we use port 7860 and create admin if requested
CMD python manage.py migrate && python create_admin.py && gunicorn portfolio.wsgi:application --bind 0.0.0.0:7860
