# Lexi-Boost
A CI pipeline plug-in to validate generated code before merge.

## Usage
1. Build the Docker image: `docker build -t lexi-boost:ci .`
2. Run the image: `docker run -it lexi-boost:ci /path/to/code/file.py`
3. The image will output a JSON with the compilation status.
