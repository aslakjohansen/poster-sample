#!/usr/bin/env python3

from svgnarrative import Model

meta_setpoint = {
  "point-type": "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-5-1-3",
  "modality":   "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-8-97",
  "unit":       "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-1-4-8",
  "room":       "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-7-9-9",
  "room-area":  "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-56-0-43",
}
meta_sensor = {
  "point-type": "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-5-17",
  "modality":   "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-17",
  "unit":       "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-1-6",
  "room":       "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-7-5",
  "room-area":  "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-56-1",
}
meta_actuator = {
  "point-type": "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-5-1-4-8",
  "modality":   "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-8-9-86",
  "unit":       "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-1-4-6-4",
  "room":       "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-7-9-5-9",
  "room-area":  "text2298-3-7-2-8-8-0-5-5-0-4-1-8-1-7-5-2-9-0-56-0-4-7",
}
meta_edges = {
  "setpoint": "path34644-1-5-2-0-7-9",
  "sensor":   "path34644-1-5-2-0-15",
  "actuator": "path34644-1-5-2-0-7-8-8",
}
ts_u180_setpoint = "g4962-8"
ts_u180_sensor   = "g4966-4"
ts_u180_actuator = "g4970-4"
ts_u178 = "g25702-4-2-9-1"
ts_u181 = "g25702-4-2-9"
ts = [
  ts_u180_setpoint,
  ts_u180_sensor,
  ts_u180_actuator,
  ts_u178,
  ts_u181,
]
rooms = {
  "178": [
    "path34644-1-5-2-0-7-9-3-3-4-0",
    "path34644-1-5-2-0-15-3-56-7-1",
    "path34644-1-5-2-0-7-9-3-0-3-9-8",
    "g33043-8-9-6",
  ],
  "180": [
    "path34644-1-5-2-0-7-9-3",
    "path34644-1-5-2-0-15-3",
    "path34644-1-5-2-0-7-9-3-0",
    "g33043",
  ],
  "181": [
    "path34644-1-5-2-0-7-9-3-3-4",
    "path34644-1-5-2-0-15-3-56-7",
    "path34644-1-5-2-0-7-9-3-0-3-9",
    "g33043-8-9",
  ],
}
dampers = {
  "178": [
    "path34644-1-5-2-0-15-3-4-7-1-9",
    "g33043-0-6-5-9",
  ],
  "180": [
    "path34644-1-5-2-0-15-3-4",
    "g33043-0",
  ],
  "181": [
    "path34644-1-5-2-0-15-3-4-7-1",
    "g33043-0-6-5",
  ],
}
duct = [
  "path34644-1-5-2-0-15-3-4-7-7-6",
  "path34644-1-5-2-0-15-3-4-4",
  "path34644-1-5-2-0-15-3-4-7-7-6-6",
  "g33043-05",
  "path34644-1-5-2-0-15-3-4-7-7-6-5",
]
extra_ts = [
  "g65122",
  "g65128",
  "g65134",
  "g46926",
]
extra_meta_specific = [
  "g65139",
  "g65144",
  "g65149",
]
extra_meta_generic = [
  "g46690-3-4-9",
  "g46690",
  "g46690-3-4",
  "g46690-40-9-2-4",
  "g46690-4-3-1-4",
  "g46690-40",
  "g46690-4",
  "g46690-40-9-2",
  "g46690-4-3-1",
  "g46690-9",
]

############################################################ helpers

def store ():
  global i
  filename_svg = 'figs/metadata%d.svg' % i
  m.store(filename_svg)
  i += 1

############################################################ main

i = 0
m = Model('figs/metadata.svg')

# clear
m.hide(list(map(lambda key: meta_setpoint[key], meta_setpoint.keys())))
m.hide(list(map(lambda key: meta_sensor[key]  , meta_sensor.keys())))
m.hide(list(map(lambda key: meta_actuator[key], meta_actuator.keys())))
m.hide(list(map(lambda key: meta_edges[key]   , meta_edges.keys())))
m.hide(ts)
for room in rooms:
  m.hide(rooms[room])
for damper in dampers:
  m.hide(dampers[damper])
m.hide(duct)
m.hide(extra_ts)
m.hide(extra_meta_specific)
m.hide(extra_meta_generic)
store()

# initial timeseries
m.show(ts_u180_setpoint)
store()
m.show(ts_u180_sensor)
store()
m.show(ts_u180_actuator)
store()

# adding key-value metadata
m.show(list(map(lambda key: meta_edges[key]   , meta_edges.keys())))
for key in ["modality", "unit", "point-type", "room", "room-area"]:
  m.show(meta_setpoint[key])
  m.show(meta_sensor[key])
  m.show(meta_actuator[key])
  store()

# remaining timeseries
m.show(ts_u178)
store()
m.show(ts_u181)
store()

# add room nodes
for room in rooms:
  m.show(rooms[room])
m.hide(meta_setpoint["room"])
m.hide(meta_sensor["room"])
m.hide(meta_actuator["room"])
store()

# add damper nodes
for damper in dampers:
  m.show(dampers[damper])
store()

# add duct node
m.show(duct)
store()

# add extra timeseries
m.show(extra_ts)
store()

# add specific metadata
m.show(extra_meta_specific)
m.hide(meta_setpoint["room-area"])
m.hide(meta_sensor["room-area"])
m.hide(meta_actuator["room-area"])
store()

# add generic metadata
m.show(extra_meta_generic)
store()

