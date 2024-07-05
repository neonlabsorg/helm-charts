# Go Ethereum K8s

This helmchart is based on the [instruction](https://medium.com/scb-digital/running-a-private-ethereum-blockchain-using-docker-589c8e6a4fe8)

### Usage
1. Clone repo
    ```bash
    git clone this_repo_url
    ```
2. Generate `NODE_KEY_HEX` and `ENODE`
    ```bash
    python -m venv env && source env/bin/activate && pip install eth-keys eth-utils && python get_node_enode_keys.py && deactivate && rm -rf env
    ```
3. Customize `values.yaml` (see comments). !!! Current version does not support `replicaCount` > 1.
4. Run helm
    ```bash
    helm install geth-chart . --values values.yaml
    ```
5. Copy mainer key from mainer pod to rpc pod. !!! Use right namespace `go-eth` in my case
    ```bash
    mkdir -p mainerKey && kubectl -n go-eth cp geth-miner-0:/root/.ethereum/keystore/. mainerKey/ && kubectl -n go-eth cp mainerKey/. geth-rpc-endpoint-0:/root/.ethereum/keystore/ && rm -rf mainerKey
    ```
#### Optional. Unlock mainer and rpc accounts before make transcations
Example of `port-forwar` usage. But you`re free to use ingress URL instead
1. Port forward. !!! Use right namespace `go-eth` in my case
    ```bash
    kubectl -n go-eth port-forward svc/geth-rpc-endpoint 8545:8545
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
3. Unlock them(both)
    ```bash
    curl --location --request POST 'localhost:8545' --header 'Content-Type: application/json' --data-raw '{
        "jsonrpc": "2.0",
        "id": 6,
        "method": "personal_unlockAccount",
        "params": [
            "Account",
            "ACCOUNT_PASSWORD"
        ]
    }'
    ```

More examples of usage can be found in the instructions provided at the top.