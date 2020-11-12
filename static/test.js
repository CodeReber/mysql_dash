fetch('/api/chart/' + 24).then(function(response){
    response.json().then(function(data){
        // console.log(data);
        var arr = [];
        var arr1 = [];
        for (let obj of data.results){
               arr.push(obj.Capacity);
               arr1.push(obj.Date);
        }
    //     x: ["beer", "wine", "martini", "margarita",
    //     "ice tea", "rum & coke", "mai tai", "gin & tonic"],
    //   y: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
var trace1 = {
    x: arr,
    y: arr1,
    type: "line"
  };
  
  var data = [trace1];
  
  var layout = {
    title: "'Line' Chart"
  };
  
  Plotly.newPlot("plot", data, layout);
    });
});