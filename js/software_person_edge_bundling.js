var entries_handler = function(data,names) {
  var entries = [];
  for (i in data) {
    var contributor = [];
    if (data[i].contributor == null) { continue; }
    for (u in data[i].contributor) {
      if (data[i].contributor[u].name != null) { continue; }
      console.log(data[i].contributor[u]);
      contributor.push("Person.Person." + data[i].contributor[u].replace(/^.*\//,"").replace(".","_"));
      if (names[data[i].contributor[u].replace(/\/$/,"")] == undefined) {
        entries.push({
          "name" : "Person.Person." + data[i].contributor[u].replace(/^.*\//,"").replace(".","_"),
          "size" : 8000,
          "link" : data[i].contributor[u],
          "imports" : []
        });
      }
      names[data[i].contributor[u].replace(/\/$/,"")] = "Person.Person." + data[i].contributor[u].replace(/^.*\//,"");
    }
    var entry = {
      "name" : names[data[i]["@id"].replace(/\/$/,"")],
      "size" : 8000,
      "link" : data[i]["@id"],
      "imports" : contributor
    };
    entries.push(entry);
  }
  return entries;
}
