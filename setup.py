
from setuptools import setup, find_packages

setup(name = 'MELKE',
      version = '1',
      description = 'Extract entities and relations from BIO-text',
      long_description = 'You can read brief description of MELKE here: \nhttps://github.com/im-na02/melke/',
      url = 'https://github.com/im-na02/melke/',
      license = 'MIT',
      packages = ['melke'],
      keywords = ['bio', 'text', 'NER', 'entity', 'relation'],
      py_modules = ['EntityRelation'],
      python_requires = '>=3',
      include_package_data = True,
      package_data = {'melke':['*']},
      zip_safe = False
    )

