
fetch_data = (dataset, variable, success) ->
    xhr = new XMLHttpRequest()
    xhr.open('GET', "/api/#{dataset}/data/#{variable}", true);
    xhr.responseType = 'arraybuffer';

    xhr.onload = (e) ->
        array_buf = new Float32Array(this.response)
        success(array_buf)

    xhr.send();

render_trace = (divid, dataset, variable) ->
    svg = d3.select("##{divid}").append('svg')
    
    # hack
    timesteps = d3.range(10001, 109982, 20)

    margin = {top: 20, right: 20, bottom: 30, left: 50}
    width = 960 - margin.left - margin.right
    height = 500 - margin.top - margin.bottom
    
    x = d3.scale.linear().range([width, 0])
    y = d3.scale.linear().range([height, 0])
    
    xAxis = d3.svg.axis().scale(x).orient("bottom")

    yAxis = d3.svg.axis().scale(y).orient("left")

    line = d3.svg.line()
        .x((d) -> x(d.date))
        .y((d) -> y(d.close))

    # after having set everything up do the asynchronous bit
    fetch_data(dataset, variable, (buf) ->
        console.log buf.length
    )
    
module.exports.render_trace = render_trace