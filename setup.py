from setuptools import setup

setup(name='cbpi4-audio',
      version='0.0.2',
      description='CraftBeerPi4 Audio Plugin',
      author='DaSchaef',
      url='https://github.com/DaSchaef/cpbi-audio',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-audio': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-audio'],
      long_description="Plays audio files",
      long_description_content_type='text/markdown',
      install_requires=[
            'playsound'
      ],
     )