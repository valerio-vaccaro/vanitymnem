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
                  VanityMnem - create your vanity mnemonics - 2020-2022 Valerio Vaccaro
                         https://github.com/valerio-vaccaro/vanitymnem
```

Create a valid Bitcoin mnemonic with a vanity address in a specific derivation.

Hey this is a PoC! I take no responsibility if you lose your bitcoins using this
program! Be careful and use testnet!

## Install
You can install using pip.

```
pip install vanitymnem
```

## Usage

Just call the program  `vanitymnem` with

```
vanitymnem -h
usage: vanitymnem [-h] [-v] [-n NETWORK] [-p PATTERN] [-P PASSPHRASE] [-t TWELVE] [-c CHILDREN] [-a ADDRESS]

Create a valid Bitcoin mnemonic with a vanity address in a specific derivation.

options:
  -h, --help            show this help message and exit
  -v, --verbose         Be more verbose. Can be used multiple times.
  -n NETWORK, --network NETWORK
                        main, test (default=test)
  -p PATTERN, --pattern PATTERN
                        Regex for pattern
  -P PASSPHRASE, --passphrase PASSPHRASE
                        Passphrase
  -t TWELVE, --twelve TWELVE
                        Twelve words (if false a twentyfour words mnemonic will be returned)
  -c CHILDREN, --children CHILDREN
                        Check in children derivations from 0 to this value (default=100).
  -a ADDRESS, --address ADDRESS
                        native_segwit, nested_segwit or legacy (default=native_segwit).

MIT License - Copyright (c) 2020 Valerio Vaccaro
```

### Examples

Generate a mnemonic with a derivation with beef (with upper or lower case chars) in a mainnet legacy address (check on first 1000 derivations).

```
vanitymnem -p "^.*[bB][eE][eE][fF]" -n main -c 1000  -a legacy -v

'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020-2022 Valerio Vaccaro
                         https://github.com/valerio-vaccaro/vanitymnem
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  Processed 37 mnemonics in 6 seconds (6 mnemonics per second).
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Tested mnemonics:      37
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Seed:                  4942f7915d0ca896b0794c3e5db05394f13b6f764d8e3462a8a00a50d26504b28a8da5e5b786e20f9d7fd319b819584bf4fd1fd659a0e30823605f124791643d
Mnemonic:              punch useful able actor gun coast arrow owner wear fold same scrub outside crisp cause dice inch bar employ lucky artefact soldier buddy whip
Passphrase:            
Master key:            xprv9s21ZrQH143K3mYSRVTtrmyNDM7bhTwrhv4Kr8T3j2Z25bmLcdzCGUuuiK2iudotFQsCVFotwtH7eAki9qez9uZZ5Rzc3gPB8fZm6m4G1SC
Derivation:            m/44'/0'/0'/0/66
Legacy address:        16HTutTekFFo3UJbuaBeEFcZ6cWokefLss
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```

Generate a 12 words mnemonic with a derivation compatible with regex `^.*[vV][aA][lL][eE]` in mainnet address (check on first 100 derivations hardened) with passphrase test

```
vanitymnem -t true -P test -n main -v

'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020-2022 Valerio Vaccaro
                         https://github.com/valerio-vaccaro/vanitymnem
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  Processed 101 mnemonics in 2 seconds (50 mnemonics per second).
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Tested mnemonics:      101
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Seed:                  e1493a1c19f4ec4a0b2f9647b66697a880b44b1c0b209f7bdff02c99e6093908d1dc7faded67ff1d115abfc27e769aa6e4e549481bc0733900cce2af3edcc8c8
Mnemonic:              hammer throw trick invest circle walk that drink practice admit legal switch
Passphrase:            test
Master key:            xprv9s21ZrQH143K2urfneTLs7YSCpg8NkNNuqjCwMKU3g87ggpE6dxLmDNHnjXey4bQKoqZTL2q4Ttu8afUzyXUS8XziUSndNdwKx85ZnZzQXv
Derivation:            m/84'/0'/0'/0/35
Native segwit address: bc1qk5srrutmvaletm2l0wt9309d6r3tcuqzgy60st
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```

If you run this example your mnemonics will be different.

## Check

You can check generate address using [iancoleman bip39 tool](https://iancoleman.io/bip39/).
