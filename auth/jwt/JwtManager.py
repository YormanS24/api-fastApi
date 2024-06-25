from jwt import encode,decode;

def createToken(data:dict)->str:
    return str(encode(payload=data,key="Profeta2@",algorithm="HS256"));

def validateToken(token: str)-> dict:    
    return dict(decode(token,key="Profeta2@",algorithms=['HS256']));