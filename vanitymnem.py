# '##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
#  ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
#  ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
#  ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
# . ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
# :. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
# ::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
# :::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
#                 VanityMnem - create your vanity mnemonics - 2020-2022 Valerio Vaccaro
#                            https://github.com/valerio-vaccaro/vanitymnem

import argparse
import os
import wallycore as wally
import re
import time

from colorama import init
from termcolor import colored

banner = """
'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020-2022 Valerio Vaccaro
                         https://github.com/valerio-vaccaro/vanitymnem"""

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main():
    init()
    parser = argparse.ArgumentParser(description='Create a valid Bitcoin mnemonic with a vanity address in a specific derivation.', epilog='MIT License - Copyright (c) 2020 Valerio Vaccaro')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Be more verbose. Can be used multiple times.')
    parser.add_argument('-n', '--network', help=' main, test (default=test)', default='test')
    parser.add_argument('-p', '--pattern', help='Regex for pattern', default='^.*[vV][aA][lL][eE]')
    parser.add_argument('-P', '--passphrase', help='Passphrase', default='')
    parser.add_argument('-t', '--twelve', help='Twelve words (if false a twentyfour words mnemonic will be returned)', type=bool, default=False)
    parser.add_argument('-c', '--children', help='Check in children derivations from 0 to this value (default=100).', type=int, default=100)
    parser.add_argument('-a', '--address', help='native_segwit, nested_segwit or legacy (default=native_segwit).', default='native_segwit')
    args = parser.parse_args()
    print(colored(banner, 'green'))

    # check net
    if args.network == 'main':
        master_key_flags = wally.BIP32_VER_MAIN_PRIVATE
        native_segwit_address_flags = 'bc'
        nested_segwit_address_flags = wally.WALLY_ADDRESS_VERSION_P2SH_MAINNET
        legacy_address_flags = wally.WALLY_ADDRESS_VERSION_P2PKH_MAINNET
    elif args.network == 'test':
        master_key_flags = wally.BIP32_VER_TEST_PRIVATE
        native_segwit_address_flags = 'bc'
        nested_segwit_address_flags = wally.WALLY_ADDRESS_VERSION_P2SH_TESTNET
        legacy_address_flags = wally.WALLY_ADDRESS_VERSION_P2PKH_TESTNET
    else:
        print(colored('Wrong network type, choose between main or test.', 'red'))
        exit(1)

    # check address
    if args.address == 'native_segwit':
        derivation = "m/84'/0'/0'"
    elif args.address == 'nested_segwit':
        derivation = "m/49'/0'/0'"
    elif args.address == 'legacy':
        derivation = "m/44'/0'/0'"
    else:
        print(colored('Wrong address type, choose between native_segwit or nested_segwit or legacy.', 'red'))
        exit(1)
    
    # check external addresses, not change ones
    derivation = derivation + '/0'

    path = []
    for c in derivation.split('/'):
        der = c.split("'")
        if (der[0] == 'm'):
            continue
        if len(der) == 2:
            path = path + [0x80000000 + int(der[0])]
        else:
            path = path + [int(der[0])]

    pattern = re.compile(args.pattern)
    i = 0
    start = time.time()

    while(True):
        i = i + 1

        # get entropy
        if args.twelve:
            entropy = os.urandom(16)
        else:
            entropy = os.urandom(32)

        # calculate mnemonic
        mnemonic = wally.bip39_mnemonic_from_bytes(None, entropy)

        # calculate the seed
        seed = bytearray(64)
        wally.bip39_mnemonic_to_seed(mnemonic, args.passphrase, seed)

        # calculate master key
        master_key = wally.bip32_key_from_seed(seed, master_key_flags, wally.BIP32_FLAG_SKIP_HASH)
        if args.verbose > 1:
            print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
            print(colored('Seed:                  {}'.format(seed.hex()), 'red'))
            print(colored('Mnemonic:              {}'.format(mnemonic), 'red'))
            print(colored('Passphrase:            {}'.format(args.passphrase), 'red'))
            print(colored('Master key:            {}'.format(wally.bip32_key_to_base58(master_key, 0)), 'yellow'))
            print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))

        # derive a children
        found = False
        for x in range(0, args.children + 1):
            child = x
            derived = wally.bip32_key_from_parent_path(master_key, path + [child],  wally.BIP32_FLAG_KEY_PRIVATE);

            if args.verbose > 1:
                print(colored('Derivation:            {}/{}'.format(derivation, x), 'yellow'))

            if args.address == 'native_segwit':
                # calculate native segwit address
                native_segwit = wally.bip32_key_to_addr_segwit(derived, native_segwit_address_flags, 0);
                if args.verbose > 1:
                    print(colored('Native segwit address: {}'.format(native_segwit), 'yellow'))
                if pattern.match(native_segwit):
                    found = True
            if args.address == 'nested_segwit':
                # calculate nested segwit address - base_58
                nested_segwit = wally.bip32_key_to_address(derived, wally.WALLY_ADDRESS_TYPE_P2SH_P2WPKH, nested_segwit_address_flags);
                if args.verbose > 1:
                    print(colored('Nested segwit addres:  {}'.format(nested_segwit), 'yellow'))
                if pattern.match(nested_segwit):
                    found = True

            if args.address == 'legacy':
                # calculate legacy address - base_58
                legacy_address = wally.bip32_key_to_address(derived, wally.WALLY_ADDRESS_TYPE_P2PKH, legacy_address_flags);
                if args.verbose > 1:
                    print(colored('Legacy address:        {}'.format(legacy_address), 'yellow'))
                if pattern.match(legacy_address):
                    found = True

            if args.verbose > 1:
                print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))

            if found:
                break

        if found:
            break

        if i%1000 == 0:
            if args.verbose > 0:
                end = time.time()
                print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
                print('  Processed {} mnemonics in {} seconds ({} mnemonics per second).'.format(i, round(end-start), round(i/(end-start))))

    end = time.time()
    if args.verbose > 0:
        print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
        print(colored('  Processed {} mnemonics in {} seconds ({} mnemonics per second).'.format(i, round(end-start), round(i/(end-start))), 'yellow'))
        print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
        print(colored('Tested mnemonics:      {}'.format(i), 'yellow'))

    print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))
    print(colored('Seed:                  {}'.format(seed.hex()), 'red'))
    print(colored('Mnemonic:              {}'.format(mnemonic), 'red'))
    print(colored('Passphrase:            {}'.format(args.passphrase), 'red'))
    print(colored('Master key:            {}'.format(wally.bip32_key_to_base58(master_key, 0)), 'yellow'))
    print(colored('Derivation:            {}/{}'.format(derivation, x), 'yellow'))
    if args.address == 'native_segwit':
        print(colored('Native segwit address: {}'.format(native_segwit), 'yellow'))
    if args.address == 'nested_segwit':
        print(colored('Nested segwit addres:  {}'.format(nested_segwit), 'yellow'))
    if args.address == 'legacy':
        print(colored('Legacy address:        {}'.format(legacy_address), 'yellow'))
    print(colored('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'yellow'))

if __name__== "__main__" :
    main()