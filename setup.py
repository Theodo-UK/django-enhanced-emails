from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='django-enhanced-emails',
    version='0.0.2',
    description='Enhanced email classes for Django',
    long_description=readme(),
    author='Nathan Gaberel',
    author_email='nathang@theodo.co.uk',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Email',
    ],
    keywords='class based emails django',
    url='https://github.com/Theodo-UK/django-enhanced-emails',
    license='MIT',
    packages=[
        'enhanced_emails',
    ],
    install_requires=[
        'bs4',
        'django',
    ]
)
