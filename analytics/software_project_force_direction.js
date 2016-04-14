
var width = 960,
    height = 500;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(30)
    .size([width, height]);

var svg = d3.select("body").append("svg")
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
      var names = {};
      var expertise_n = 0;
      var expertise_id = {};
      var name_n = -1;
      var name_id = {};
      var graph = { 
        "nodes" : [],
        "links" : []
      };
      for (i in data) {
        var expertise = "Unknown_Expertise";
        if (data[i].expertise != null) { 
          var expertise = data[i].expertise[0].replace(/\W+/g,"_");
        }
        var name = data[i].name.replace(/\W+/g,"_");
        names[data[i]["@id"].replace(/\/$/,"")] = //competence + "." + 
        expertise + "." + name;
        var exp_id = -1;
        if (expertise_id[expertise] == null) {
          expertise_n = expertise_n + 1;
          expertise_id[expertise] = expertise_n;
        }
        if (name_id[name] == null) {
          name_n = name_n + 1;
          name_id[name] = name_n;
          graph.nodes.push({"name":name, "group":expertise_id[expertise], "nr":name_id[name], "link":data[i]["@id"], "type":"software"});
        }
      }

      for (i in data) {
        if (data[i].usedIn == null) { continue; }
        for (u in data[i].usedIn) {
          var name = data[i].usedIn[u].replace(/^.*\//,"")
          var expertise = "Project";
          var exp_id = -1;
          if (expertise_id[expertise] == null) {
            expertise_n = expertise_n + 1;
            expertise_id[expertise] = expertise_n;
          }
          if (name_id[name] == null) {
            name_n = name_n + 1;
            name_id[name] = name_n;
            graph.nodes.push({"name":name, "group":expertise_id[expertise], "link":"http://software.esciencecenter.nl/project/" + name, "type" : "project"});
          }
          graph.links.push({
            "source" : name_id[data[i].name.replace(/\W+/g,"_")],
            "target" : name_id[name],
            "value" : 1
          });
        }
      }

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
      .attr("class", function(d) {
        return d.type;
      })
      .call(force.drag);

      d3.selectAll(".software")
      .append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function(d) { return color(d.group); })

      d3.selectAll(".project")
      .append("rect")
      .attr("class", "node")
      .attr("x",-5)
      .attr("y",-5)
      .attr("width", 10)
      .attr("height", 10)
      .style("fill", function(d) { return color(d.group); })

      node.on("click", function(d){
        if(d3.event.defaultPrevented) {
          return;
        } else {
          $(location).attr('href', d.link);
          window.location = d.link;
        }
      }); 

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
