[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![CI](https://github.com/sander76/mspyteams/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/sander76/mspyteams/branch/master/graph/badge.svg)](https://codecov.io/gh/sander76/mspyteams)



# MsPyTeams

A sansio card creation library for sending cards to Microsoft Teams.

mspyteams requires python 3.6 and up.

## Installation


`python3 -m pip install mspyteams`

Being a sans-io library this installs only the card composition library, which in the end returns a valid card dict, which can be send as a json payload using any http client library of your liking.

Currently the `aiohttp` client is implemented as an option. To install:

`python3 -m pip install mspyteams[aiohttp]`


## Goals

There are more ms teams card libaries available, like [pymsteams](https://github.com/rveachkc/pymsteams) and [msteams](https://github.com/johanjeppsson/msteams), and I have thought of adapting them to my needs by doing pull requests etc.
However, my goals were to provide a library that complies with pep8 (no camelcasing), doing an sans-io implementation, using flit, trying to get github actions running in combination with nox and learning some more along the way. So to do that effectively, I thought it would be best to do a library from scratch. And there you go..

## Usage

For a complete description of the Card API go [here](https://docs.microsoft.com/en-us/outlook/actionable-messages/message-card-reference)

