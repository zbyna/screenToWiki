"""
    upload_file_directly.py

    MediaWiki API Demos
    Demo of `Upload` module: Sending post request to upload a file directly

    MIT license

    upraveno by Zbyna
"""

import requests
import click
import logging


logging.basicConfig(filename='mujLOG.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


@click.command()
@click.argument('pathtofile', type=click.Path(exists=True))
@click.option('-s', '--site-name', 'jmeno_site', prompt='Site name?')
@click.option('-b', '--bot-name', 'jmeno_bota', prompt='Bot name?')
@click.option('-p', '--password', 'heslo_pro_bota', prompt=True, hide_input=True,
              confirmation_prompt=True)
def screenToWiki(jmeno_site, jmeno_bota, heslo_pro_bota, pathtofile):
    """
    \b
     upload a file(picture) to MediaWiki site
     it is needed:
     1. site name e.g. http://192.168.1.13/wiki/api.php
     2. token for bot login -LOGIN_TOKEN
     3. login as a bot -  name, password
     4. token for upload  - CSRF_TOKEN
     5. upload image
    """
    S = requests.Session()
    # "http://192.168.1.13/wiki/api.php"
    URL = jmeno_site
    FILE_PATH = pathtofile
    FILE_NAME = click.format_filename(pathtofile, shorten=True)

    click.echo(f'File name: {FILE_NAME}')
    logging.debug(f'File name: {FILE_NAME}')
    click.echo(f'Site name: {URL}')
    logging.debug(f'Site name: {URL}')
    click.echo(f'Path: {click.format_filename(pathtofile,shorten = False)}')
    logging.debug(f'Path: {click.format_filename(pathtofile,shorten = False)}')
    # Step 1: Retrieve a login token
    PARAMS_1 = {
        "action": "query",
        "meta": "tokens",
        "type": "login",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS_1)
    DATA = R.json()
    print(f'Response - 1: {R.content}')
    logging.debug(f'Response - 1: {R.content}')

    LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

    # Step 2: Send a post request to login. Use of main account for login is not
    # supported. Obtain credentials via Special:BotPasswords
    # (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
    PARAMS_2 = {
        "action": "login",
        "lgname": jmeno_bota,
        "lgpassword": heslo_pro_bota,
        "format": "json",
        "lgtoken": LOGIN_TOKEN
    }
    print(f'Request 2: {PARAMS_2}')
    logging.debug(f'Request 2: {PARAMS_2}')
    R = S.post(URL, data=PARAMS_2)
    print(f'Response - 2: {R.content}')
    logging.debug(f'Response - 2: {R.content}')

    # Step 3: Obtain a CSRF token
    PARAMS_3 = {
        "action": "query",
        "meta": "tokens",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS_3)
    DATA = R.json()
    print(f'Response - 3: {R.content}')
    logging.debug(f'Response - 3: {R.content}')

    CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

    # Step 4: Post request to upload a file directly
    PARAMS_4 = {
        "action": "upload",
        "filename": FILE_NAME,
        "format": "json",
        "token": CSRF_TOKEN,
        "ignorewarnings": 1
    }

    FILE = {'file': (FILE_NAME, open(FILE_PATH, 'rb'), 'multipart/form-data')}

    R = S.post(URL, files=FILE, data=PARAMS_4)
    DATA = R.json()
    print(f'Response - 4: {R.content}')
    logging.debug(f'Response - 4: {R.content}')
    S.close()
    print('Session closed')
    logging.info('Session closed')


if __name__ == '__main__':
    screenToWiki()
