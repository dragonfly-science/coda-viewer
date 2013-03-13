# coda-viewer

Viewer for CODA files that store the output from BUGS models

This consists of a Django application for accessing and serving data from
CODA files and a coffeescript based client-side application for rendering 
visualizations of the data using d3.

## Django Application

This is a fairly basic django application with the addition of an api layer
which serves data directly from the CODA files to the client side visualisation
application. Currently (14-March-2013), the api is very basic and eventually
will probably be replaced with a full blown tastypie based api. The api has been
versioned so that the current (evolving) api will be accessible (as v0) once
a more complete api has been created.

**Installation** create a virtualenv and run `pip install -r requirements.txt`.
The settings.py file currently only supports debug mode.

## Client Side Visualisation Application

Currently (14-March-2013), this is fairly basic but will enevntually be a 
psuedo single page application for each django view - and each django view will
be a type of visualisation of the data.

**Installation** [brunch.io](http://brunch.io) is being used to build the 
coffeescript. Run `npm install -g brunch` to install this and then run 
`npm install .` in the codarender directory. Once brunch has been installed
then just run `brunch w` in the codarender directory to continuously build the
application.

