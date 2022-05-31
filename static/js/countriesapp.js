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
    var dropdown = d3.select("#selDataset");
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
            dropdown.append("option").text(names).property("value")
        );
    });         
};

// function to generate the data charts
function gimmePastandPlot(nat) {
    // define variables for the data needed
    let data_source = data_url+nat.replace(' ','%20')+'.json';
    let NOC = nat.split('~',[2])[1]
        d3.json(data_source).then((nat_data)=> {
            let attempts = nat_data[NOC];
            let bronze = 0;
            let silver = 0;
            let gold = 0;
            let sports = [];
            let sport_medals = [];
            let nat_stats = {"GDP":"No Data", "Rural_Pop%":"No Data","Nat_Pop":"No Data","Year":0};
            let yearly_medals = {};
            let yearly_competes = {};
            let yearly_gdpc = {};
            // fill variables from data
            for (i = 0; i < attempts.length; i++) {
                year = attempts[i].Year
                yearly_gdpc[year] = attempts[i].GDP_Per_Cap;
                yearly_competes[year] = (yearly_competes[year] || 0) + 1;
                if (attempts[i].Medal != "") {
                    yearly_medals[year] = (yearly_medals[year] || 0) + 1;}
                if (year > nat_stats.Year) {
                    nat_stats.GDP = attempts[i].GDP;
                    nat_stats["Rural_Pop%"] = attempts[i]["Rural_Pop%"];
                    nat_stats.Nat_Pop = attempts[i].Nat_Pop;
                    nat_stats.Year = year;}
                sports.push(attempts[i].Sport)
                if (attempts[i].Medal == 'Bronze') {
                    bronze++; sport_medals.push(attempts[i].Sport);}
                else if (attempts[i].Medal == 'Silver') {
                    silver++;sport_medals.push(attempts[i].Sport);}
                else if (attempts[i].Medal == 'Gold') {
                    gold++; sport_medals.push(attempts[i].Sport)};    
            };
            // extrapolated stats
            tot_medals = bronze + silver + gold;
                console.log("Total Medals: "+tot_medals)
            tot_competitions = attempts.length;
                console.log("Total competes: "+tot_competitions)
            ratio = tot_medals/tot_competitions
                console.log("Medal Ratio: "+ratio)
            // DIV SELECTION VARIABLES
            let stats = d3.select("#national-stats"); // info panel
            let history = d3.select("#medal-history");

            // EMPTY PANELS
            stats.html("");
            history.html("");
            //PANEL FILLING CODE
            Object.entries(nat_stats).forEach((key)=> {
                stats.append("h5").text(key[0] + ": " + key[1] + "\n")
            });
            if (tot_medals == 0) {
                history.append("h5").text("Victory Ratio: %" + "0"+"       Total Medals: "+tot_medals)
            } else {
                history.append("h5").text("Victory Ratio: %" + ratio.toFixed(4)+"       Total Medals: "+tot_medals)
            };


            // CHART MAKING CODE HERE

        // Line Chart
            let traceL2 = {
                x: Object.keys(yearly_medals),
                y: Object.values(yearly_medals),
                type: 'scatter',
                name: 'Medals Won'
            };
            let traceL1 = {
                x: Object.keys(yearly_competes),
                y: Object.values(yearly_competes),
                type: 'scatter',
                name: 'Competes'
            };
            let L_layout = {
                title: "Yearly Competitors vs. Yearly Medals Won",
            };
            let Ldata = [traceL1,traceL2]
            Plotly.newPlot('line',Ldata,L_layout)
            
        // Bar Chart
            let traceB1 = {
                x: Object.keys(countOccurrences(sports)),
                y: Object.values(countOccurrences(sports)),
                type: 'bar',
                name: 'Competes'
            };
            let traceB2 = {
                x: Object.keys(countOccurrences(sport_medals)),
                y: Object.values(countOccurrences(sport_medals)),
                type: 'bar',
                name: 'Medals Won'
            };
            let B_layout = {
                title: 'Sports Competed in vs. Medals Won'
            };
            let Bdata = [traceB1,traceB2]

            Plotly.newPlot('bar',Bdata,B_layout)
        // Stacked Bar
            let traceM1 = {
                x: [bronze],
                y: [''],
                type: 'bar',
                name: 'Bronze',
                orientation: 'h',
                marker:{
                    color: 'rgb(176,141,87)',
                    width: .5
                }
            };
            let traceM2 = {
                x: [silver],
                y: [''],
                type: 'bar',
                name: 'Silver',
                orientation: 'h',
                marker:{
                    color: 'rgb(181,181,189)',
                    width: .5
                }
            };
            let traceM3 = {
                x: [gold],
                y: [''],
                type: 'bar',
                name: 'Gold',
                orientation: 'h',
                marker:{
                    color: 'rgb(231,189,66)',
                    width: .5
                }
            };
            let M_layout = {
                title: 'Medals Won',
                barmode: 'stack',
                height: 100,
                showlegend: false,
                margin: {
                    l: 10,
                    r: 0,
                    b: 15,
                    t: 24,
                    pad: 0
                  }
            };
            let Mdata = [traceM1,traceM2,traceM3];

            Plotly.newPlot('medals',Mdata,M_layout);
            
            // log verification
            // console.log(yearly_medals)
            // console.log(nat_stats)
            // console.log(bronze,'Bronze',silver,'Silver',gold,'Gold')
            // console.log(countOccurrences(sports))
            // console.log(countOccurrences(sport_medals))  
        });
};

// function to populate prediction data
function gimmePreds(nat) {
    let data_source = pred_url+nat.replace(' ','%20')+'.json';
    let NOC = nat.split('~',[2])[1]
    d3.json(data_source).then((nat_data)=> {
        let sports = (nat_data[NOC])[0]    
        //console.log(sports)
        let sorted = Object.fromEntries(
            Object.entries(sports).sort(([,a],[,b]) => b-a)
        );
        console.log(Object.entries(sorted));
        // console.log(sports.Archery)
        let predictions = d3.select("#predicted-medals")
        predictions.html("")
        for (i = 1; i < 6; i++) {
            Object.entries(sorted)[i]
            console.log(Object.entries(sorted)[i])
            predictions.append("h5").text(Object.entries(sorted)[i][0] + ": " + Object.entries(sorted)[i][1] + "\n")};
            
        });
};

function optionChanged(nat) {
    gimmePreds(nat)
    gimmePastandPlot(nat)
};

init();