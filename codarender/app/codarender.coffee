
coda_variables = (dataset, success) ->
    $.getJSON("/api/#{dataset}/variables", (data) -> 
        success(data)
    )
    
module.exports.coda_variables = coda_variables