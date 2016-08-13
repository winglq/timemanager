from setuptools import setup


setup(
    name = "TimeManager",
    version = "0.0.1",
    author = "Liu Qing",
    author_email = "winglq@gmail.com",
    packages=['timemanager'],
    entry_points = {
        'console_scripts': ['tomator=timemanager.timemanager:main'],
    }
)

