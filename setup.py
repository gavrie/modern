from setuptools import setup

setup(
    name='modern',
    version='0.1.0',
    description='Modern Software Development Techniques with Python',
    packages=['modern'],
    install_requires=['pytest'],
    entry_points={
        'console_scripts': [
            'modern=modern:main',
        ],
    },
)
