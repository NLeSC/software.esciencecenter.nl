function deterministicShuffle(a,seed){
    // A little error handling, whynot!
    if(!seed)
        throw new Error("deterministicShuffle: seed not given, or 0");

    var temp,j,array=a.slice(0);

    for(var i=0; i<array.length; i++){
        // Select a "random" position.
        j = (seed % (i+1) + i) % array.length;

        // Swap the current element with the "random" one.
        temp=array[i];
        array[i]=array[j];
        array[j]=temp;

    }

    return array;
}

function reduceFieldsAdd(fields,fieldname) {
  return function(p, v) {
    var values = v[fieldname] || 'None';

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
    var values = v[fieldname] || 'None';

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
    },
    top: function(k) {
      tops = _.take(_.sortBy(_.keys(group.value()),function(item) {
        return group.value()[item] * -1;
      }),k);
      var result = [];
      for (var k in tops) {
        result.push({
          key: tops[k],
          value: group.value()[tops[k]]
        });
      }
      return result;
    }
  };
}

function uniqueFieldValues(data,field) {
  return _.uniq(_.flatten(_.map(data, function(x){ return _.get(x, field) || 'None'; })));
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

var chartwidth = 250;
var barheight = 25;
var gapheight = 1;
var margin = 0;

function chartheight(nvalues) {
  return (nvalues-1) * gapheight + (barheight * nvalues) + margin;
}

d3.json("/software.json", function (software_data) {

  var partyFilter = purl().fparam('inGroup');
  var disciplineFilter = purl().fparam('discipline');
  var competenceFilter = purl().fparam('competence');
  var expertiseFilter = purl().fparam('expertise');
  var programmingLanguageFilter = purl().fparam('programmingLanguage');
  //var supportLevelFilter = purl().fparam('supportLevel');
  var statusFilter = purl().fparam('status');
  var technologyTagFilter = purl().fparam('technologyTag');
  var licenseFilter = purl().fparam('license');

  var dataTable = dc.dataTable("#dc-table-graph");
  var programmingLanguageChart = dc.rowChart("#dc-languages-chart");
  var partyChart = dc.rowChart("#dc-party-chart");
  var disciplineChart = dc.rowChart("#dc-discipline-chart");
  var competenceChart = dc.rowChart("#dc-competence-chart");
  var expertiseChart = dc.rowChart("#dc-expertise-chart");
  var technologyTagChart = dc.rowChart("#dc-technology-tag-chart");
  //var supportLevelChart = dc.rowChart("#dc-support-level-chart");
  var statusChart = dc.rowChart("#dc-status-chart");
  var licenseChart = dc.rowChart("#dc-license-chart");

  var ndx = crossfilter(software_data);
  var all = ndx.groupAll();

  var softwareDimension = ndx.dimension(function(d) { return d['@id']; });
  var endorsedbyDimension = ndx.dimension(function(d) { return d.inGroup || 'Other'; });
  var disciplineDimension = ndx.dimension(function(d) { return d.discipline || 'None'; });
  var competenceDimension = ndx.dimension(function(d) { return d.competence || 'None'; });
  var expertiseDimension = ndx.dimension(function(d) { return d.expertise || 'None'; });
  var programmingLanguageDimension =  ndx.dimension(function(d) { return d.programmingLanguage || 'None'; });
  //var supportLevelDimension = ndx.dimension(function(d) { return d.supportLevel || 'None'; });
  var statusDimension = ndx.dimension(function(d) { return d.status || 'None'; });
  var technologyTagDimension = ndx.dimension(function(d) { return d.technologyTag || 'None'; });
  var licenseDimension = ndx.dimension(function(d) { return d.license || 'None'; });

  var endorsedbyValues = uniqueFieldValues(software_data,'inGroup');
  var fakePartyGroup = fakify(endorsedbyDimension.groupAll().reduce(reduceFieldsAdd(endorsedbyValues, 'inGroup'), reduceFieldsRemove(endorsedbyValues, 'inGroup'), reduceFieldsInitial(endorsedbyValues)));
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
  var licenseValues = uniqueFieldValues(software_data,'license');
  var fakeLicenseGroup = fakify(licenseDimension.groupAll().reduce(reduceFieldsAdd(licenseValues,'license'), reduceFieldsRemove(licenseValues,'license'), reduceFieldsInitial(licenseValues)));
  var statusGroup = statusDimension.group().reduceCount();
  //var supportLevelGroup = supportLevelDimension.group().reduceCount();

  var programmingLanguageCount = programmingLanguageDimension.group().reduceCount();

  programmingLanguageChart
    .width(chartwidth)
    .height(chartheight(programmingLanguageValues.length))
    .fixedBarHeight(barheight)
    .dimension(programmingLanguageDimension)
    .group(fakeProgrammingLanguageGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .colors(d3.scale.ordinal().range(deterministicShuffle(colorbrewer.Set3[12],2)))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (programmingLanguageFilter) {
    programmingLanguageChart.filter(programmingLanguageFilter);
  }
  programmingLanguageChart.ordering(function(d){ return -d.value });

  competenceChart
    .width(chartwidth)
    .height(chartheight(competenceValues.length))
    .fixedBarHeight(barheight)
    .dimension(competenceDimension)
    .group(fakeCompetenceGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .colors(d3.scale.ordinal().range(deterministicShuffle(colorbrewer.Set1[3],3)))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (competenceFilter) {
    competenceChart.filter(competenceFilter);
  }
  competenceChart.ordering(function(d){ return -d.value });

  expertiseChart
    .width(chartwidth)
    .height(chartheight(Math.min(expertiseValues.length,8)))
    .fixedBarHeight(barheight)
    .dimension(expertiseDimension)
    .group(fakeExpertiseGroup)
    .filterHandler(bagFilterHandler)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .elasticX(true)
    .colors(d3.scale.ordinal().range(deterministicShuffle(colorbrewer.Spectral[11],5)))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (expertiseFilter) {
    expertiseChart.filter(expertiseFilter);
  }
  expertiseChart.ordering(function(d){ return -d.value }).rowsCap(8).othersGrouper(false);

  partyChart
    .width(chartwidth)
    .height(chartheight(endorsedbyValues.length))
    .fixedBarHeight(barheight)
    .dimension(endorsedbyDimension)
    .group(fakePartyGroup)
    .filterHandler(bagFilterHandler)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .elasticX(true)
    .colors(d3.scale.ordinal().range(['#00a3e3','#cccccc']))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (partyFilter) {
    partyChart.filter(partyFilter);
  }
  partyChart.ordering(function(d){ return -d.value });

  disciplineChart
    .width(chartwidth)
    .height(chartheight(disciplineValues.length))
    .fixedBarHeight(barheight)
    .dimension(disciplineDimension)
    .group(fakeDisciplineGroup)
    .filterHandler(bagFilterHandler)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .elasticX(true)
    .colors(d3.scale.ordinal().range(deterministicShuffle(colorbrewer.Spectral[11],1)))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (disciplineFilter) {
    disciplineChart.filter(disciplineFilter);
  }
  disciplineChart.ordering(function(d){ return -d.value });

  technologyTagChart
    .width(chartwidth)
    .height(chartheight(Math.min(technologyTagValues.length,8)))
    .fixedBarHeight(barheight)
    .dimension(technologyTagDimension)
    .group(fakeTechnologyTagGroup)
    .filterHandler(bagFilterHandler)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .elasticX(true)
    .colors(d3.scale.ordinal().range(deterministicShuffle(colorbrewer.Set3[12],800)))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (technologyTagFilter) {
    technologyTagChart.filter(technologyTagFilter);
  }
  technologyTagChart.ordering(function(d){ return -d.value }).rowsCap(8).othersGrouper(false);

  statusChart
    .width(chartwidth)
    .height(chartheight(statusGroup.all().length))
    .fixedBarHeight(barheight)
    .dimension(statusDimension)
    .group(statusGroup)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .elasticX(true)
    .colors(d3.scale.ordinal().range(deterministicShuffle(colorbrewer.Set3[12],8)))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (statusFilter) {
    statusChart.filter(statusFilter);
  }
  statusChart.ordering(function(d){ return -d.value });
  /*
  supportLevelChart
    .width(chartwidth)
    .height(chartheight(supportLevelGroup.all().length))
    .fixedBarHeight(barheight)
    .dimension(supportLevelDimension)
    .group(supportLevelGroup)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .elasticX(true)
    .colors(d3.scale.ordinal().range(colorbrewer.Reds[3]))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (supportLevelFilter) {
    supportLevelChart.filter(supportLevelFilter);
  }
  supportLevelChart.ordering(function(d){ return -d.value });
  */
  licenseChart
    .width(chartwidth)
    .height(chartheight(licenseValues.length))
    .fixedBarHeight(barheight)
    .dimension(licenseDimension)
    .group(fakeLicenseGroup)
    .filterHandler(bagFilterHandler)
    .elasticX(true)
    .gap(1)
    .margins({top:0,bottom:-1,right:0,left:0})
    .colors(d3.scale.ordinal().range(deterministicShuffle(colorbrewer.Set3[12],2)))
    .xAxis().tickFormat(d3.format("d")).ticks(1);
  if (licenseFilter) {
    licenseChart.filter(licenseFilter);
  }
  licenseChart.ordering(function(d){ return -d.value });

  dataTable.width(800)
      .dimension(softwareDimension)
      .group(function(d) { return 1; })
    .size(100)
    .columns([
        function(d) {
            // site_url variable should be set before this line is executed.
            return '<a href="' + d['@id'].replace(site_url, '') + '">' + d.name + '</a>';
        },
        function(d) { return d.tagLine; }
    ])
    .sortBy(function(d){ return d.name.toLowerCase(); })
    // (optional) sort order, :default ascending
    .order(d3.ascending);


  dc.dataCount(".dc-data-count")
    .dimension(ndx)
    .group(all);


  dc.renderAll();
});
