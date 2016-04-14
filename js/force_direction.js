var width = 700,
    height = 500;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(30)
    .size([width, height]);

var svg = d3.select("#network-fd-graph").append("svg")
    .attr("width", width)
    .attr("height", height);

$.ajax({
  type: "GET",
  url: "../software.json",
  async: true,
  cache: false,
  timeout:10000,
  success: function(data){
    if(data){
      var graph = { 
        "nodes" : [],
        "links" : []
      };

      graph_filler(data,graph);

      force
          .nodes(graph.nodes)
          .links(graph.links)
          .start();

      var link = svg.selectAll(".link")
          .data(graph.links)
        .enter().append("line")
          .attr("class", "link")
          .style("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.selectAll(".node")
      .data(graph.nodes)
    .enter()
    .append("g")
      .attr("class", "node")
      .attr("class",function(d){
        return d.type;
      })
      .call(force.drag);

      d3.selectAll(".software")
      .append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function(d) { return color(d.group); })

      d3.selectAll(".person, .project")
      .append("rect")
      .attr("class", "node")
      .attr("x",-5)
      .attr("y",-5)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", function(d) { return color(d.group); })


      node.append("title")
          .text(function(d) { return d.name; });

      node.append("text")
          .attr("dx", 6)
          .attr("dy", 2.5)
          .text(function(d) { 
            if (d.name.length > 15) {
              return d.name.substring(0,15) + "...";
            } else {
              return d.name;
            }});

      node.on("click", function(d){
        if(d3.event.defaultPrevented) {
          return;
        } else {
          $(location).attr('href', d.link);
          window.location = d.link;
        }
      }); 

      force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

      });
    }
  },
  error: function(XMLHttpRequest, textStatus, errorThrown){
    console.log(textStatus + ', ' + errorThrown);
  }
});