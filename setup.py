import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sanakirju-simplifier",
    version="0.1.0",
    author="stscoundrel",
    description="Simplify Sanakirju XML dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stscoundrel/sanakirju-simplifier/",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    package_data={"": ["**/*.xml"]},
)
