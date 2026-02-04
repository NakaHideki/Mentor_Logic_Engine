# Use Python 3.11 lightweight version
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency definition first (for better caching)
COPY pyproject.toml .
# Also copy src and README because pip install -e needs them
COPY src/ src/
COPY README.md .

# Install dependencies including dev tools
# -e means "editable" mode (changes in host reflect in container)
RUN pip install --no-cache-dir -e ".[dev]"

# Copy the rest of the application
COPY . .

# Default command: keep the container running
CMD ["tail", "-f", "/dev/null"]
