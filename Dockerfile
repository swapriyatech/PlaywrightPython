FROM mcr.microsoft.com/playwright/python:v1.48.0-noble

WORKDIR /workspace
COPY pyproject.toml requirements.lock ./
RUN pip install --no-cache-dir -r requirements.lock
RUN pip install --no-cache-dir --no-deps -e .
COPY . .
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 RUN_BROWSER_TESTS=false
CMD ["python", "-m", "pytest"]
