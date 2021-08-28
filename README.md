# IPFS CID v0 <--> 32 Bytes string
## Now you can include IPFS content or metadata CID addresses into Algorand Standard Asset's `metadatahash`

### IMPORTANT: on Release 2.7.1 Algorand increased the URL field capacity to 96 Bytes so it does not need this solution, but still URL and CDI in respect to ASA context can have various usecases and some Devs like me may still prefer metadatahash field (for IPFS CDI storage) which includes exactly the ASA metadata and is an standard 32 Byte (256 bit) hash! Unoccupied URL then can still be used for ASA corresponding longer service endpoint URLs. 

This is a gist and example code repository for a solution on how to fit IPFS CID v0 (majority of IPFS addresses) into Algorand Standard Asset's `metadatahash` field which is 32 bytes. This solution makes it possible to avoid including the IPFS CID into ASA's transactions note field which is the current practice in Algorand's Dev  and user community. This way the IPFS address is originally and immutably part of ASA context and data on chain, directly fetched and accessed by ASA ID.

## How it works:

IPFS CID v0 is constructed like this: <function><size><256 bit hash>
In this solution considering the majority of IPFS and default settings to it being v0 with sha2 function and 256 bit size, therefore these two sections can be omitted by service internal logic agreement (they are known bytes!). The remaining is a 256 bit (32 Bytes) hash string that fits into Algorand's ASA `metadatahash` field.  

## [SEE HOW IT WORKS ONLINE](https://emg110.github.io/ipfs2bytes32/)
 
## Examples are provided in

- Javascript
- Typescript
- Python

## Convertor functions have been contributed to these Algorand SDKs:

- [JS-SDK](https://github.com/algorand/js-algorand-sdk/pull/427)
- [PYTHON-SDK](https://github.com/algorand/py-algorand-sdk/pull/229)
