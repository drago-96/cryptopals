import base64


def b2u8(b):
    return bytes(b).decode('utf-8')


def b2h(b):
    return bytes(b).hex()


def ba2l(ba):
    return list(ba)


def b64file_to_bytes(abs_path):
    with open(abs_path, 'r') as f:
        lines = f.readlines()
    content = ''.join([line.strip() for line in lines])
    b = base64.b64decode(content)
    return b


def hexfile_lines_to_bytes(abs_path):
    with open(abs_path, 'r') as f:
        lines = f.readlines()
    return [bytes.fromhex(line.strip()) for line in lines]
