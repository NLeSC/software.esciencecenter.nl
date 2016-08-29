function CollectionsFullTextSearcher() {
  var me = this;
  this.raw_data = {};
  this.indices = {};
  this.toplen = 3;
  this.collections = ['software', 'project', 'person', 'organization', 'report'];

  this.create_indices = function() {
    this.indices.software = lunr(function() {
      this.ref('@id');
      this.field('name', {boost: 10});
      this.field('tagLine', {boost: 8});
      this.field('description', {boost: 6});
      this.field('technologyTag');
    });
    this.indices.project = lunr(function() {
      this.ref('@id');
      this.field('name', {boost: 10});
      this.field('tagLine', {boost: 8});
      this.field('description', {boost: 6});
      this.field('infrastructure');
      this.field('website');
    });
    this.indices.person = lunr(function() {
      this.ref('@id');
      this.field('name', {boost: 10});
      this.field('description', {boost: 6});
    });
    this.indices.organization = lunr(function() {
      this.ref('@id');
      this.field('name', {boost: 10});
      this.field('description', {boost: 6});
      this.field('website');
    });
    this.indices.report = lunr(function() {
      this.ref('@id');
      this.field('title', {boost: 10});
      this.field('description', {boost: 6});
      this.field('link');
    });
  };

  this.fill_indices = function(data) {
    this.collections.forEach(function(collection) {
      data[collection].forEach(function(d) {
        me.indices[collection].add(d);
      });
    });
  };

  this.search = function(query) {
    var hits = this.collections.map(function(collection) {
        var results = me.indices[collection].search(query);
        return {
          collection: collection,
          count: results.length,
          top: results.slice(0, me.toplen)
        };
    });
    return hits;
  };

  this.search_render = function(query, results_div) {
    var hits = this.search(query);

    results_div.empty();

    hits.forEach(function(collection_hits) {
      var collection = collection_hits.collection;
      if (collection_hits.count > 0) {
        results_div.append('<a href="#query=' + query + '">' + collection_hits.count + '</a> hit(s) in ' + collection + ':<br/>');
        collection_hits.top.forEach(function(hit) {
          var item = me.get_collection_item(collection, hit.ref);
          var hit_name = '';
          if (collection === 'report') {
            hit_name = item.title;
          } else {
            hit_name = item.name;
          }
          results_div.append('<a href="' + hit.ref + '">'+ hit_name + '</a><br/>');
        });
      // } else {
      //   results_div.append('No hits in ' + collection + '<br/>');
      }
    });
  };

  this.get_collection_item = function(collection, item_id) {
    return this.raw_data[collection].find(function(d) {
      return d['@id'] === item_id;
    });
  };

  this.init = function() {
    this.create_indices();
    d3.json('/index.json', function(error, data) {
      if (error) {
        console.warn(error);
        return;
      }
      me.raw_data = data;
      me.fill_indices(data);
    });
  };
}

var collections_fulltext_searcher =  new CollectionsFullTextSearcher();
collections_fulltext_searcher.init();

$(document).ready(function() {
  var results_div = $('#search-results');
  var search_box = $('input#search-box');
  search_box.on('keyup', function() {
    var query = $(this).val();
    collections_fulltext_searcher.search_render(query, results_div).bind(collections_fulltext_searcher);
  });
  $('.search-panel-toggle').click(function() {
    $('.search-panel').toggle();
    $('#search-box').focus();
  });
});
