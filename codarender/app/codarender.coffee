
fetch_data = (dataset, variable, success) ->
    xhr = new XMLHttpRequest()
    xhr.open('GET', "/api/#{dataset}/data/#{variable}", true);
    xhr.responseType = 'arraybuffer';

    xhr.onload = (e) ->
        array_buf = new Float32Array(this.response)
        success(array_buf)

    xhr.send();

render_trace = (divid, dataset, variable) ->
    # hack
    timesteps = d3.range(10001, 109982, 20)

    margin = {top: 20, right: 20, bottom: 30, left: 50}
    width = 960 - margin.left - margin.right
    height = 500 - margin.top - margin.bottom
    
    x = d3.scale.linear().range([0, width])
    y = d3.scale.linear().range([height, 0])
    
    xAxis = d3.svg.axis().scale(x).orient("bottom")
    yAxis = d3.svg.axis().scale(y).orient("left")

    line = d3.svg.line()
        .x((d) -> x(d[0]))
        .y((d) -> y(d[1]))

    svg = d3.select("##{divid}").append('svg')
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
        
    x.domain(d3.extent(timesteps, (d) -> d))
    
    # after having set everything up do the asynchronous bit
    fetch_data(dataset, variable, (buf) ->
        y.domain(d3.extent(buf, (d) -> d))
        
        svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis)

        svg.append("g")
          .attr("class", "y axis")
          .call(yAxis)
        .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", ".71em")
          .style("text-anchor", "end")
          .text("#{variable}")
        
        svg.append("path")
          .datum(d3.zip(timesteps, buf))
          .attr("class", "line-trace")
          .attr("d", line)
    )
    
module.exports.render_trace = render_trace