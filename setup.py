from setuptools import setup

install_requires = []
with open("./requirements.txt", encoding="utf-8") as requirements_file:
    reqs = [r.strip() for r in requirements_file.readlines()]
    reqs = [r for r in reqs if r and r[0] != "#"]
    for r in reqs:
        install_requires.append(r)

setup(
    name="easy_context",
    version="0.1",
    packages=["easy_context"],
    install_requires=install_requires,
    url='https://github.com/jzhang38/EasyContext/
    license='Apache License 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
