// console.log(`this is temp ${likelihood_sum}`);

jsonString_intensity = intensity_frontend.replace(/'/g, '"');
// Add quotes around the keys
jsonString_intensity = jsonString_intensity.replace(/(\d+)(:)/g, '"$1"$2');
var dictionary_intensity = JSON.parse(jsonString_intensity);
var jsonArray_intensity = [];

for (var key in dictionary_intensity) {
  if (dictionary_intensity.hasOwnProperty(key)) {
    jsonArray_intensity.push({
      key: key,
      value: parseInt(dictionary_intensity[key]),
    });
  }
}
// console.log(jsonArray_intensity);
jsonString_likelihood = likelihood_frontend.replace(/'/g, '"');
jsonString_likelihood = jsonString_likelihood.replace(/(\d+)(:)/g, '"$1"$2');
var dictionary_likelihood = JSON.parse(jsonString_likelihood);
var jsonArray_likelihood = [];

for (var key in dictionary_likelihood) {
  if (dictionary_likelihood.hasOwnProperty(key)) {
    jsonArray_likelihood.push({
      key: key,
      value: parseInt(dictionary_likelihood[key]),
    });
  }
}
// console.log(jsonArray_likelihood);

jsonString_relevance = relevance_frontend.replace(/'/g, '"');
jsonString_relevance = jsonString_relevance.replace(/(\d+)(:)/g, '"$1"$2');
var dictionary_relevance = JSON.parse(jsonString_relevance);
var jsonArray_relevance = [];

for (var key in dictionary_relevance) {
  if (dictionary_relevance.hasOwnProperty(key)) {
    jsonArray_relevance.push({
      key: key,
      value: parseInt(dictionary_relevance[key]),
    });
  }
}
// console.log(jsonArray_relevance);

jsonString_start_year = start_year_frontend.replace(/'/g, '"');
jsonString_start_year = jsonString_start_year.replace(/(\d+)(:)/g, '"$1"$2');
var dictionary_start_year = JSON.parse(jsonString_start_year);
var jsonArray_start_year = [];

for (var key in dictionary_start_year) {
  if (dictionary_start_year.hasOwnProperty(key) & (key != 0)) {
    jsonArray_start_year.push({
      key: key,
      value: parseInt(dictionary_start_year[key]),
    });
  }
}
// console.log("start_year");
// console.log(jsonArray_start_year);

jsonString_country = country_frontend.replace(/'/g, '"');
jsonString_country = jsonString_country.replace(/(\d+)(:)/g, '"$1"$2');
const decodedString = new DOMParser().parseFromString(jsonString_country, "text/html").body
  .textContent;
jsonString_country = decodedString.replace(/'/g, '"');
jsonString_country = jsonString_country.replace(/(\d+)(:)/g, '"$1"$2');
var dictionary_country = JSON.parse(jsonString_country);
// console.log(dictionary_country);
var jsonArray_country = [];
for (var key in dictionary_country) {
  if (dictionary_country.hasOwnProperty(key) & (key != 0)) {
    jsonArray_country.push({
      key: key,
      value: parseInt(dictionary_country[key]),
    });
  }
}
console.log("country");
console.log(jsonArray_country);

// pie chart start for likelihood
// Set up the pie layout
const pie = d3
  .pie()
  .value((d) => d.value)
  .sort(null);

// Set up arc generator with rounded corners on outer radius
const arc = d3.arc().innerRadius(100).outerRadius(150).cornerRadius(7);

// Set up color scale
const color = d3.scaleOrdinal(d3.schemeCategory10);

// Select the SVG container
const svg = d3.select("#chart");

// Set up the group element for the pie chart
const chart = svg.append("g").attr("transform", "translate(200,200)");

// Generate the pie slices
const arcs = chart
  .selectAll(".arc")
  .data(pie(jsonArray_likelihood))
  .enter()
  .append("g")
  .attr("class", "arc")
  .style("cursor", "pointer")
  .on("mouseover", handleMouseOver)
  .on("mouseout", handleMouseOut)
  .on("click", function (event, d) {
    formvariable.value = d.data.key;
    formvariable_type.value = "likelihood";
    form.submit();
  });
// Draw the pie slices
arcs
  .append("path")
  .attr("d", arc)
  .style("stroke", "#5eff00cc")
  .style("stroke-width", 2)
  .attr("fill", (d, i) => color(i));

arcs

  .append("text")
  .attr("transform", (d) => `translate(${arc.centroid(d)})`)
  .attr("text-anchor", "middle")
  .text(function (d) {
    if (d.data.value / intensity_sum > 0.04) return d.data.key;
    else return "";
  })
  .style("fill", "#ffffff")
  .style("font-size", 20);
const innerContent = arcs.append("g").attr("class", "inner-content");

innerContent
  .append("text")
  .attr("text-anchor", "middle")
  .attr("dy", "0.35em")
  .text("Likelihood")
  .style("font-size", "20px")
  .style("fill", "#fff");

// Mouseover event handler
function handleMouseOver(event, d) {
  d3.select(this).select("path").transition().duration(200).attr("transform", `scale(1.05)`);

  const tooltip = d3.select(".tooltip");
  var scrollOffsetX = window.pageXOffset || document.documentElement.scrollLeft;
  var scrollOffsetY = window.pageYOffset || document.documentElement.scrollTop;
  tooltip
    .html("likelihood : " + d.data.key + "<br>number of articles : " + d.data.value)
    .style("left", event.pageX - scrollOffsetX + "px")
    .style("top", event.pageY - scrollOffsetY + "px")
    .style("opacity", 1);
}

// Mouseout event handler
function handleMouseOut(event, d) {
  d3.select(this).select("path").transition().duration(200).attr("transform", "");

  d3.select(".tooltip").style("opacity", 0);
}

// bar graph intensity script
// var bar_data = [30, 86, 168, 281, 303, 365];

const svg_bar = d3.select(".bar_chart");
// Append y axis to SVG

svg_bar
  .selectAll("div")
  .data(jsonArray_intensity)
  .enter()
  .append("div")
  .style("width", "14px")
  .style("height", function (d) {
    return Math.min((d.value / intensity_sum) * 100, 23) + "rem";
  })
  .on("mouseover", handleMouseOver_bar)
  .on("mouseout", handleMouseout_bar)
  .on("click", function (event, d) {
    formvariable.value = d.key;
    formvariable_type.value = "intensity";
    form.submit();
  })
  .text(function (d) {
    return d.key;
  });

function handleMouseOver_bar(event, d) {
  const tooltip = d3.select(".tooltip");
  d3.select(this).style("cursor", "pointer");
  var scrollOffsetX = window.pageXOffset || document.documentElement.scrollLeft;
  var scrollOffsetY = window.pageYOffset || document.documentElement.scrollTop;
  tooltip
    .html("number of articles : " + d.value)
    .style("left", event.pageX - scrollOffsetX + "px")
    .style("top", event.pageY - scrollOffsetY + "px")
    .style("opacity", 1);
}
// Mouseout event handler
function handleMouseout_bar(event, d) {
  d3.select(".tooltip").style("z-index", 100).style("opacity", 0);
}

// Select the SVG container
const svg_rel = d3.select("#chart_rel");

// Set up the group element for the pie chart
const chart_rel = svg_rel.append("g").attr("transform", "translate(200,200)");

// Generate the pie slices
const arcs_rel = chart_rel
  .selectAll(".arc")
  .data(pie(jsonArray_relevance))
  .enter()
  .append("g")
  .attr("class", "arc")
  .style("cursor", "pointer")
  .on("mouseover", handleMouseOver_rel)
  .on("mouseout", handleMouseOut_rel)
  .on("click", function (event, d) {
    formvariable.value = d.data.key;
    formvariable_type.value = "relevance";
    form.submit();
  });
// Draw the pie slices
arcs_rel
  .append("path")
  .attr("d", arc)
  .style("stroke", "#5eff00cc")
  .style("stroke-width", 2)
  .attr("fill", (d, i) => color(i));

arcs_rel

  .append("text")
  .attr("transform", (d) => `translate(${arc.centroid(d)})`)
  .attr("text-anchor", "middle")
  .text(function (d) {
    if (d.data.value / intensity_sum > 0.04) return d.data.key;
    else return "";
  })
  .style("fill", "#ffffff")
  .style("font-size", 20);
const innerContent_rel = arcs_rel.append("g").attr("class", "inner-content");

innerContent_rel
  .append("text")
  .attr("text-anchor", "middle")
  .attr("dy", "0.35em")
  .text("relevance")
  .style("font-size", "20px")
  .style("fill", "#fff");
// Mouseover event handler
function handleMouseOver_rel(event, d) {
  d3.select(this).select("path").transition().duration(200).attr("transform", `scale(1.05)`);

  const tooltip = d3.select(".tooltip");
  var scrollOffsetX = window.pageXOffset || document.documentElement.scrollLeft;
  var scrollOffsetY = window.pageYOffset || document.documentElement.scrollTop;
  tooltip
    .html("relevance : " + d.data.key + "<br>number of articles : " + d.data.value)
    .style("left", event.pageX - scrollOffsetX + "px")
    .style("top", event.pageY - scrollOffsetY + "px")
    .style("opacity", 1);
}

// Mouseout event handler
function handleMouseOut_rel(event, d) {
  d3.select(this).select("path").transition().duration(200).attr("transform", "");

  d3.select(".tooltip").style("opacity", 0);
}

// bar graph intensity script
// var bar_data = [30, 86, 168, 281, 303, 365];

const svg_bar_year = d3.select(".bar_chart_year");
// Append y axis to SVG

svg_bar_year
  .selectAll("div")
  .data(jsonArray_start_year)
  .enter()
  .append("div")
  .style("width", "14px")
  .style("height", function (d) {
    return Math.min((d.value / start_year_sum) * 100, 23) + "rem";
  })
  .on("mouseover", handleMouseOver_bar_year)
  .on("mouseout", handleMouseout_bar_year)
  .on("click", function (event, d) {
    formvariable.value = d.key;
    formvariable_type.value = "start_year";
    form.submit();
  })
  .text(function (d) {
    return d.key;
  });

function handleMouseOver_bar_year(event, d) {
  const tooltip = d3.select(".tooltip");
  d3.select(this).style("cursor", "pointer");
  var scrollOffsetX = window.pageXOffset || document.documentElement.scrollLeft;
  var scrollOffsetY = window.pageYOffset || document.documentElement.scrollTop;
  tooltip
    .html("number of articles : " + d.value)
    .style("left", event.pageX - scrollOffsetX + "px")
    .style("top", event.pageY - scrollOffsetY + "px")
    .style("opacity", 1);
}
// Mouseout event handler
function handleMouseout_bar_year(event, d) {
  d3.select(".tooltip").style("z-index", 100).style("opacity", 0);
}

// bar graph intensity script
// var bar_data = [30, 86, 168, 281, 303, 365];

const svg_bar_country = d3.select(".bar_chart_country");
// Append y axis to SVG

svg_bar_country
  .selectAll("div")
  .data(jsonArray_country)
  .enter()
  .append("div")
  .style("width", "14px")
  .style("height", function (d) {
    return Math.min((d.value / country_sum) * 100, 23) + "rem";
  })
  .on("mouseover", handleMouseOver_bar_country)
  .on("mouseout", handleMouseout_bar_country)
  .on("click", function (event, d) {
    formvariable.value = d.key;
    formvariable_type.value = "country";
    form.submit();
  })
  .text(function (d) {
    return d.key;
  });

function handleMouseOver_bar_country(event, d) {
  const tooltip = d3.select(".tooltip");
  d3.select(this).style("cursor", "pointer");
  var scrollOffsetX = window.pageXOffset || document.documentElement.scrollLeft;
  var scrollOffsetY = window.pageYOffset || document.documentElement.scrollTop;
  tooltip
    .html("country : " + d.key + " <br>number of articles : " + d.value)
    .style("left", event.pageX - scrollOffsetX + "px")
    .style("top", event.pageY - scrollOffsetY + "px")
    .style("opacity", 1);
}
// Mouseout event handler
function handleMouseout_bar_country(event, d) {
  d3.select(".tooltip").style("z-index", 100).style("opacity", 0);
}
