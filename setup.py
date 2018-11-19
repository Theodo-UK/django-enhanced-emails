from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="django-enhanced-emails",
    version="0.0.7",
    description="Enhanced email classes for Django",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Nathan Gaberel",
    author_email="nathang@theodo.co.uk",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Email",
    ],
    keywords="class based emails django",
    url="https://github.com/Theodo-UK/django-enhanced-emails",
    license="Theodo",
    packages=["enhanced_emails"],
    setup_requires=["setuptools>=38.6.0"],
    install_requires=["bs4", "django"],
)
