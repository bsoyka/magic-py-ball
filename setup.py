import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='magic_py_ball',
      version='2.1.0',
      description='A magic 8 ball made entirely with Python.',
      url='http://github.com/bsoyka/magic-py-ball',
      author='Benjamin Soyka',
      author_email='bensoyka@icloud.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=setuptools.find_packages(),
      license='MIT',
      zip_safe=False)
