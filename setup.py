import setuptools

setuptools.setup(
    name="ObfuscateProtect",
    version="0.0.1",
    author="James Stevenson",
    author_email="hi@jamesstevenson.me",
    description="A tool for quickly obfuscating sensitive, violent, or extremist text to protect the researcher or analyst viewing the content.",
    long_description="A tool for quickly obfuscating sensitive, violent, or extremist text to protect the researcher or analyst viewing the content.",
    long_description_content_type="text/markdown",
    url="https://github.com/CartographerLabs/ObfuscateProtect",
    packages=["ObfuscateProtect"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
)