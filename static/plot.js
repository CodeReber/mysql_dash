let aggrname_select = document.getElementById('aggrname');
const button = document.querySelector('.btn');
// console.log(button)
// aggrname_select.onchange = function()

  button.addEventListener('click', event =>{
  event.preventDefault();
  aggrid = aggrname_select.value; 
  console.log(aggrid)
  fetch('/api/chart/' + aggrid).then(function(response){
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
});