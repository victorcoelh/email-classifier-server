FROM ghcr.io/astral-sh/uv:python3.13-alpine
WORKDIR /api
COPY . .

#RUN export PYTHONPATH="${PYTHONPATH}:/api/"
RUN uv sync --no-group dev
RUN python -m compileall -q ./src/
EXPOSE 8080

ENTRYPOINT ["uv", "run", "--no-group", "dev", "uvicorn", \
"src.server:app", "--host", "0.0.0.0", "--port", "8080"]
