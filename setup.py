import setuptools

setuptools.setup(
    name="stravaboard",
    version="1.0.0",
    author="David Zhang",
    author_email="dyzhang32@gmail.com",
    description="A simple dashboard for displaying and analysing Strava data",
    url="https://github.com/dzhang32/stravaboard",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
