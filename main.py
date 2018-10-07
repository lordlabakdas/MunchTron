from __future__ import print_function
import time
from slackclient import SlackClient
from configparser import ConfigParser
from brain.brain import brain
import os

if not os.path.exists("config.ini"):
    parser = ConfigParser()
    parser.add_section("settings")
    parser.set("settings", "location", "")
    parser.add_section("slack")
    parser.set("slack", "userID", "")
    parser.set("slack", "key", "")
    print("Please set configurations in config.ini")
    parser.write("settings.ini")
    exit()


cf = ConfigParser()
cf.read("config.ini")

# starterbot's ID as an environment variable
BOT_ID = cf.get("slack", "userID")
SLACK_BOT_TOKEN = cf.get("slack", "key")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(SLACK_BOT_TOKEN)


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = (
        "Not sure what you mean. Use the *"
        + EXAMPLE_COMMAND
        + "* command with numbers, delimited by spaces."
    )
    if command.startswith(EXAMPLE_COMMAND):
        # response = "Sure...write some more code then I can do that!"
        br = brain()
        print(command)
        response = br.parse_sentence(command)
    slack_client.api_call(
        "chat.postMessage", channel=channel, text=response, as_user=True
    )


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and "text" in output and AT_BOT in output["text"]:
                # return text after the @ mention, whitespace removed
                return (
                    output["text"].split(AT_BOT)[1].strip().lower(),
                    output["channel"],
                )
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:

            command, channel = parse_slack_output(slack_client.rtm_read())
            # print command, channel
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
