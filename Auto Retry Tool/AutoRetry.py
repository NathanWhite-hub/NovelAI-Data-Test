import time
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)

    novel_login = []
    aiOutput = ''
    storyName = 'text='

    # Open the text file holding the email and password. Then read the lines and store them in the novel_login list to call later.
    with open('config_info.txt', 'r', encoding='utf-8') as cd:
        novel_config = cd.readlines()

    context = browser.new_context()

    # Some ascii art. Let me have my fun.
    print(' __    __                               __   ______   ______         ______               __                _______               __                         ')
    print('/  \  /  |                             /  | /      \ /      |       /      \             /  |              /       \             /  |                        ')
    print('$$  \ $$ |  ______   __     __ ______  $$ |/$$$$$$  |$$$$$$/       /$$$$$$  | __    __  _$$ |_     ______  $$$$$$$  |  ______   _$$ |_     ______   __    __ ')
    print('$$$  \$$ | /      \ /  \   /  /      \ $$ |$$ |__$$ |  $$ |        $$ |__$$ |/  |  /  |/ $$   |   /      \ $$ |__$$ | /      \ / $$   |   /      \ /  |  /  |')
    print('$$$$  $$ |/$$$$$$  |$$  \ /$$/$$$$$$  |$$ |$$    $$ |  $$ |        $$    $$ |$$ |  $$ |$$$$$$/   /$$$$$$  |$$    $$< /$$$$$$  |$$$$$$/   /$$$$$$  |$$ |  $$ |')
    print('$$ $$ $$ |$$ |  $$ | $$  /$$/$$    $$ |$$ |$$$$$$$$ |  $$ |        $$$$$$$$ |$$ |  $$ |  $$ | __ $$ |  $$ |$$$$$$$  |$$    $$ |  $$ | __ $$ |  $$/ $$ |  $$ |')
    print('$$ |$$$$ |$$ \__$$ |  $$ $$/ $$$$$$$$/ $$ |$$ |  $$ | _$$ |_       $$ |  $$ |$$ \__$$ |  $$ |/  |$$ \__$$ |$$ |  $$ |$$$$$$$$/   $$ |/  |$$ |      $$ \__$$ |')
    print('$$ | $$$ |$$    $$/    $$$/  $$       |$$ |$$ |  $$ |/ $$   |      $$ |  $$ |$$    $$/   $$  $$/ $$    $$/ $$ |  $$ |$$       |  $$  $$/ $$ |      $$    $$ |')
    print('$$/   $$/  $$$$$$/      $/    $$$$$$$/ $$/ $$/   $$/ $$$$$$/       $$/   $$/  $$$$$$/     $$$$/   $$$$$$/  $$/   $$/  $$$$$$$/    $$$$/  $$/        $$$$$$$ |')
    print('                                                                                                                                                   /  \__$$ |')
    print('                                                                                                                                                   $$    $$/ ')
    print('                                                                                                                                                    $$$$$$/  ')


    # Open new page
    page = context.new_page()
    page.set_default_timeout(200000)

    # Go to https://novelai.net/
    page.goto("https://novelai.net")

    # Click text=Login
    page.click("text=Login")
    
    # Fill input[type="email"] with the first element in novel_login
    page.fill("input[type=\"email\"]", novel_config[0])

    # Fill input[type="password"] with the second element in novel_login
    page.fill("input[type=\"password\"]", novel_config[1])

    # Click text=Submit
    page.click("text=Submit")

    # Wait for user input of story name
    storyName += novel_config[2]
    print(novel_config[2])

    # Navigate to the story specified by the user.
    page.click(storyName)

    print('Beginning passes now on the story', + novel_config[2] +'!')
    # Create a text file called 'ai_output'
    with open('ai_output.txt', 'w', encoding='utf-8') as cd:
        for i in range(99):

            # Click button:has-text("Retry")
            page.click("button:has-text('Retry')")

            # Wait for the ai text to appear.
            page.wait_for_selector('.aiText')

            # Query the .aiText selectors which queries all text output from the AI.
            aiTexts = page.query_selector_all(".aiText")

            for aiText in aiTexts:
                aiOutput += ' ' + aiText.text_content()

            # Write the ai output text content to the text file and specify which pass number it is.
            cd.write('Output ' + str(i+1) + ': ' + aiOutput + '\n\n')
            print('Pass ' + str(i+1) + ' complete!')

            # Click the undo button, which will remove the ai text for the next pass.
            page.click("button:has-text('Undo')")
            aiOutput = ''
            time.sleep(0.1)

        # ---------------------
        context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)