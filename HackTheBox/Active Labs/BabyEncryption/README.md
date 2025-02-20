# 1/ BabyEncryption
### 📜 CHALLENGE DESCRIPTION 📜
You are after an organised crime group which is responsible for the illegal weapon market in your country. As a secret agent, you have infiltrated the group enough to be included in meetings with clients. During the last negotiation, you found one of the confidential messages for the customer. It contains crucial information about the delivery. Do you think you can decrypt it?
### :dart: SOLUTION :dart:
To decrypt the message that was encrypted using the provided encryption function, we need to reverse the encryption process. The encryption function applies a linear transformation to each character in the message, specifically:

`ct = (123 \times \text{char} + 18) \mod 256`

To decrypt, we need to find the inverse of this transformation. The decryption process can be broken down into the following steps:

- Subtract 18 from the ciphertext value.
- Multiply by the modular inverse of 123 modulo 256.

#### Finding the Modular Inverse
To find the modular inverse of 123 modulo 256, we can use the Extended Euclidean Algorithm. The modular inverse ( x ) of ( a ) modulo ( m ) satisfies:

`a \times x \equiv 1 \mod m`
