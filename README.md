# Vanitymnem
```
'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020 Valerio Vaccaro
                           https://github.com/valerio-vaccaro/vanitymnem
```

Create a valid Bitcoin mnemonic with a vanity address in a specific derivation.

Hey this is a PoC! I take no responsibility if you lose your bitcoins using this
program! Be careful and use testnet!

## Install
You will need python3 and virtualenv plus **only one** external library
(libwally).

Create a virtual environment and load it.

```
virtualenv -p python3 venv3
. venv3/bin/activate
```

Install dependencies.

```
pip install -r requirements.txt
```

You are ready!

## Usage

Just call the script `vanitymnem.py` with

```
usage: vanitymnem.py [-h] [-v] [-n NETWORK] [-p PATTERN] [-d DERIVATION]
                     [-c CHILDREN] (--hardened | --no-hardened) [-a ADDRESS]

Create a valid Bitcoin mnemonic with a vanity address in a specific
derivation.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Be more verbose. Can be used multiple times.
  -n NETWORK, --network NETWORK
                        main, test (default=test)
  -p PATTERN, --pattern PATTERN
                        Regex for pattern
  -d DERIVATION, --derivation DERIVATION
                        Base derivation (default=m/44'/0'/0')
  -c CHILDREN, --children CHILDREN
                        Check in children derivations from 0 to this value
                        (default=100).
  --hardened            Add for have hardened child.
  --no-hardened         Add for have not hardened child.
  -a ADDRESS, --address ADDRESS
                        native_segwit, nested_segwit or legacy
                        (default=native_segwit).
```

### Examples

Generate a mnemonic with a derivation with beef (with upper or lower case chars)
in a mainnet legacy address (check on first 1000 derivations hardened).

```
python vanitymnem.py -p "^.*[bB][eE][eE][fF]" -n main -c 1000  --hardened -a legacy -v

'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020 Valerio Vaccaro
                           https://github.com/valerio-vaccaro/vanitymnem
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  Processed 12 mnemonics in 2 seconds (6 mnemonics per second).
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Tested mnemonics:      12
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Seed:                  7bcce0a77871e3a4a77ad5b264ab95311d40de669b1b7547318ad78b88e5d5446638accf0ddf39e513d63dc4da64c0f434106767c65b3ab55170024e287f8fd1
Mnemonic:              bronze hint primary cause gesture basic feel glove regular layer unveil acid magnet glance disease sell wood excite crash lawsuit rebuild awesome stock price
Master key:            xprv9s21ZrQH143K4bQ5Uy3zPXVqm7wzrHLCCPZawCx498NW9wU9EaZsoZuZbHyxWBdqNUovrZz69cfiV2r9BbYyE2JpNYK4k8TMPBU1pF6c7sa
Derivation:            m/44'/0'/0'/790'
Legacy address:        1JeKLTEJD32ufTZ7ypZsEcPfBeEFppYShu
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```

The same in testnet but not hardened.

```
vanitymnem % python vanitymnem.py -p "^.*[bB][eE][eE][fF]" -n test -c 1000  --no-hardened -a legacy -v

'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020 Valerio Vaccaro
                           https://github.com/valerio-vaccaro/vanitymnem
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  Processed 16 mnemonics in 3 seconds (6 mnemonics per second).
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Tested mnemonics:      16
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Seed:                  57422164b2f36dbcffce4038875c91b3e46184ee979716613152f8208fd612b4f0eed07249c9289f740e55c246a7b01c9c563315dcd2181f0f07064f6d3eba9d
Mnemonic:              culture check elder resemble pony minimum woman people volume february youth weather credit yellow farm coyote virus cream biology category online vivid bus dawn
Master key:            tprv8ZgxMBicQKsPdV57khs5criFS2bHqVs1SwkvjXzBHWLH6NDSBuZ74uCQrfUPj7QtcXSw2amPm4a7fQcdPp8ZAYUsNLVWHp1ZJfDSvh97hky
Derivation:            m/44'/0'/0'/253
Legacy address:        mwFQ7VtuKDBrcLqpaoW2xu2BEefQNtuWAt
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```

Generate a mnemonic with a derivation compatible with regex `^.*[vV][aA][lL][eE]`
in a mainnet legacy address (check on first 100 derivations hardened).

```
python vanitymnem.py -d "m/0'/0'/0'" -v -n main --hardened -a legacy

'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020 Valerio Vaccaro
                           https://github.com/valerio-vaccaro/vanitymnem

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  Processed 315 mnemonics in 7 seconds (45 mnemonics per second).
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Tested mnemonics:      315
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Seed:                  d439433f959aecaad201c18d875b978303279f5aa5b0e910a9e7825326166a013535bd99db212efbae34fbb163ae1a9a2733b1e6c836dd5d6a76aabc76d
5e8d9
Mnemonic:              ticket snow winner twin flip where mutual wolf great mother wild useless upset crime toilet consider rose medal notice divi
de census canoe better include
Master key:            xprv9s21ZrQH143K2mYECXTUUGtJfpXMbXWwf44xRAXwo6XXVcBJpaZqCZhZG9kxkuAQrSnRMwufhY2AkyGG6ihqHtbqZtvh5jh7g99GBTp1C7s
Derivation:            m/0'/0'/0'/96'
Legacy address:        19vbqAd4fwao3RqFvALEdS4nTgfW4ZXiuG
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```

If you run this example your mnemonics will be different.

## Check

You can check generate address using [iancoleman bip39 tool](https://iancoleman.io/bip39/).
