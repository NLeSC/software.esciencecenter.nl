function reduceFieldsAdd(fields) {
  return function(p, v) {
    var disciplines = v.discipline;

    fields.forEach(function(f) {
      if (disciplines.indexOf(f) > -1) {
        p[f] += 1;
      }
    });
    return p;
  };
}
function reduceFieldsRemove(fields) {
  return function(p, v) {
    var disciplines = v.discipline;

    fields.forEach(function(f) {
      if (disciplines.indexOf(f) > -1) {
        p[f] -= 1;
      }
    });
    return p;
  };
}
function reduceFieldsInitial(fields) {
  return function() {
    var ret = {};
    fields.forEach(function(f) {
      ret[f] = 0;
    });
    return ret;
  };
}

function fakify(group) {
  return {
    all: function () {
      var hash = group.value();
      var result = [];
      for (var kv in hash) {
        result.push({
          key: kv,
          value: hash[kv]
        });
      }
      return result;
    }
  }
};

function uniqueFieldValues(data,field) {
  return _.uniq(_.flatten(_.map(data,function(x){return _.get(x,field)})));
}

d3.json("/software.json", function (software_data) {
  var disciplineFilter = purl().fparam('discipline');
  var competenceFilter = purl().fparam('competence');
  var expertiseFilter = purl().fparam('expertise');
  var programmingLanguageFilter = purl().fparam('programmingLanguage');
  var licenseFilter = purl().fparam('licenseFilter');
  var supportLevelFilter = purl().fparam('supportLevel');
  var statusFilter = purl().fparam('status');
  var technologyTagFilter = purl().fparam('technologyTag');

  var dataTable = dc.dataTable("#dc-table-graph");
  var programmingLanguageChart = dc.rowChart("#dc-languages-chart");
  var disciplineChart = dc.rowChart("#dc-discipline-chart");
  var statusChart = dc.rowChart("#dc-status-chart");

  var ndx = crossfilter(software_data);

  var softwareDimension = ndx.dimension(function(d) { return d['@id']; });
  var disciplineDimension = ndx.dimension(function(d) { return d.discipline; });
  var competenceDimension = ndx.dimension(function(d) { return d.competence; });
  var expertiseDimension = ndx.dimension(function(d) { return d.expertise; });
  var programmingLanguageDimension =  ndx.dimension(function(d) { return d.programmingLanguage; });
  var supportLevelDimension = ndx.dimension(function(d) { return d.supportLevel; });
  var statusDimension = ndx.dimension(function(d) { return d.status; });
  var technologyTagDimension = ndx.dimension(function(d) { return d.technologyTag; });

  var disciplineValues = uniqueFieldValues(software_data,'discipline');
  var fakeDisciplineGroup = fakify(disciplineDimension.groupAll().reduce(reduceFieldsAdd(disciplineValues), reduceFieldsRemove(disciplineValues), reduceFieldsInitial(disciplineValues)));
  var competenceValues = uniqueFieldValues(software_data,'competence');
  var fakeCompetenceGroup = fakify(competenceDimension.groupAll().reduce(reduceFieldsAdd(competenceValues), reduceFieldsRemove(competenceValues), reduceFieldsInitial(competenceValues)));
  var expertiseValues = uniqueFieldValues(software_data,'expertise');
  var fakeExpertiseGroup = fakify(expertiseDimension.groupAll().reduce(reduceFieldsAdd(expertiseValues), reduceFieldsRemove(expertiseValues), reduceFieldsInitial(expertiseValues)));
  var programmingLanguageValues = uniqueFieldValues(software_data,'programmingLanguage');
  var fakeProgrammingLanguageGroup = fakify(programmingLanguageDimension.groupAll().reduce(reduceFieldsAdd(programmingLanguageValues), reduceFieldsRemove(programmingLanguageValues), reduceFieldsInitial(programmingLanguageValues)));
  var statusGroup = statusDimension.group().reduceCount();

  var programmingLanguageCount = programmingLanguageDimension.group().reduceCount();

  programmingLanguageChart
    .width(340)
    .height(340)
    .dimension(programmingLanguageDimension)
    .group(programmingLanguageCount)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (programmingLanguageFilter) {
    languageChart.filter(programmingLanguageFilter);
  }

  disciplineChart
    .width(340)
    .height(340)
    .dimension(disciplineDimension)
    .group(fakeDisciplineGroup)
    .filterHandler(function(dimension, filter){
      dimension.filterFunction(function(d) {
        var result = true;
        filter.forEach(function(f) {
          if (result === true && d.indexOf(f) === -1) {
            result = false;
          }
        });
        return result;
      });
      // dimension.filter(filter);
      return filter; // set the actual filter value to the new value
    })
    .elasticX(true)
    .colors(d3.scale.category20());
  if (disciplineFilter) {
    disciplineChart.filter(disciplineFilter);
  }

  statusChart
    .width(340)
    .height(340)
    .dimension(statusDimension)
    .group(statusGroup)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (statusFilter) {
    statusChart.filter(statusFilter);
  }

  dataTable.width(800).height(800)
      .dimension(softwareDimension)
      .group(function(d) { return d.competence[0]; })
    .size(100)
    .columns([
        function(d) {
            return '<a href="' + d['@id'].replace('{{ site.url }}', '') + '">' + d.name + '</a>';
        },
        function(d) { return d.tagLine; }
    ])
    .sortBy(function(d){ return d.name; })
    // (optional) sort order, :default ascending
    .order(d3.ascending);


  dc.renderAll();
});