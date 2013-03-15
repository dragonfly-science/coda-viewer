class Overview extends Spine.Controller
  constructor: ->
    super
    @routes
      "plot-all": ->
        @render_plots()
        console.log 'plot-all'
      "plot-selected": ->
        console.log 'plot-selected'
        
    Spine.Route.setup()
    
  render: ->
    ctx_obj = this # TODO: risto ~ Fri Mar 15 14:27:26 NZDT 2013 >>> got to be a better way
    $.getJSON("/api.v0/#{@dataset}/variables", (data) ->
      ctx_obj.html require('views/overview')({variables: data, size:12})      
    )
    
  render_plots: ->
    @html "<h1>Some Plots</h1>"
    
    # TODOs
    # - setup routing so that clicking back to bare overview gives back the list
    # of variables - and preserves the state so that the list of variables is 
    # the same
    # - probably need to setup a model to store variable data in for this to 
    # work
    # - need to think about how to use routing and model sync to server to 
    # allow for storing the history of the session - could be a really neat and
    # easy way to achieve this

module.exports = Overview
    