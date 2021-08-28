# IPFS CID v0 <--> 32 Bytes string
## Now you can include IPFS content or metadata CID addresses into Algorand Standard Asset's `metadatahash` or `url`

This is a gist and example code repository for a solution on how to fit IPFS CID v0 (majority of IPFS addresses) into Algorand Standard Asset's `metadatahash` or `url` fields which are each 32 bytes in capacity. This solution makes it possible to avoid including the IPFS CID into ASA's transactions note field which is the current practice in Algorand's Dev  and user community. This way the IPFS address is originally and immutably part of ASA context and data on chain, directly fetched and accessed by ASA ID.

## How it works:

IPFS CID v0 is constructed like this: <function><size><256 bit hash>
In this solution considering the majority of IPFS and default settings to it being v0 with sha2 function and 256 bit size, therefore these two sections can be omitted by service internal logic agreement (they are known bytes!). The remaining is a 256 bit (32 Bytes) hash string that fits into Algorand's ASA `metadatahash` or `url` fields.  
 
 
## Examples are provided in

- Javascript
- Typescript
- Python

## Convertor functions have been contributed to these Algorand SDKs:

- JS-SDK
- PYTHON-SDK
