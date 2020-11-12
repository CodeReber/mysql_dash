let aggrname_select = document.getElementById('aggrname');
console.log(aggrname_select)
fetch('/api/chart/' + 24).then(function(response){
    response.json().then(function(data){
        // console.log(data);
        var capacities = [];
        var dates = [];
        for (let obj of data.results){
               capacities.push(obj.Capacity);
               dates.push(obj.Date);
        }
var trace1 = {
    x: capacities,
    y: dates,
    type: "line"
  };
  
  var data = [trace1];
  
  var layout = {
    title: "'Line' Chart"
  };
  
  Plotly.newPlot("plot", data, layout);
    });
});