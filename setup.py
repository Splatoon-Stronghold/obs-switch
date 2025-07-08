from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="obs_switch",
    version="0.0.1",
    author="Jason Jiménez Cruz",
    author_email="jasonjimenezcruz@gmail.com",
    description="OBS Studio and Nintendo Switch controller integration via Kafka",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Splatoon-Stronghold/obs-switch",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "confluent-kafka>=2.0.0",
        "python-dotenv==1.1.1",
        "websocket-client==1.7.0",
        "python-engineio==4.5.1",
        "python-socketio==5.8.0",
        "simple-websocket==1.1.0",
        "argparse>=1.4.0",
        "typing-extensions>=4.0.0",
    ],
    entry_points={
        "console_scripts": [
            "obs-switch=obs_switch.cli:main",
        ],
    },
)