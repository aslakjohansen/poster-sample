#!/usr/bin/env python3

from svgnarrative import Model

line_client = 'g18359'
line_meta   = 'g18354'
line_data   = 'g18364'
line_admin  = 'g18349'
lines = [line_client, line_meta, line_data, line_admin]

blocks = 'g49937'

meta = [
  'g34801',
  'g34794',
]
data = [
  'g34794-3',
  'g34801-0',
]
process = 'g34609-1'

second = 'g43117'
update = 'g34794-8'
third  = 'g43117-1'

############################################################ helpers

def store ():
  global i
  filename_svg = 'figs/pollpoll%d.svg' % i
  m.store(filename_svg)
  i += 1

############################################################ main

i = 0
m = Model('figs/pollpoll.svg')

# clear
m.hide(lines)
m.hide(blocks)
m.hide(meta)
m.hide(data)
m.hide(process)
m.hide(second)
m.hide(update)
m.hide(third)
store()

m.show(line_client)
store()

m.show(line_meta)
store()

m.show(meta[0])
store()

m.show(meta[1])
store()

m.show(line_data)
store()

m.show(data[0])
store()

m.show(data[1])
store()

m.show(process)
store()

m.show(blocks)
store()

m.show(second)
store()

m.show(line_admin)
store()

m.show(update)
store()

m.show(third)
store()

