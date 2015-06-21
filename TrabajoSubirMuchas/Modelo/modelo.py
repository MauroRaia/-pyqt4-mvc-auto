# -*- coding: utf-8 -*-
class Auto():

  def __init__(self):
    self.cantidad_personas = 0

  def subir_persona(self):
    self.cantidad_personas = self.cantidad_personas + 1

  def bajar_persona(self):
    self.cantidad_personas = self.cantidad_personas - 1

  def subir5_persona(self):
    self.cantidad_personas = self.cantidad_personas + 5

  def bajar5_persona(self):
    self.cantidad_personas = self.cantidad_personas - 5

  def subirX_persona(self,x):
    self.cantidad_personas = self.cantidad_personas + x

  def bajarX_persona(self,x):
      self.cantidad_personas = self.cantidad_personas - x
