from setuptools import setup

setup(name='vid_station',
      version='0.1',
      description='video editing cli',
      include_package_data=True,
      install_requires=['moviepy'],
      entry_points={
            'console_scripts': ['vedit=vid_station.command_line:main'],
      })
