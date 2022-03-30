from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 2000
LOCAL_BLOCKCHAINS = ["development", "ganache-local"]
FORKED_BLOCKCHAINS = ["mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAINS
        or network.show_active() in FORKED_BLOCKCHAINS
    ):
        return accounts[0]
    else:
        account = accounts.add(config["wallets"]["from_key"])

    return account


def deploy_mock():
    account = get_account()
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": account}
        )
    print("Mocks Deployed")
