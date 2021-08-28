import base58
import binascii


def ipfscidv0_to_byte32(cid):
    """
    Convert ipfscidv0 to 32 bytes hex string.

    Args:
        cid (string): IPFS CID Version 0

    Returns:
        str: 32 Bytes long string
    """
    """bytes32 is converted back into Ipfs hash format."""

    decoded = base58.b58decode(cid)
    sliced_decoded = decoded[2:]
    return binascii.b2a_hex(sliced_decoded).decode("utf-8")


def byte32_to_ipfscidv0(hexstr):
    """
    Convert 32 bytes hex string to ipfscidv0.

    Args:
        hexstr (string): 32 Bytes long string

    Returns:
        str: IPFS CID Version 0
    """

    binary_str = binascii.a2b_hex(hexstr)
    completed_binary_str = b'\x12 ' + binary_str
    return base58.b58encode(completed_binary_str).decode("utf-8")

def demo_me():
    """
    Demos the logical and manipulation operations during both convertor methods.

    """
    print(' ')
    print("########## HOW ipfscidv0_to_byte32 WORKS DEMO ")
    ipfscid = "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"
    print("The IPFS CID v0: ", ipfscid)
    b32 = base58.b58decode(ipfscid)
    print("Binary of IPFS CID v0: ", b32)
    b32cid = b32[2:]
    bcut = b32[0:2]
    print("Binary of IPFS CID v0 after omit: ", b32cid)
    print("Omitted section binary: ", bcut)
    b32hex = binascii.b2a_hex(b32cid).decode("utf-8")
    print("Converted Binary of IPFS CID v0 to hex string: ", b32hex)
    print("########## END OF ipfscidv0_to_byte32 OPS DEMO ")
    print(' ')
    print(' ')
    print("########## HOW byte32_to_ipfscidv0 WORKS DEMO ")
    bb32 = binascii.a2b_hex(b32hex)
    print("bb32: ", bb32)
    bb32p = bcut+bb32
    print("bb32p: ", bb32p)
    res = base58.b58encode(bb32p).decode("utf-8")
    print("res: ", res)
    print("########## END OF byte32_to_ipfscidv0 OPS DEMO ")


def test_me():
    """
    Tests ipfscidv0_to_byte32 and byte32_to_ipfscidv0 functions operations.

    """
    print(' ')
    expected = "QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR"
    print("expected: ", expected)
    hexstr = ipfscidv0_to_byte32(expected)
    print("hexstr: ", hexstr)
    actual = byte32_to_ipfscidv0(hexstr)
    print("actual: ", actual)
    print("ARE ACTUAL & EXPECTED VALUES EQUAL: ", bool(expected == actual))

print("IPFS2bytes32 Convertor: ####################################################################################################################");
print("DEMO: ####################################################################################################################");
demo_me();
print(' ');
print("##########################################################################################################################");
print(' ');
print("TEST: ####################################################################################################################");
test_me();
