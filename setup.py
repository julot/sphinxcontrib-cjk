from setuptools import setup, find_packages


description = (
    'Sphinx extension for kanji and hangul character support in LaTeX'
)

with open('README.rst', 'r', encoding='utf8') as f:
    long_description = f.read()

requires = ['Sphinx>=0.6']

keywords = [
    'sphinx',
    'sphinxcontrib',
    'cjk',
    'chinese',
    'japanese',
    'korean',
    'kanji',
    'hangul',
]

setup(
    name='sphinxcontrib-cjk',
    version='0.1',
    url='https://github.com/julot/sphinxcontrib-cjk',
    license='BSD',
    author='Andy Yulius',
    author_email='julot@gmail.com',
    description=description,
    long_description=long_description,
    keywords=' '.join(keywords),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
