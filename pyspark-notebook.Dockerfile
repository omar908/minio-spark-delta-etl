# Use the existing image as the base
FROM quay.io/jupyter/pyspark-notebook:8f03304445ec

# Option 2: Install from a requirements file
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt