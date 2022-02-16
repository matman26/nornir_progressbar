from setuptools import setup, find_packages
setup(
  name = 'nornir_progressbar',
  py_modules = ['nornir_progressbar.plugins.runners.progressbar'],
  version = '0.1.0',
  license='apache-2.0',
  description = 'Multi-threaded runner plugin for nornir that prints a cute progress bar.',
  long_description = open('README.md','r',encoding='utf-8').read(),
  long_description_content_type="text/markdown",
  author = 'Matheus Augusto da Silva',
  author_email = 'a.matheus26@hotmail.com',
  url = 'https://github.com/matman26/nornir_progressbar',
  download_url = 'https://github.com/matman26/nornir_progressbar/archive/refs/tags/v0.1.1.tar.gz',
  keywords = ['nornir', 'tqdm', 'runner', 'plugin'],
  install_requires=[
      'nornir',
      'tqdm',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
