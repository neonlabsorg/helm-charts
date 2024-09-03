# Go Ethereum K8s

This helmchart is based on the [instruction](https://docs.prylabs.network/docs/advanced/proof-of-stake-devnet)
Source docker-compose [repo](https://github.com/Offchainlabs/eth-pos-devnet)

[Prysm x Geth EIP4844 Interop](https://gist.github.com/terencechain/3e43cd7f99d69e311e00b04e712b3d5a#prysm-x-geth-eip4844-interop)

### Usage
1. Clone repo
    ```bash
    git clone this_repo_url    
    ```
2. Customize `values.yaml` (see comments). !!! Current version does not support `replicaCount` > 1.
3. Run helm
    ```bash
    helm install geth-chart . --values values.yaml
    ```
4. Wait about 3 minutes after pod started.
   Check logs
   ```bash
   k -n go-eth logs beacon-chain-0 -f

   time="2024-09-03 09:43:30" level=info msg="1m37s until chain genesis" genesisStateRoot=e0341e3784b5dd6ffce5c79f06b0060ae993a1502453881fee3085e76abe6849 genesisTime="2024-09-03 09:45:08 +0000 UTC" genesisValidators=64 prefix=slotutil
   ```
#### Optional. Unlock mainer and rpc accounts before make transcations
Example of `port-forward` usage. But you`re free to use ingress URL instead
1. Port forward. !!! Use right namespace `go-eth` in my case
    ```bash
    kubectl -n geth-test port-forward svc/geth-svc 8545:8545
    ```
2. Get accounts
    ```bash
    curl --location --request POST 'localhost:8545' --header 'Content-Type: application/json' --data-raw '{
        "jsonrpc": "2.0",
        "id": 3,
        "method": "eth_accounts",
        "params": []
    }'
    ```
3. Unlock it
    ```bash
    curl --location --request POST 'localhost:8545' --header 'Content-Type: application/json' --data-raw '{
        "jsonrpc": "2.0",
        "id": 6,
        "method": "personal_unlockAccount",
        "params": [
            "0x123463a4b065722e99115d6c222f267d9cabb524",
            ""
        ]
    }'
    ```
4. Check transactions by script

    4.1. Install  python and pip [instruction](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)

    4.2. Install web3 lib and run script
    ```bash
    pip install web3
    python3 
    ```
    Result example:
    ```bash
    nonce: 0 # Increase each transaction
    Transaction sent with hash: c5396480885689a45cc69d3d8102c2b5eb7bbff8ce3b013f8cf23e78addd99fa
    ```

### Prefounded accounts
The are 2 predefined accounts
```
Account 1 Private Key: 0x2e0834786285daccd064ca17f1654f67b4aef298acbb82cef9ec422fb4975622
Account 1 Address: 0x123463a4b065722e99115d6c222f267d9cabb524
Account 2 Private Key: 01492bb4030f9726fea707865434894e5270b51facc1bace8d701e5aa83962cf
Account 2 Address: 0x14dc79964da2c08b23698b3d3cc7ca32193d9955
```

If you want to create new accounts `gen_eth_accounts.py`
```bash
pip install web3
python gen_eth_accounts.py
```
and then update `files/genesis.json` accordingly.

If you want to change predefined balances update `files/genesis.json` accordingly and reinstall this chart from scratch (Do not forget to remove PVC)

More examples of usage can be found in the instructions provided at the top.