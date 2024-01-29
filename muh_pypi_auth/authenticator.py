import pyotp
import getpass

def get_totp_code(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

if __name__ == "__main__":
    secret_key = getpass.getpass("Enter your PyPI 2FA secret key: ")
    code = get_totp_code(secret_key)
    print(f"Current 2FA code: {code}")
