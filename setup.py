import setuptools

with open("requirements.txt") as fp:
    install_requires = fp.read()

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="page-xml-draw",
    version="0.0.1",
    author="Lucas Sulzbach, João Okimoto",
    author_email="lucas@sulzbach.org",
    description="A CLI application that enables quick PAGE.XML files visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dokumente-br/page_xml_draw",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='>=3.6',
)
