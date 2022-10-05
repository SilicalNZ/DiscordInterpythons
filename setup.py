import setuptools


requirements = []
with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()


setuptools.setup(
    name="DiscordInterpythons",
    version="0.3.10",
    license="Anyone may use this, but the origin (this project) must be credited",
    url="https://gihtub.com/SilicalNZ/DiscordInterpythons",
    description="A Pythonic wrapper for the Discord API specifically servicing Interaction Bots",
    long_description="This is a project meant to express the Discord Types as Python Classes and "
                     "build bots using exclusively the interactions features",
    author="SilicalNZ@gmail.com",
    install_requires=requirements,
    packages=["DiscordInterpythons.abcs", "DiscordInterpythons.handlers", "DiscordInterpythons.models", "DiscordInterpythons.providers"],
)
