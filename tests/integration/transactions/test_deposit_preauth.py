from unittest import TestCase

from tests.integration.it_utils import submit_transaction
from tests.integration.transactions.reusable_values import FEE, WALLET
from xrpl.models.response import ResponseStatus
from xrpl.models.transactions import DepositPreauth
from xrpl.network_clients import JsonRpcClient

JSON_RPC_URL = "http://test.xrp.xpring.io:51234"
JSON_RPC_CLIENT = JsonRpcClient(JSON_RPC_URL)

ACCOUNT = WALLET.classic_address
ADDRESS = "rEhxGqkqPPSxQ3P25J66ft5TwpzV14k2de"


class TestDepositPreauth(TestCase):
    def test_authorize(self):
        deposit_preauth = DepositPreauth(
            account=ACCOUNT,
            fee=FEE,
            sequence=WALLET.next_sequence_num,
            authorize=ADDRESS,
        )
        response = submit_transaction(deposit_preauth, WALLET)
        self.assertEqual(response.status, ResponseStatus.SUCCESS)

    def test_unauthorize(self):
        deposit_preauth = DepositPreauth(
            account=ACCOUNT,
            fee=FEE,
            sequence=WALLET.next_sequence_num,
            unauthorize=ADDRESS,
        )
        response = submit_transaction(deposit_preauth, WALLET)
        self.assertEqual(response.status, ResponseStatus.SUCCESS)