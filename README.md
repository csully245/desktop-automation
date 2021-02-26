# Desktop Automation
Lightweight code to handle desktop tasks I don't want to do by hand

## maintenance-bot
Maintenance Bot is my solution to regular computer maintenance I don't have the patience or desire to complete.
At the moment, his only task is to point out files in my downloads folder that haven't been touched in 90 days or more
and prompt me with actions to deal with them.

### Setup
https://datatofish.com/python-script-windows-scheduler/

## toggle-privacy
Toggle Privacy opens the privacy settings for the camera or microphone and toggles them. Pretty simple.

## OHQ
For automatically joining the UMich EECS Office Hours queue.
1. Download independently.
2. Install pyautogui: ```$pip install pyautogui```
3. Open the office hours queue prior to it becoming available. Move it to somewhere on your screen where it can sit without things popping up over it. All you need exposed is the form with "Location," "Description," and "Request Help."
4. Run OHQ.py: ```$python run OHQ.py```
5. Enter the text you want to use for your office hours request into the box as prompted.
6. Hover over each desired field as prompted and press Enter when ready. Make sure you don't click or tab off of the OHQ window or the Enter key won't work.
7. Wait for the office hours queue to open. As long as you don't move anything over top of the form, you can continue to use your computer as you wait. It will check availability every half second and sign in for you once it's available.
8. If the Python terminal closes early/the code stops running before you've joined the queue, something went wrong. Sorry. Note that the OHQ window will close after each prompt is completed, but the core script should still be running in the terminal until you're signed in.

## Usage Rule
Don't tell anyone about this. I'd like to keep it within myself and my project partners so we don't have to worry about others beating us to the queue.
