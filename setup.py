from setuptools import setup

setup(
    name = 'snapshotalyzer_3000',
    version = '0.1',
    author = "Yevgen Reus",
    author_email = "yevgen.reus@gmail.com",
    description = "SnapshotAlyzer 3000 is a tool to manage AWS EC2 snapshots",
    licence = "GPLv3+",
    packages = ['shotty'],
    url = "https://github.com/zaMedvedem/snapshotalyzer-3000",
    install_requires = [
    'click',
    'boto3'
    ],
    entry_points = '''
    [console_scripts]
    shotty = shotty.shotty:cli
    ''',
)
