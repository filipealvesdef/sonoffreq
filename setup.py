from setuptools import setup, find_packages

setup(
    name='sonoffreq',
    description='A simple lib that sends requests to sonoff devices',
    version='0.1.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pycryptodome',
        'requests',
        'argparse',
    ],
    packages=find_packages(),
    scripts=['sonoff-req'],
    url='https://github.com/filipealvesdef/sonoffreq',
    zip_safe=False,
)
