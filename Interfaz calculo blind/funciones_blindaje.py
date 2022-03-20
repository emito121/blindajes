#LAS FUNCIONES SIGUIENTES Y TABLAS SON EN BASE AL CÁLCULO DE BLINDAJES PARA RAYOS X (NCRP 147).
#Actualmente solo soporta el cálculo para materiales de plomo y hormigón, pero se pueden agregar otros materiales.
#También se puede optimizar mucho más.

import pandas as pd
import numpy as np
from math import log
import os

def kp0(kp1, N, U, d, superficie): 
  '''
  Devuelve kp0 el kerma en aire a d distancia sin blindaje de por medio, correjido con el factor de uso (mGy*semana/metro2)

  donde kp1 es el kerma en aire a un metro de la fuente con una carga de trabajo dada (mGy/paciente)

  N es el promedio de pacientes por semana (adimencional)

  U es el factor de uso estadistico, depende de la sala y la pared (adimencional)

  d es la distancia al punto de interes (en metros)

  superficie es dependiendo hacia que pared, piso o techo va dirigido, ya que dependiendo cual sea se le debe sumar un espesor: 

  si es piso ingrese 0

  si es techo ingrese 1

  si es pared ingrese 2
  '''

  #suma a la distancia dependiendo de que superficie se trata
  if (superficie == 0):
    d2=d+1.7
  elif superficie == 1:
    d2 = d + 0.5
  elif superficie == 2:
    d2 = d + 0.3
  else:
    print("no ingreso un numero de superficie correcto")

  kpo = (kp1*N*U)/d2**2 #calcula el kerma en aire a cierta distancia sin blindaje de por medio

  return kpo

def Bp(P, T, kp0):
  '''
  Retorna la transmision permitida al blindaje primario (adimensional)

  P es el kerma limite permitido en area controlada o supervisada (mGy/semana)

  T factor de ocupación (adimencional)
  
  Kp0 kerma limitante primario a cierta distancia (mGy*semana)

  '''
  Bpe = P/(T*kp0)
  return Bpe

def Bs(P, T, N, KL1, KS1, dL, dS):
  '''
  Retona la transmision permitida al blindaje secundario (adimensional)

  P es el kerma limite permitido en el area controlada o supervisada (mGy/semana)

  T es el factor de ocupación (adimensional)

  N es es el promedio de pasientes por semana (paciente/semana)

  KL1 es el kerma por dispersion lateral (mGy/paciente) a 1 metro

  KS1 es el kerma por fuga (mGy/paciente) a 1 metro

  dL es la distancia por fuga desde el tubo hacia dL distancia (metro)

  dS es la distancia por dispercion secundaria desde un objeto hasta la distancia dS (metro)

  '''
  a = KL1/dL**2
  b = KS1/dS**2
  c = P/(T*N)
  d = 1/(a+b)
  Bsec = c*d
  return Bsec

def espesor(orden, sala, B, equivalente, material):
  '''
  *DEVUELVE EL ESPESOR EN mm

  *orden es si el blindaje es primario o secundario:

  si es primario ingresar 0

  si es secundario ingresar 2

  *sala es que tipo de estudio con rayos x se va a llevar a cabo:

  si es all barriers ingrese 0

  si es chesty bucky ingrese 1

  si es hacia el piso ingrese 2

  *B es la transmision permitida primaria o secundaria 

  *equivalente del receptor de imagen a un material de atenuacion: 

  si es en la mesa o pared ingrese 0

  si es cross-table ingrese 1

  *material con el que se desea hacer el blindaje

  si material es plomo, ingrese 0

  si el material es hormigon, ingrese 1

  si el material es acero, ingrese 2

  '''

  pPlomo = pd.read_csv(f'{os.getcwd()}\\tablas\\primaria plomo.txt', sep = ';')
  sPlomo = pd.read_csv(f'{os.getcwd()}\\tablas\\secundaria plomo.txt', sep = ';')
  pConcreto = pd.read_csv(f'{os.getcwd()}\\tablas\\primaria concreto.txt', sep = ';')
  sConcreto = pd.read_csv(f'{os.getcwd()}\\tablas\\secundaria concreto.txt', sep = ';')
  equivalent = pd.read_csv(f'{os.getcwd()}\\tablas\\equivalente receptor.txt', sep = ';')

  if material == 0: #si el material es plomo
    if orden == 0: #si el bilndaje es para primario
      if sala == 0: # si la sala es de all barriers
        alpha = pPlomo.loc[0,'alpha(mm-1)']
        beta = pPlomo.loc[0,'beta(mm-1)']
        gamma = pPlomo.loc[0,'gamma(mm-1)']
      if sala == 1: # si la sala es chest bucky
        alpha = pPlomo.loc[1,'alpha(mm-1)']
        beta = pPlomo.loc[1,'beta(mm-1)']
        gamma = pPlomo.loc[1,'gamma(mm-1)']
      if sala == 2: # si la sala es de floor
        alpha = pPlomo.loc[2,'alpha(mm-1)']
        beta = pPlomo.loc[2,'beta(mm-1)']
        gamma = pPlomo.loc[2,'gamma(mm-1)']
    if orden == 2: #si el bilndaje es para secundario
      if sala == 0: # si la sala es de all barriers
        alpha = sPlomo.loc[0,'alpha(mm-1)']
        beta = sPlomo.loc[0,'beta(mm-1)']
        gamma = sPlomo.loc[0,'gamma(mm-1)']
      if sala == 1: # si la sala es chest bucky
        alpha = sPlomo.loc[1,'alpha(mm-1)']
        beta = sPlomo.loc[1,'beta(mm-1)']
        gamma = sPlomo.loc[1,'gamma(mm-1)']
      if sala == 2: # si la sala es de floor
        alpha = sPlomo.loc[2,'alpha(mm-1)']
        beta = sPlomo.loc[2,'beta(mm-1)']
        gamma = sPlomo.loc[2,'gamma(mm-1)']

  if material == 1: #si el material es hormigón
    if orden == 0: #si el bilndaje es para primario
      if sala == 0: # si la sala es de all barriers
        alpha = pConcreto.loc[0,'alpha(mm-1)']
        beta = pConcreto.loc[0,'beta(mm-1)']
        gamma = pConcreto.loc[0,'gamma(mm-1)']
      if sala == 1: # si la sala es chest bucky
        alpha = pConcreto.loc[1,'alpha(mm-1)']
        beta = pConcreto.loc[1,'beta(mm-1)']
        gamma = pConcreto.loc[1,'gamma(mm-1)']
      if sala == 2: # si la sala es de all barriers
        alpha = pConcreto.loc[2,'alpha(mm-1)']
        beta = pConcreto.loc[2,'beta(mm-1)']
        gamma = pConcreto.loc[2,'gamma(mm-1)']
    if orden == 2: #si el bilndaje es para secundario
      if sala == 0: # si la sala es de all barriers
        alpha = sConcreto.loc[0,'alpha(mm-1)']
        beta = sConcreto.loc[0,'beta(mm-1)']
        gamma = sConcreto.loc[0,'gamma(mm-1)']
      if sala == 1: # si la sala es chest bucky
        alpha = sConcreto.loc[1,'alpha(mm-1)']
        beta = sConcreto.loc[1,'beta(mm-1)']
        gamma = sConcreto.loc[1,'gamma(mm-1)']
      if sala == 2: # si la sala es de all barriers
        alpha = sConcreto.loc[2,'alpha(mm-1)']
        beta = sConcreto.loc[2,'beta(mm-1)']
        gamma = sConcreto.loc[2,'gamma(mm-1)']

  x = (1/(alpha*gamma))*log((((1/B)**gamma)+(beta/alpha))/(1+(beta/alpha))) #calcula el grosor en mm dependiendo del material del blindaje y si es primario o secundario
  xr = 0 #creamos una variable que es lo que al final se le va a restar al blindaje calculado si hay algo que atenue la radiación antes que la superficie

  if orden == 0: #si es primaria
    if equivalente == 0: #si es camilla o bucky de pared
      if material == 0: #si es plomo el material con el que se está haciendo el blindaje
        xr = equivalent.loc[0,'Plomo(mm)']
      elif material ==1: #si es hormigón el material con el que se está haciendo el blindaje
        xr = equivalent.loc[0,'Hormigón(mm)']
      elif material == 2: #si es acero el material con el que se está haciendo el blindaje
        xr = equivalent.loc[0,'Acero(mm)']
    elif equivalente == 1:
      if material == 0: #si es plomo el material con el que se está haciendo el blindaje
        xr = equivalent.loc[1,'Plomo(mm)']
      elif material ==1:#si es hormigón el material con el que se está haciendo el blindaje
        xr = equivalent.loc[1,'Hormigón(mm)']
      elif material == 2: #si es acero el material con el que se está haciendo el blindaje
        xr = equivalent.loc[1,'Acero(mm)']
    else: #si no ingresan un número de equivalente que sea 0, 1 o 2
      print("no ingreso un numero de equivalente correcto")

  x = x-xr #si hay un equivalente se le resta al espesor calculado anteriormente

  return x #retorna el espesor del blindaje en mm

def calculoBilndaje(Kp1, N, U, dp, superficie, P, T, orden, sala, atenuacion, material):
  Kpo0 = kp0(Kp1, N, U, dp, superficie)
  Bpr = Bp(P, T, Kpo0)
  expesor = espesor(orden, sala, Bpr, atenuacion, material)
  return expesor