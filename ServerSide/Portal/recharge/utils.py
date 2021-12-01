import uuid

def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "")[:7]
    return code
def generate_ref_code1():
    code = str(uuid.uuid4()).replace("-", "")[:8]
    return code  

def generate_ref_code2():
    code = str(uuid.uuid4()).replace("-", "")[:10]
    return code 