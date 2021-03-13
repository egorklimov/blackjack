from setuptools import find_packages, setup

setup(
    name='blackjack-lib',
    packages=find_packages(),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    entry_points={
        'console_scripts': ['blackjack-cli=blackjack.blackjack_cli:main'],
    },
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==5.3.5'],
    test_suite='tests',
)
