from setuptools import setup

setup(name='vid_station',
      version='0.1',
      description='video editing cli',
      include_package_data=True,
      install_requires=['moviepy'],
      scripts=['bin/clip'])
