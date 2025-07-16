# setup.py

from setuptools import setup, find_packages

setup(
    name="groqcli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "requests",
        "groq",
        "dotenv",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "groqcli=groqcli.cli:cli",
            "groqcli-files=groqcli.module_each:cli_files",
        ],
    },
    author="MaSalope UwU",
    description="A kawaii CLI tool to chat with Groq LLMs in style 💖",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
