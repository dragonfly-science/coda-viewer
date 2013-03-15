# require('lib/setup')

class Overview extends Spine.Controller
  constructor: ->
    super
    
  render: ->
    ctx_obj = this # TODO: risto ~ Fri Mar 15 14:27:26 NZDT 2013 >>> got to be a better way
    $.getJSON("/api.v0/#{@dataset}/variables", (data) ->
      ctx_obj.html require('views/overview')({variables: data, size:12})      
    )

module.exports = Overview
    