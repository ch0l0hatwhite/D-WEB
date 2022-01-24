import requests as st
import time

def dweb():
	print("""
	________  __      _______________________ 
\______ \/  \    /  \_   _____/\______   \
 |    |  \   \/\/   /|    __)_  |    |  _/
 |    `   \        / |        \ |    |   \
/_______  /\__/\  / /_______  / |______  /
        \/      \/          \/         \/ 
        
   CREATED BY CH0L0H4TWH1T3 usage: [https://direccionweb.com]
	""")
	site=input("[*] Pagina > ")
	
	r=st.get(site)
	__statuse__=r.status_code
	c=r.text
	if __statuse__==200:
		print("\n\n[*] SE HA ENCONTRADO LA PAGINA.\n\n")
		time.sleep(1)
		print("\n\n[*] Cargando Formato ..\n\n")
		print("\n\n[*] PAGINA DESCARGADA!")
		a=open("/storage/emulated/0/pagina_python.html","w")
		a.write(c)
		a.close()
	else:
		print("[--] PAGINA NO ENCONTRADA...")

dweb()



	