import time
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    file_pass_num = 0
    novel_email = 'john.doe69@aol.com'
    novel_pass = 'PASSWORD'

    # Number of times the script loops (5 times here). 
    # Change 5 to a different number decrease or increase number of times
    for i in range(5):
        context = browser.new_context()
        
        # Counts the amount of responses generated to undo at the end.
        ai_responses = 0
        file_pass_num += 1

        # Open new page
        page = context.new_page()
        page.set_default_timeout(200000)

        # Go to https://novelai.net/
        page.goto("https://novelai.net")

        # Click text=Login
        page.click("text=Login")

        # Fill input[type="email"]
        page.fill("input[type=\"email\"]", novel_email)

        # Fill input[type="password"]
        page.fill("input[type=\"password\"]", novel_pass)

        # Click text=Submit
        page.click("text=Submit")

        # with page.expect_navigation(url="https://novelai.net/#/stories"):
        # Click on the specified story. Change anything after 'text=' if you want to open a new story.
        page.click("text=STORY NAME HERE")

        # Clicks send every three seconds for sixty seconds. This gives the AI time to respond.
        for num in range(21):
            # Click button:has-text("Send")
            page.click("button:has-text('Send')")
            ai_responses += 1
            time.sleep(3)

        # Query all .aiText selectors which queries all text output from the AI.
        aiTexts = page.query_selector_all(".aiText")

        # Create a text file called 'ai_test' which defaults to C:\Users\COMPUTERNAMEHERE
        with open('ai_test_' + str(file_pass_num) + '.txt', 'w', encoding="utf-8") as cd:
            # Writes a line in the text file for each AI response.
            for aiText in aiTexts:
                cd.write(aiText.text_content() + '\n\n')

        # Counts out the number of responses the AI output and clicks the undo button every .5 seconds.
        for num in range(ai_responses):
            page.click("button:has-text('Undo')")
            time.sleep(0.5)

        # ---------------------
        context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)