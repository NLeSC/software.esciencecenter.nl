function reduceFieldsAdd(fields,fieldname) {
  return function(p, v) {
    var values = v[fieldname];

    fields.forEach(function(f) {
      if (values.indexOf(f) > -1) {
        p[f] += 1;
      }
    });
    return p;
  };
}
function reduceFieldsRemove(fields,fieldname) {
  return function(p, v) {
    var values = v[fieldname];

    fields.forEach(function(f) {
      if (values.indexOf(f) > -1) {
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

function bagFilterHandler(dimension, filter){
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
  var competenceChart = dc.rowChart("#dc-competence-chart");
  var expertiseChart = dc.rowChart("#dc-expertise-chart");
  var technologyTagChart = dc.rowChart("#dc-technology-tag-chart");
  var supportLevelChart = dc.rowChart("#dc-support-level-chart");
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
  var fakeDisciplineGroup = fakify(disciplineDimension.groupAll().reduce(reduceFieldsAdd(disciplineValues,'discipline'), reduceFieldsRemove(disciplineValues,'discipline'), reduceFieldsInitial(disciplineValues)));
  var competenceValues = uniqueFieldValues(software_data,'competence');
  var fakeCompetenceGroup = fakify(competenceDimension.groupAll().reduce(reduceFieldsAdd(competenceValues,'competence'), reduceFieldsRemove(competenceValues,'competence'), reduceFieldsInitial(competenceValues)));
  var expertiseValues = uniqueFieldValues(software_data,'expertise');
  var fakeExpertiseGroup = fakify(expertiseDimension.groupAll().reduce(reduceFieldsAdd(expertiseValues,'expertise'), reduceFieldsRemove(expertiseValues,'expertise'), reduceFieldsInitial(expertiseValues)));
  var technologyTagValues = uniqueFieldValues(software_data,'technologyTag');
  var fakeTechnologyTagGroup = fakify(technologyTagDimension.groupAll().reduce(reduceFieldsAdd(technologyTagValues,'technologyTag'), reduceFieldsRemove(technologyTagValues,'technologyTag'), reduceFieldsInitial(technologyTagValues)));
  var programmingLanguageValues = uniqueFieldValues(software_data,'programmingLanguage');
  var fakeProgrammingLanguageGroup = fakify(programmingLanguageDimension.groupAll().reduce(reduceFieldsAdd(programmingLanguageValues,'programmingLanguage'), reduceFieldsRemove(programmingLanguageValues,'programmingLanguage'), reduceFieldsInitial(programmingLanguageValues)));
  var statusGroup = statusDimension.group().reduceCount();
  var supportLevelGroup = supportLevelDimension.group().reduceCount();

  var programmingLanguageCount = programmingLanguageDimension.group().reduceCount();

  programmingLanguageChart
    .width(200)
    .height(140)
    .dimension(programmingLanguageDimension)
    .group(fakeProgrammingLanguageGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .xAxis().tickFormat(d3.format("d"));
  if (programmingLanguageFilter) {
    languageChart.filter(programmingLanguageFilter);
  }

  competenceChart
    .width(200)
    .height(140)
    .dimension(competenceDimension)
    .group(fakeCompetenceGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (competenceFilter) {
    competenceChart.filter(competenceFilter);
  }

  expertiseChart
    .width(200)
    .height(180)
    .dimension(expertiseDimension)
    .group(fakeExpertiseGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (expertiseFilter) {
    expertiseChart.filter(expertiseFilter);
  }

  disciplineChart
    .width(200)
    .height(140)
    .dimension(disciplineDimension)
    .group(fakeDisciplineGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (disciplineFilter) {
    disciplineChart.filter(disciplineFilter);
  }

  technologyTagChart
    .width(200)
    .height(180)
    .dimension(technologyTagDimension)
    .group(fakeTechnologyTagGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (technologyTagFilter) {
    technologyTagChart.filter(technologyTagFilter);
  }

  statusChart
    .width(200)
    .height(140)
    .dimension(statusDimension)
    .group(statusGroup)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (statusFilter) {
    statusChart.filter(statusFilter);
  }

  supportLevelChart
    .width(200)
    .height(140)
    .dimension(supportLevelDimension)
    .group(supportLevelGroup)
    .elasticX(true)
    .colors(d3.scale.category20());
  if (supportLevelFilter) {
    supportLevelChart.filter(supportLevelFilter);
  }

  dataTable.width(650).height(800)
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