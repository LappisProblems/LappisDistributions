from distutils.core import setup
setup(
    name='LappisDistributions',
    version='0.0.1',
    author='Timothy Chapman',
    author_email='timothy.chapman98@outlook.com',
    url='https://github.com/LappisProblems/LappisDistributions',
    license='MIT',
    packages=['LappisDistributions'],
    description='A collection of selected distributions',
    install_requires=[
    'python>=3.6.0',
    'numpy>=1.0.0',
    'math>=3.0.0',
    'scipy>=1.0.0'
    ]
)
