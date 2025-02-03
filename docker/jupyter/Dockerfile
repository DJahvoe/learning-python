# Base image with Python
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install JupyterLab and any additional libraries
RUN pip install jupyterlab pandas numpy matplotlib

# Expose port 8888 for JupyterLab
EXPOSE 8888

# Command to start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
