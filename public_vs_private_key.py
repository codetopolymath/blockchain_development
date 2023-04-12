"""
an easy to understand way of private and public keys is treat them as password and username.
    WEB2 : username, password
    WEB3 :  public_key, private_key
PUBLIC VS PRIVATE KEY:
    in blockchain world we use key to sign data, authenticate message and protect it from being altered by unauthorized users.
    public key can be distributed but private key should kept secret as it used to sign transaction and can be used to fake you.
    from private key you can generate public key but you can not trace back private key from given public key.

"""

#   `sudo apt-get install openssl` :install openssl to get genrsa function
#   `openssl genrsa -out private_key_name.pem 1024` :generate private key
#   `openssl rsa -in private_key_name.pem -pubout > public_key_name.pum` :generate public key from private key

# BELOW CODE IS TO ILLUSTRATE WHY PRIVATE & PUBLIC KEY HOLD RELATIONSHIP AND HOW THEY ARE CO-RELLATED
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    """generate private key"""
    private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend())

def verify_message():
    """
    validate message: can be validate by other peers as it is based on public key
        to verify a message using signature you only need public key
    """
    public_key.verify(
            signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256()
            )

def falsify_message():
    """
    validate messsage with fake data: if changes are made into previous block and then tried to verify message

    """
    message = b"rohit can't do it, hahaha"
    signature = b"this is fake signature"

    with open ("first_public_key.pub", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
                key_file.read(), backend=default_backend())

    public_key.verify(
            signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())


"""
    EXPLANATION:
        AUTHOR:
            message ---> hash calculated ---> encrypted with private key ---> signature generated
        VERIFYER:
            calculated hash from message == decrypt signature with public key
                if false: either message altered or private key is different.
"""
















