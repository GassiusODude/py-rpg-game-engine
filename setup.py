from setuptools import setup, find_packages
from setuptools.extension import Extension

name = "py-rpg-game-engine"
release = "0.0"
version = "0.0.0"
extensions = []

setup(
    name=name,
    version=version,
    description="Keith Chow Role Playing Game",
    url="",
    author="Keith Chow",
    packages=find_packages(),
    tests_require=["pytest"],
    setup_requires=[],
    install_requires=["numpy"],
    dependency_links=[],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs/source')
            }
        },
    )
