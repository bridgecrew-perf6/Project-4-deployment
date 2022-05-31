const data_url = "https://raw.githubusercontent.com/thelearning1/test/main/by_country/";
const pred_url = 'https://raw.githubusercontent.com/thelearning1/test/main/by_country/pred/'
const country_json = 'https://raw.githubusercontent.com/thelearning1/test/main/countries.json'

// a function for counting occurrences of an object in an array
function countOccurrences (array) {
    let a = [],
      b = [],
      arr = [...array], // clone array so we don't change the original when using .sort()
      prev;
    arr.sort();
    for (let element of arr) {
      if (element !== prev) {
        a.push(element);
        b.push(1);
      }
      else ++b[b.length - 1];
      prev = element;
    }
    let occurness = {}
    for (let i = 0; i < a.length; i++) {
        occurness[a[i]] = parseInt(b[i])
      }
    return occurness;
}
//initialization function to populate page upon entry
function init() {
    var dropdownA = d3.select("#pick-country-A");
    var dropdownB = d3.select("#pick-country-B");
    var blah = [];
    d3.json(country_json).then((country)=> {
        // index through json to populate list of countries
        Object.values(country).forEach(x=> {
            blah.push(x[0].Country);
        });
        // sort the list alphabetically for usability
        blah.sort();
        // populate dropdown from list of countries
        blah.forEach(names =>
            dropdownA.append("option").text(names).property("value"));
        blah.forEach(names =>
            dropdownB.append("option").text(names).property("value"));
        
        traceA1 = 'undefined'
        traceA2 = 'undefined'
        traceA3 = 'undefined'
        traceB1 = 'undefined'
        traceB2 = 'undefined'
        traceB3 = 'undefined'
    });         
};

// function to generate the data charts
function countryAchanged(nat) {
    // define variables for the data needed
    let data_source = data_url+nat.replace(' ','%20')+'.json';
    let NOC = nat.split('~',[2])[1]
        d3.json(data_source).then((nat_data)=> {
            let attempts = nat_data[NOC];
            let yearly_medals = {};
            let yearly_competes = {};
            let yearly_gdp_perc = {};
            let yearly_rural_pop_perc = {};
            let yearly_life_expect = {};
            let yearly_global_pop_perc = {};
            let yearly_medal_victory_perc = {};
            let yearly_gdp = {};
            let yearly_pop = {};
            let yearly_gdpc = {};
            // fill variables from data
            for (i = 0; i < attempts.length; i++) {
                year = attempts[i].Year
                
                // values for the separate percentage based chart
                yearly_gdp_perc[year] = attempts[i]['Global_GDP%'];
                yearly_rural_pop_perc[year] = attempts[i]['Rural_Pop%'];
                yearly_life_expect[year] = attempts[i]['Life_Expect'];
                yearly_global_pop_perc[year] = attempts[i]['Global_Pop%'];
                
                // calculating yearly victory percentage
                yearly_competes[year] = (yearly_competes[year] || 0) + 1;
                if (attempts[i].Medal != "") {
                    yearly_medals[year] = (yearly_medals[year] || 0) + 1;}
                
                yearly_medal_victory_perc[year] = yearly_medals[year] / yearly_competes[year];
                
                // values for the merged flat-value chart
                yearly_pop[year] = attempts[i]['Nat_Pop']
                yearly_gdp[year] = attempts[i]['GDP']
                yearly_gdpc[year] = attempts[i].GDP_Per_Cap;        
            };
           
            // CHART MAKING CODE HERE

        // Separate chart Chart
            let traceperc1 = {
                x: Object.keys(yearly_gdp_perc),
                y: Object.values(yearly_gdp_perc),
                type: 'scatter',
                name: '% of Global GDP'
            };
            let traceperc2 = {
                x: Object.keys(yearly_rural_pop_perc),
                y: Object.values(yearly_rural_pop_perc),
                type: 'scatter',
                name: '% of Population is Rural'
            };
            let traceperc3 = {
                x: Object.keys(yearly_life_expect),
                y: Object.values(yearly_life_expect),
                type: 'scatter',
                name: 'Life Expectancy (years)'
            };
            let traceperc4 = {
                x: Object.keys(yearly_global_pop_perc),
                y: Object.values(yearly_global_pop_perc),
                type: 'scatter',
                name: '% of Global Population'
            };
            let traceperc5 = {
                x: Object.keys(yearly_medal_victory_perc),
                y: Object.values(yearly_medal_victory_perc),
                type: 'scatter',
                name: '% of Competitions Won'
            };
            let L_layout = {
                title: "Yearly Competitors vs. Yearly Medals Won",
                xaxis:{
                    title: 'Year',
                    range: [1956,2020]
                },
                yaxis:{
                    range: [0,100]
                }
            };
            let Ldata = [traceperc1,traceperc2,traceperc3,traceperc4,traceperc5]
            Plotly.newPlot('lineA',Ldata,L_layout)
            
        // Merged chart
            traceA1 = {
                x: Object.keys(yearly_pop),
                y: Object.values(yearly_pop),
                type: 'scatter',
                name: nat.split('~')[0]+'Population '
            };
            traceA2 = {
                x: Object.keys(yearly_gdp),
                y: Object.values(yearly_gdp),
                type: 'scatter',
                name: nat.split('~')[0]+'GDP'
            };
            traceA3 = {
                x: Object.keys(yearly_gdpc),
                y: Object.values(yearly_gdpc),
                type: 'scatter',
                name: nat.split('~')[0]+'GDP per Capita'
            };
            let B_layout = {
                title: 'Flat National Statistics'
            };

            if (traceB1 === 'undefined'){
                let data = [traceA1,traceA2,traceA3]
                Plotly.newPlot('line-flat',data,B_layout)
            }
            else {
                let data = [traceA1,traceA2,traceA3,traceB1,traceB2,traceB3]
                Plotly.newPlot('line-flat',data,B_layout)
            }
    });
}
// function to generate the data charts
function countryBchanged(nat) {
    // define variables for the data needed
    let data_source = data_url+nat.replace(' ','%20')+'.json';
    let NOC = nat.split('~',[2])[1]
        d3.json(data_source).then((nat_data)=> {
            let attempts = nat_data[NOC];
            let yearly_medals = {};
            let yearly_competes = {};
            let yearly_gdp_perc = {};
            let yearly_rural_pop_perc = {};
            let yearly_life_expect = {};
            let yearly_global_pop_perc = {};
            let yearly_medal_victory_perc = {};
            let yearly_gdp = {};
            let yearly_pop = {};
            let yearly_gdpc = {};
            // fill variables from data
            for (i = 0; i < attempts.length; i++) {
                year = attempts[i].Year
                
                // values for the separate percentage based chart
                yearly_gdp_perc[year] = attempts[i]['Global_GDP%'];
                yearly_rural_pop_perc[year] = attempts[i]['Rural_Pop%'];
                yearly_life_expect[year] = attempts[i]['Life_Expect'];
                yearly_global_pop_perc[year] = attempts[i]['Global_Pop%'];
                
                // calculating yearly victory percentage
                yearly_competes[year] = (yearly_competes[year] || 0) + 1;
                if (attempts[i].Medal != "") {
                    yearly_medals[year] = (yearly_medals[year] || 0) + 1;}
                
                yearly_medal_victory_perc[year] = yearly_medals[year] / yearly_competes[year];
                
                // values for the merged flat-value chart
                yearly_pop[year] = attempts[i]['Nat_Pop']
                yearly_gdp[year] = attempts[i]['GDP']
                yearly_gdpc[year] = attempts[i].GDP_Per_Cap;        
            };
           
            // CHART MAKING CODE HERE
            nat.split('~')[0]
        // Separate chart Chart
            let traceperc1 = {
                x: Object.keys(yearly_gdp_perc),
                y: Object.values(yearly_gdp_perc),
                type: 'scatter',
                name: '% of Global GDP'
            };
            let traceperc2 = {
                x: Object.keys(yearly_rural_pop_perc),
                y: Object.values(yearly_rural_pop_perc),
                type: 'scatter',
                name: '% of Population is Rural'
            };
            let traceperc3 = {
                x: Object.keys(yearly_life_expect),
                y: Object.values(yearly_life_expect),
                type: 'scatter',
                name: 'Life Expectancy (years)'
            };
            let traceperc4 = {
                x: Object.keys(yearly_global_pop_perc),
                y: Object.values(yearly_global_pop_perc),
                type: 'scatter',
                name: '% of Global Population'
            };
            let traceperc5 = {
                x: Object.keys(yearly_medal_victory_perc),
                y: Object.values(yearly_medal_victory_perc),
                type: 'scatter',
                name: '% of Competitions Won'
            };
            let L_layout = {
                title: "Yearly Competitors vs. Yearly Medals Won",
                xaxis:{
                    title: 'Year',
                    range: [1956,2020]
                },
                yaxis:{
                    range: [0,100]
                }
            };
            let Ldata = [traceperc1,traceperc2,traceperc3,traceperc4,traceperc5]
            Plotly.newPlot('lineB',Ldata,L_layout)
            
        // Merged chart
            traceB1 = {
                x: Object.keys(yearly_pop),
                y: Object.values(yearly_pop),
                type: 'scatter',
                name: nat.split('~')[0]+'Population'
            };
            traceB2 = {
                x: Object.keys(yearly_gdp),
                y: Object.values(yearly_gdp),
                type: 'scatter',
                name: nat.split('~')[0]+'GDP'
            };
            traceB3 = {
                x: Object.keys(yearly_gdpc),
                y: Object.values(yearly_gdpc),
                type: 'scatter',
                name: nat.split('~')[0]+'GDP per Capita'
            };
            let B_layout = {
                title: 'Flat National Statistics'
            };
            if (traceA1 === 'undefined'){
                let data = [traceB1,traceB2,traceB3]
                Plotly.newPlot('line-flat',data,B_layout)
            }
            else {
                let data = [traceA1,traceA2,traceA3,traceB1,traceB2,traceB3]
                Plotly.newPlot('line-flat',data,B_layout)
            };
            
    });
}


init();