from distutils import setup, find_namespace_packages
setup(
    name='LappisDistributions',
    version='0.0.1',
    author='Timothy Chapman',
    author_email='timothy.chapman98@outlook.com',
    url='https://github.com/LappisProblems/LappisDistributions',
    license='MIT',
    packages=find_namespace_packages(where='src'),
    description='A collection of selected distributions',
    install_requires=[]
)
