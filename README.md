# NovelAI-Data-Test

This project was created in Python using the Playwright API framework for the NovelAI community at the request of user Shincore. The purpose of this tool is to automate the process of testing the AI's output with the retry button against a given prompt and documenting what it outputs into a text file for further analysis before resetting back to the prompt (undoing the ai output).

A special thanks to the developers at https://playwright.dev/

## Installation

**1.)** If not already installed, go to https://www.python.org/downloads/ and download the latest version of Python for your OS. Make sure to install pip with the installation (check the box).

**2.)** If Playwright is not installed on your system run both of the following commands in command prompt or terminal if on MacOS.
```
pip install playwright
playwright install
```

**3.)** I recommend just downloading the Auto Retry Tool folder and dragging it to you desired location rather than keeping both the script and config text file loose.

**4.)** Once the above steps are done, navigate to your config_info.txt file and change the values in there. All lines need to be kept seperate as show in the placeholder texts within that document. Replace the first line with your login email, the second line with your password, and the third line with the **exact** name of the story you're using for testing. Once you have done this, save the document. Now you are ready to begin.

**Note:** None of the data within the config_info file is sent to me. If you are concerned about me having access to your login password, I don't. Feel free to look over the code within the AutoRetry.py file.

## Use

The goal behind my design of this script was to make it as user friendly as I could without going overboard. Because of that, you no longer need to use an editor to use the file and/or change variables. Upon running the script, it will no longer launch a browser window that the user can see. It runs in headless mode and this is just for further comfort.

**1.)** Upon executing the file, the user will recieve a prompt for how many passes they wish to do and will need to enter any number so long as it is in a format such as `200` and not something like `two-hundred`. After this, the script begins and will run until it reaches the number of passes.

**2.)** Once finished with the passes, it outputs a text file called ai_out.txt which will hold the AI's output. Each of the passes are indicated with a number to the left and the word "Output" such as `Output 1: The AI's text will be here`.

### What is a pass? (Non-technical)

A pass is the script clicking the retry button, grabbing the text the AI output, writing it in the text file, and then clicking the undo button to essentially reset the output back to the inital prompt. For a more indepth technical answer on how this code works, see the technical outline below.

## The Technical Outline

The script starts by logging into the user's NovelAI account. The user needs to specify their email and password information within the config_info.txt file within this folder. Fill in the place holder lines in the config file. This is due to Playwright launching the browser in a Chromium browser context, which won't have NovelAI autologin due to the cookies not being stored. Once the script logins the user, it selects the specified story which the user defines in the third line of the config_info.txt file. This is case sensitive and it is recommended the user copy and paste the exact title of the story from their browser to this config file.

The user will then recieve a prompt asking for the number of passes. The user will need to enter a number in the format indicated (ie 7, 140, 100, 200, etc). The number of passes the user specified will then execute in the for loop, esentially doing tests one after another. 

### What is a Pass? (Technical)
The script begins clicking the button that contains the text "Retry" and waits for the selector(s) .aiText to appear. Once the selectors appear, the script queries them, gets the text content from each selector (via for loop), and stores them in the variable aiOutput, making sure to concatinate each of the text contents onto the variable. It then writes the aiOutput varaible containing the text content to the text file ai_output.txt with each of the AI's output indicated with the pass number or as it shows in the text file:

```
Output 1: The AI output text is here and this is pass number 1.

```

Once finished, the script clicks the undo button. Once all aiText selectors are gone, it then finishes the pass and moves onto the next pass, which is the name process above.
