class Overview extends Spine.Controller
  events: 'click #plot-selected': 'clicked_selected', 'click #plot-all': 'clicked_all'

  constructor: ->
    super
    @routes
      "/users/:id": (params) ->
        console.log("/users/", params.id)
      "/users": ->
        console.log("users")
        
    Spine.Route.setup()
    
  render: ->
    ctx_obj = this # TODO: risto ~ Fri Mar 15 14:27:26 NZDT 2013 >>> got to be a better way
    $.getJSON("/api.v0/#{@dataset}/variables", (data) ->
      ctx_obj.html require('views/overview')({variables: data, size:12})      
    )
  
  # this works but it is not what we want to do as we should be using #urlfragments
  clicked_selected: (e) ->
    console.log e
    
  clicked_all: (e) ->
    console.log e

module.exports = Overview
    