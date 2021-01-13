from typing import List


class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        encoder: List[str] = [''] * 26
        decode: List[str] = [''] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decode[k] = chr((k - shift) % 26 + ord('A'))

        self._forward = ''.join(encoder)
        self._backward = ''.join(decode)

    def encrypt(self, message):
        """Return string representing encrypted message."""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)

    @staticmethod
    def _transform(message, s):
        """"""
        s1 = []
        for i in message:
            if i.isupper():
                s1.append(s[ord(i) - ord('A')])
            else:
                s1.append(i)
        return ''.join(s1)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    m = "THE EAGLE IS N PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(m)
    print(coded)
    answer = cipher.decrypt(coded)
    print(answer)
