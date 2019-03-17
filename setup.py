from setuptools import setup
import os

version = "1.0.0"

requirements = [
      "selenium == 3.141.0"
]


setup(name='comcast-outage-detector',
      version=version,
      description='Browser automation to detect for Comcast outages in your area',
      author='Marko SomethingHardToSpell Smith',
      author_email='marko_pavlovic87@yahoo.com',
      url='https://github.com/UncleMarko922/ComcastOutageDetector',
      install_requires=requirements,
      packages=['comcast_outage_detector'],
)