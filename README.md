# Automatic Investing Tool for Coinbase

Recurring investment is not very profitable when you pay $1.00 fee on a $5.00 order in the Coinbase app. Meanwhile, Coinbase Pro charges a taker fee of 0.35% - that's $0.0175. And that's the highest the fee goes. However, it lacks the ability to buy recurringly. Automatic Investing Tool for Coinbase solves this problem and allows you to invest in cryptocurrencies in a recurring manner and not pay insane fees!

## Installation

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/klimenkoff9/django_investment
$ cd django_investment
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/account/add-key/`.

## Usage

Note: This is a sandbox example, to use your real Coinbase Pro account follow same steps but remove api_url parameter in utils/verify_account.py on line 9

On the `add-key` page, you can add a new key to the database. To do so navigate to `https://public.sandbox.pro.coinbase.com/profile/api-keys` and click the `+ New API Key` button.
Very important! Give permissions to the key to view and trade and give it a nickname.
Then, copy the `passphrase` value and enter it into the `passphrase` field.
Click create key.
Since we're on Sandbox you won't receive a text code so enter any dummy value.
Copy the `API Secret` value and enter it into the `api_value` field.
Click Done.
Copy the `API Key` value above the `Nickname` line and enter it into the `api_key` field.
Give the key a nickname and click Post.

Congrats - you've added a new key to the database!

Next step is to Navigate to `http://127.0.0.1:8000/account/place-order/`.

There choose a currency (example: `BTC-USD` or `ETH-USD`), enter the amount you want to buy and pick the frequency. Then choose your associated key and click Post.

Congratulations - now you recurrently investing into cryptomarket without paying insane fees!   

## Contributing
We're currently working on deploying this app and make it available to users without having to install it. Front end is also in progress.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)