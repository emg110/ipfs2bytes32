/**
 * Includes functions to convert between IPFS CID version 0 (Base58), and a 32 bytes hex string
 * TypeScript module.
 */

import { encode, decode } from 'bs58';

/**
 * Converts IPFS CID version 0 (Base58) to a 32 bytes hex string and adds initial 0x.
 * @param cid - The 46 character long IPFS CID V0 string (starts with Qm).
 * @returns string
 */
export function convertIpfsCidV0ToByte32(cid: string) {
  return `0x${decode(cid).slice(2).toString('hex')}`;
}

/**
 * Converts 32 byte hex string (initial 0x is removed) to Base58 IPFS content identifier version 0 address string (starts with Qm)
 * @param str - The 32 byte long hex string to encode to IPFS CID V0 (without initial 0x).
 * @returns string 
 */
export function convertByte32ToIpfsCidV0(str: string) {
  if (str.indexOf('0x') === 0) {
    str = str.slice(2)
  }
  return encode(Buffer.from(`1220${str}`, 'hex'));
}