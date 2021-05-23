<div align="center">
  <img src="/Images/dsi.png" alt="dsi-logo" width="150px"/>
</div>

<h1 align="center"> DiscordScraperCLI</h1>

<p align="center">A simple command line interface tool that scrapes messages from any discord channel.<p>

<hr>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing Using pip](#installing-using-pip)
  - [Installing the Project Directly](#installing-the-project-directly)
- [Usage](#usage)
  - [Getting a Channel's ID](#getting-a-channels-id)
  - [Getting Authorization Tokens](#getting-authorization-tokens)
- [Options](#options)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## Features

```bash
dsi get_json -a 38fl3hd9co -c 10083930 -d -f example.json
```

Prints the messages from the discord channel with ID `10083930` to console:

```JSON
{
  "this": "is",
  "some": "random",
  "ass": "JSON",
  "for": "now..."
}
```

And saves a full detalied list of messages to the file `example.json` in your machine's Download folder.

## Getting Started

### Prerequisites

First, ensure that your computer has Python with at least ***version 3.6*** installed. You can check your Python version number in your terminal using:

```properties
python --version
```

If you don't have Python or need to update to a newer version, [check out this link](https://www.python.org/downloads/)!

Next, ensure that `pip` is installed as well (newer version of Python should come with pip preinstalled). If you're unsure if your device has pip, [check out this link](https://pip.pypa.io/en/stable/installing/)!

### Installing Using pip

Coming soon... 8)

### Installing the Project Directly

After downloading the project, navigate to `/DiscordScraperCLI` directory in your terminal.

Next, run:

```properties
pip install .
```

This command will install all the neccessary packages for DiscordScraperCLI to work!

## Usage

### Getting a Channel's ID

Make sure you have a Discord account and that you are  logged into the ***web app version*** of [Discord](https://discord.com) and that you either have ***Google Chrome***, ***FireFox***, or any other browser that has access to ***Developer Tools***.


### Getting Authorization Tokens


## Options

## Credits

DiscordScraperCLI by Luke Sirand ([@ljsirand](https://twitter.com/sirandlj) on Twitter)

Logo by [@meeanin](https://twitter.com/sirandlj) on Instagram

## Acknowledgments

