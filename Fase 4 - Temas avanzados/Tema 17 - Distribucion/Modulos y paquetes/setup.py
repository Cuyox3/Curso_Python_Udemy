from setuptools import setup, find_packages

setup(
    name='Mensajes',
    version='4.0',
    description='Un paquete para saludar y despedir',
    author='Héctor Costa Guzmán',
    author_email='hola@hektor.dev',
    url='https://www.hektor.dev',
    packages=find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires=[paquete.strip()
                      for paquete in open("requirements.txt").readlines()]
)
