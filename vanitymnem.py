# '##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
#  ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
#  ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
#  ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
# . ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
# :. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
# ::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
# :::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
#                 VanityMnem - create your vanity mnemonics - 2020 Valerio Vaccaro
#                          https://github.com/valerio-vaccaro/vanitymnem

import argparse
import os
import wallycore as wally
import re
import time

banner = """
'##::::'##::::'###::::'##::: ##:'####:'########:'##:::'##:'##::::'##:'##::: ##:'########:'##::::'##:
 ##:::: ##:::'## ##::: ###:: ##:. ##::... ##..::. ##:'##:: ###::'###: ###:: ##: ##.....:: ###::'###:
 ##:::: ##::'##:. ##:: ####: ##:: ##::::: ##:::::. ####::: ####'####: ####: ##: ##::::::: ####'####:
 ##:::: ##:'##:::. ##: ## ## ##:: ##::::: ##::::::. ##:::: ## ### ##: ## ## ##: ######::: ## ### ##:
. ##:: ##:: #########: ##. ####:: ##::::: ##::::::: ##:::: ##. #: ##: ##. ####: ##...:::: ##. #: ##:
:. ## ##::: ##.... ##: ##:. ###:: ##::::: ##::::::: ##:::: ##:.:: ##: ##:. ###: ##::::::: ##:.:: ##:
::. ###:::: ##:::: ##: ##::. ##:'####:::: ##::::::: ##:::: ##:::: ##: ##::. ##: ########: ##:::: ##:
:::...:::::..:::::..::..::::..::....:::::..::::::::..:::::..:::::..::..::::..::........::..:::::..::
                  VanityMnem - create your vanity mnemonics - 2020 Valerio Vaccaro
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

parser = argparse.ArgumentParser(description='Create a valid Bitcoin mnemonic with a vanity address in a specific derivation.', epilog='MIT License - Copyright (c) 2020 Valerio Vaccaro')
parser.add_argument('-v', '--verbose', action='count', default=0, help='Be more verbose. Can be used multiple times.')
parser.add_argument('-n', '--network', help=' main, test (default=test)', default='test')
parser.add_argument('-p', '--pattern', help='Regex for pattern', default='^.*[vV][aA][lL][eE]')
parser.add_argument('-d', '--derivation', help="Base derivation (default=m/44'/0'/0')", default="m/44'/0'/0'")
parser.add_argument('-c', '--children', help='Check in children derivations from 0 to this value (default=100).', type=int, default=100)
feature_parser = parser.add_mutually_exclusive_group(required=True)
feature_parser.add_argument('--hardened', help='Add for have hardened child.', dest='hardened', action='store_true')
feature_parser.add_argument('--no-hardened', help='Add for have not hardened child.', dest='hardened', action='store_false')
parser.set_defaults(feature=True)

parser.add_argument('-a', '--address', help='native_segwit, nested_segwit or legacy (default=native_segwit).', default='native_segwit')

args = parser.parse_args()
print(banner)

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
    print('Wrong network type, choose between main or test.')
    exit(1)

# check address
if args.address not in ['native_segwit', 'nested_segwit', 'legacy']:
    print('Wrong address type, choose between native_segwit or nested_segwit or legacy.')
    exit(1)

# convert derivation
if args.derivation != "m/44'/0'/0'":
    print("Actually we use only m/44'/0'/0' derivation.")
    exit(1)

hardened_notation = ''
if args.hardened == True:
    hardened_notation = '\''

path = [0x80000000 + 44] + [0x80000000 + 0] + [0x80000000 + 0]

pattern = re.compile(args.pattern)
i = 0
start = time.time()

while(True):
    i = i + 1

    # get entropy
    entropy = os.urandom(32)

    # calculate mnemonic
    mnemonic = wally.bip39_mnemonic_from_bytes(None, entropy)

    # calculate the seed
    seed = bytearray(64)
    password = ''
    wally.bip39_mnemonic_to_seed(mnemonic, password, seed)

    # calculate master key
    master_key = wally.bip32_key_from_seed(seed, master_key_flags, wally.BIP32_FLAG_SKIP_HASH)
    if args.verbose > 1:
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print('Seed:                  {}'.format(seed.hex()))
        print('Mnemonic:              {}'.format(mnemonic))
        print('Master key:            {}'.format(wally.bip32_key_to_base58(master_key, 0)))
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

    # derive a children
    found = False
    for x in range(0, args.children + 1):
        child = x
        if args.hardened == True:
            child = child + 0x80000000
        derived = wally.bip32_key_from_parent_path(master_key, path + [child],  wally.BIP32_FLAG_KEY_PRIVATE);

        if args.verbose > 1:
            print('Derivation:            m/44\'/0\'/0\'/{}{}'.format(x, hardened_notation))

        if args.address == 'native_segwit':
            # calculate native segwit address
            native_segwit = wally.bip32_key_to_addr_segwit(derived, native_segwit_address_flags, 0);
            if args.verbose > 1:
                print('Native segwit address: {}'.format(native_segwit))
            if pattern.match(native_segwit):
                found = True
        if args.address == 'nested_segwit':
            # calculate nested segwit address - base_58
            nested_segwit = wally.bip32_key_to_address(derived, wally.WALLY_ADDRESS_TYPE_P2SH_P2WPKH, nested_segwit_address_flags);
            if args.verbose > 1:
                print('Nested segwit addres:  {}'.format(nested_segwit))
            if pattern.match(nested_segwit):
                found = True

        if args.address == 'legacy':
            # calculate legacy address - base_58
            legacy_address = wally.bip32_key_to_address(derived, wally.WALLY_ADDRESS_TYPE_P2PKH, legacy_address_flags);
            if args.verbose > 1:
                print('Legacy address:        {}'.format(legacy_address))
            if pattern.match(legacy_address):
                found = True

        if args.verbose > 1:
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

        if found:
            break

    if found:
        break

    if i%1000 == 0:
        if args.verbose > 0:
            end = time.time()
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
            print('  Processed {} mnemonics in {} seconds ({} mnemonics per second).'.format(i, round(end-start), round(i/(end-start))))

end = time.time()
if args.verbose > 0:
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('  Processed {} mnemonics in {} seconds ({} mnemonics per second).'.format(i, round(end-start), round(i/(end-start))))
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('Tested mnemonics:      {}'.format(i))

print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('Seed:                  {}'.format(seed.hex()))
print('Mnemonic:              {}'.format(mnemonic))
print('Master key:            {}'.format(wally.bip32_key_to_base58(master_key, 0)))
print('Derivation:            m/44\'/0\'/0\'/{}{}'.format(x, hardened_notation))
if args.address == 'native_segwit':
    print('Native segwit address: {}'.format(native_segwit))
if args.address == 'nested_segwit':
    print('Nested segwit addres:  {}'.format(nested_segwit))
if args.address == 'legacy':
    print('Legacy address:        {}'.format(legacy_address))
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
