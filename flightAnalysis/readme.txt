the fullFlightAnalysis code contains pretty much everything you need to analyze 
how the aircraft will perform in various flight manuevers.

it can model launching the aircraft by hand, climbs, turns, and level flight.

currently, the model makes a few simple assumptions that you should be aware of.
Lift is modeled simply via TAT as Cl = Cl0 + 2*pi*alpha so that can be replaced 
with actual wind tunnel data. Likewise with Cd (Cd = Cd0 + kCl^2)

the propulsion model is reasonably good and will do a decent model of both prop
and motor. it can be applied to any leg of the flight to come up with an energy 
usage (taking into account performance efficiency during that maneuver)


this is meant to be used as a standalone package requiring no external libraries 
but it can be expanded to whatever users would like...

