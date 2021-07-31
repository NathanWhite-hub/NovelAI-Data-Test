# NovelAI Auto Retry Tool

This is a Python script automates the process of clicking the retry button of your selected story, grabbing the output text by the AI, writing it to a text file, then removing the AI output text, and repeating. This was created at the request of Shincore on the NovelAI discord to test prompts output by the AI.

A special thanks to the developers at https://playwright.dev for their great library.

## Installation

**1.)** If not already installed, go to https://www.python.org/downloads/ and download the latest version of Python for your OS. Make sure to install pip with the installation (check the box).

**2.)** Run both of the following commands in command prompt or terminal if on MacOS.
```
pip install playwright
playwright install
```

**3.)** Download the Auto Retry folder from the repo.

**4.)** Open the config_info text file and paste in your email, password, and the title of the story you are testing on. Make sure it is all on its own line where indicated in the text file. Replace the entire line with your information including the `**` (ie `**PASTE LOGIN EMAIL HERE**`).

## Use

Run the AutoRetry.py script which will display a command window and some nice ascii art at the top. From here, the user does not need to input anything and this window will print commands for each pass. A pass in this context is one generation of the AI and then the removal of the output. Currently, the script will do 100 passes then end.
