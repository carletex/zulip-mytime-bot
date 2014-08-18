# mytime-bot

Zulip bot for Hackerschool.

## Usage

1. Clone this repository
2. Donwload and install the Python bindings from [Zulip](https://zulip.com/api/)
3. Create a Zulip bot on https://zulip.com/#settings
4. Create an OAuth application on you Hackerschool settings
   1. Use `urn:ietf:wg:oauth:2.0:oob` as your app redirect URI
5. Create a `keys.sh` file and put the following values:
   ```bash
   export HS_CONSUMER_KEY='<your_hackerschool_app_consumer_key>'
   export HS_CONSUMER_SECRET='<your_hackerschool_app_consumer_secret>'
   export ZULIP_BOT_EMAIL='<your_zulip_bot_email>'
   export ZULIP_API_KEY='<your_zulip_api_key>'
   ```
6. Put those variables in your environment with `$ source keys.sh`
7. Run `$ python mytime_bot` and enter your HackerSchool user and password to get the auth and access token
8. Send `mytime` in a private message to your Zulip bot and you should receive your time left in HackerSchool

## ToDo

Currently, the bot only gets the info of the authenticated user. Waiting for the `get /person/:email` HS API implementation
