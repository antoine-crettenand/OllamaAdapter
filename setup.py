from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="ollama_adapter",
    version="0.1.0",
    author="Antoine Crettenand",
    author_email="antoine.crettenand@gmail.com",
    description="An interface for interacting with a local or online LLM using langchain_ollama.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antoinecrettenand/OllamaAdapter",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "langchain",
        "langchain-ollama",
        "strictjson"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    # Uncomment and modify the following if you have console scripts:
    # entry_points={
    #     "console_scripts": [
    #         "ollama_adapter=ollama_adapter.cli:main",
    #     ],
    # },
    keywords="LLM langchain ollama adapter",
)