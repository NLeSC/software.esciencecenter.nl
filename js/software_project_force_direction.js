var graph_filler = function(data,graph) {
  var names = {};
  var expertise_n = 0;
  var expertise_id = {};
  var type_id = {};
  var name_n = -1;
  var name_id = {};

  for (i in data) {
    var expertise = "Unspecified";
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
      type_id[expertise_n] = expertise;
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
  return type_id;
}