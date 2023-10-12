import socket
def getLocalIP():
    st = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    st.connect(("8.8.8.8",80))
    LIP = st.getsockname()[0]
    st.close()
    return LIP