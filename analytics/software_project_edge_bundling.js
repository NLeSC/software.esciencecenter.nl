var entries_handler = function(data,names) {
  var entries = [];
  for (i in data) {
    var usedIn = [];
    if (data[i].usedIn == null) { continue; }
    for (u in data[i].usedIn) {
      usedIn.push("Project.Project." + data[i].usedIn[u].replace(/^.*\//,""));
      if (names[data[i].usedIn[u].replace(/\/$/,"")] == undefined) {
        entries.push({
          "name" : "Project.Project." + data[i].usedIn[u].replace(/^.*\//,""),
          "link" : data[i].usedIn[u],
          "size" : 8000,
          "imports" : []
        });
      }
      names[data[i].usedIn[u].replace(/\/$/,"")] = "Project.Project." + data[i].usedIn[u].replace(/^.*\//,"");
    }
    var entry = {
      "name" : names[data[i]["@id"].replace(/\/$/,"")],
      "link" : data[i]["@id"],
      "size" : 8000,
      "imports" : usedIn
    };
    entries.push(entry);
    }
  return entries;
}
