#!/usr/bin/python
# -*- coding: utf-8 -*-
# Код взят из книги "Программируем коллективный разум" Тоби Сегаран
import os, sys
from math import sqrt

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


critics['Lisa Rose']['Lady in the Water']=2.5
critics['Toby']['Snakes on a Plane']=4.5
critics['Toby']
{'Snakes on a Plane':4.5,'You, Me and Dupree':1.0}









# Возвращает коэффициент корреляции Пирсона между p1 и p2
def sim_pearson(prefs,p1,p2):
  # Получить список предметов, оцененных обоими
  si={}
  for item in prefs[p1]:
    if item in prefs[p2]: si[item]=1
  # Найти число элементов
  n=len(si)
  # Если нет ни одной общей оценки, вернуть 0
  if n==0: return 0
  # Вычислить сумму всех предпочтений
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  # Вычислить сумму квадратов
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
  # Вычислить сумму произведений
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  # Вычислить коэффициент Пирсона
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r


print sim_pearson(critics,'Lisa Rose','Gene Seymour')
