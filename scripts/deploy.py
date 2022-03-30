from brownie import FundMe, accounts, config, network, MockV3Aggregator
from dotenv import load_dotenv
from scripts.helper import LOCAL_BLOCKCHAINS, get_account, deploy_mock


def deploy_fund_me():
    load_dotenv()
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAINS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fund_me


def main():
    deploy_fund_me()
