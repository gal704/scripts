import sys
from Crypto.Hash import SHA256
from Crypto.Cipher import AES


def print_help():
    print "Bad input\n"
    print "Usage:"
    print "\tpython encdec.py mode path_to_input_file path_to_output_file password\n"
    print "mode: encrypt/decrypt"


def createHeader(data_length):
    magic = "DEAD0BFF"
    pad = 16 - ((4 + 8 + data_length) % 16)
    header_length = "%04x" % (pad + len(magic) + 4)
    header = magic + header_length + pad * "0"
    return header


def validateAndSkipHeader(first_twelve_bytes):
    if first_twelve_bytes[:8] != "DEAD0BFF":
        print "%x" % first_twelve_bytes[0]
        return False
    bytes_to_skip = int(first_twelve_bytes[8:], 16)
    if bytes_to_skip == 0:
        return -1
    return bytes_to_skip


def encrypt(path_to_input_file, path_to_output_file, password):
    print "encrypt"
    hash_key = SHA256.new(password).hexdigest()
    input_file = open(path_to_input_file, "rb")
    output_file = open(path_to_output_file, "wb")
    data = input_file.read()
    input_file.close()
    iv = hash_key[:16]
    cipher = AES.new(hash_key[32:64], AES.MODE_CBC, iv)
    header = createHeader(len(data))
    encrypted_data = cipher.encrypt(header + data)
    output_file.write(encrypted_data)
    output_file.close()
    return True


def decrypt(path_to_input_file, path_to_output_file, password):
    print "decrypt"
    hash_key = SHA256.new(password).hexdigest()
    input_file = open(path_to_input_file, "rb")
    output_file = open(path_to_output_file, "wb")
    data = input_file.read()
    input_file.close()
    iv = hash_key[:16]
    cipher = AES.new(hash_key[32:64], AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(data)
    bytes_to_skip = validateAndSkipHeader(decrypted_data[:12])
    if not bytes_to_skip:
        return False
    output_file.write(decrypted_data[bytes_to_skip:])
    output_file.close()
    return True

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print_help()
        exit()
    if sys.argv[1] == "encrypt":
        if encrypt(sys.argv[2], sys.argv[3], sys.argv[4]):
            print "the file was encrypted successfully"
    elif sys.argv[1] == "decrypt":
        if decrypt(sys.argv[2], sys.argv[3], sys.argv[4]):
            print "the file was decrypted successfully"
    else:
        print_help()
    exit()
