import setuptools

with open("requirements.txt", 'r') as fp:
    install_requires = fp.read()

with open("README.md", 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name="page-xml-draw",
    version="0.0.1",
    author="Lucas Sulzbach, João Okimoto",
    author_email="lucas@sulzbach.org",
    description="A powerful CLI tool for visualization and encoding of "
                "PAGE-XML files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GBN-DBP/page_xml_draw",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    package_data={
      "": ["schema.json"]
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Utilities",
    ],
    entry_points={
      "console_scripts": [
        "page-xml-draw=page_xml_draw:main",
      ]
    },
    python_requires='>=3.6',
)
