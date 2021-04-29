from ping3  import ping

def test_if_real(email):
    temp=str(email).split("@")
    link=str(temp[1])
    if ping(link):
        return False
    else:
        return True
