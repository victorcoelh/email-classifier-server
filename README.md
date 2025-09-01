# Email Classifier - Backend Server

An API built with FastAPI for classifying e-mails, and suggesting automated answers to them. Uses
the OpenAI API and Google Gemini for both classification and answer suggestion.

### Build/Installation

You can build and run the API using Docker. First, make sure you have a working
installation of Docker (instructions on [docs.docker.com](https://docs.docker.com/engine/install/)).

Then, you can build the API with the following command:

```docker build --tag email-api .```

If you do not wish to run the API with Docker, you can also run it using the [UV](https://docs.astral.sh/uv/getting-started/installation/)
package manager. UV is a Rust-based package manager for Python that simplifies virtual environment
and package management, while also providing faster installs and builds than pip.

Once you install UV, you can install all dependencies for the project in an isolated virutal environment
with the following command:

```uv sync```

UV will automatically create a .venv folder and install all dependencies for you.

### Usage

With docker:

```docker run email-api```

With UV:

```uv run fastapi run src/server.py```
