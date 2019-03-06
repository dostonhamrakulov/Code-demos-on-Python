#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys, socket

def create_error_page(conn, err_string):
    conn.send('HTTP/1.1 200 OK\r\n')
    conn.send('Connection: close\r\n')
    conn.send('Content-Type: text/html\r\n\r\n')
    conn.send('<html><head><title>ERROR</title></head>\r\n')
    conn.send('<body><h1>Error</h1><hr/><p>%s</p></body></html>'%(err_string))
    conn.close()

def handleRequest(conn):
    data = conn.recv(1024)

    try:
        head, body = data.split('\r\n\r\n')
    except:
        head = data
        body = 0;

    header = {}
    values = {}

    lines = head.split('\r\n')
    for line in lines[1:]:
        key, value = line.split(': ')
        header[key] = value
    

    #//TODO: get cookie information from Browser
    # even if connection is closed or browser tab is closed
    cookies={}
    if 'Cookie' in header:
        pairs = header['Cookie'].split(';')
        for pair in pairs:
            key, value = pair.split('=')
            cookies[key.strip()] = value.strip()

    if body:
        pairs = body.split('&')
        for pair in pairs:
            key, value = pair.split('=')
            values[key] = value

    #try:
        #kf = open(KONTOSTANDFILE, "r")
        #kontostand = float(kf.read(1024))
        #kf.close()
    #except:
        #kontostand = 100

    if cookies.has_key('balance'):
        kontostand = float(cookies['balance'])
    else:
        kontostand = 100


    if values.has_key('amount'):
        try:
            amount = float(values['amount'])
        except:
            create_error_page(conn, "%s ist kein Fliesskommawert"%(values['amount']))
            return

        if amount<=kontostand:
            kontostand -= amount
        else:
            create_error_page(conn, "%s ist nicht korrekt Betrag" % (values['amount']))
            return

        #try:
            #kf = open(KONTOSTANDFILE, "w")
            #kf.write("%5.2f"%(kontostand))
            #kf.close()            
        #except:
            #create_error_page(conn, "Probleme mit dem Kontostandsfile")
            #return

    conn.send('HTTP/1.1 200 OK\r\n')
    conn.send('Connection: close\r\n')
    conn.send('Content-Type: text/html\r\n')
    conn.send('Set-Cookie: balance=%5.2f\r\n\r\n'%(kontostand))


    conn.send('<html><head><title>Konto</title></head>\r\n')
    conn.send('<body><h1>Konto</h1><hr/>\r\n')
    if values.has_key('amount'):
        conn.send('<p>Überwiesen = %5.2f</p>\r\n'%(amount))
    conn.send('<p>Neuer Kontostand = %5.2f</p>\r\n'%(kontostand))
    conn.send('<form method="POST">\r\n')
    conn.send('<p>Betrag zum Überweisen: <input type="text" name="amount"/></p>\r\n')
    conn.send('<p><input type="submit" value="Abschicken"/></p>\r\n')
    conn.send('</form>\r\n')
    conn.send('</body></html>\r\n')
    conn.close()
    return

#KONTOSTANDFILE = 'konto.txt'

TCP_IP = ''
TCP_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    handleRequest(conn)
