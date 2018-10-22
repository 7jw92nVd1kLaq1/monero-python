from .exceptions import TransactionNotSigned
from .transaction import SignedTransaction

class Daemon(object):
    """Monero daemon.

    Provides interface do a daemon instance.

    :param backend: a daemon backend
    """
    def __init__(self, backend):
        self._backend = backend

    def info(self):
        """
        Returns basic information about the daemon.

        :rtype: dict
        """
        return self._backend.info()

    def height(self):
        """
        Return daemon's chain height.

        :rtype: int
        """
        return self._backend.info()['height']

    def send_transaction(self, tx, relay=True):
        """
        Sends a transaction generated by a :class:`Wallet <monero.wallet.Wallet>`.

        :param tx: :class:`SignedTransaction <monero.transaction.SignedTransaction>`
        :param relay: whether to relay the transaction to peers. If `False`, the daemon will have
                to mine the transaction itself in order to have it included in the blockchain.
        """
        if not isinstance(tx, SignedTransaction):
            raise TransactionNotSigned(tx.hash)
        return self._backend.send_transaction(tx.blob, relay=relay)

    def mempool(self):
        """
        Returns current mempool contents.

        :rtype: list of :class:`Transaction <monero.transaction.Transaction>`
        """
        return self._backend.mempool()
