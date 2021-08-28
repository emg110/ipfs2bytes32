# ipfs2bytes32

This is a gist and example code repository for a solution on how to fit IPFS CID v0 (majority of IPFS addresses) into Algorand Standard Asset's metadatahash or url fields which are each 32 bytes in capacity. This solution makes it possible to aviod including the IPFS CID into ASA's transactions note field which is the current practice in Algorand's Dev  and user community. This way the IPFS address is originally and immutabely part of ASA context and data on chain, directly fetched and accessed by ASA ID. 
