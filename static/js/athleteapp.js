const data_url = "https://raw.githubusercontent.com/thelearning1/test/main/by_sport/";
const pred_url = 'https://raw.githubusercontent.com/thelearning1/test/main/by_sport/pred/'
const country_json = 'https://raw.githubusercontent.com/thelearning1/test/main/countries.json'
const sports_json = 'https://raw.githubusercontent.com/thelearning1/test/main/sportlist.json'

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
    let dropdown = d3.select("#NOC");
    let blah = [];
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
    let sportdown = d3.select('#selSport') 
    d3.json(sports_json).then((sdata)=> {
        // index through json to populate dropdown of sports
        sdata.Sport.forEach(names =>
            sportdown.append("option").text(names).property("value"))
    });        
};

function sportChanged(sport) {
    let data_source = data_url+sport+'.json';
    d3.json(data_source).then((sp_data)=> {
        compete = sp_data[sport]
        let heights = []
        let weights = []
        let ages = []
        let names = []
        let years = []
        // console.log(sport)
        // console.log(compete)
        compete.forEach(x => {
            heights.push(x.Height);
            weights.push(x.Weight);
            ages.push(x.Age);
            names.push(x.Name);
            years.push(x.Year)  
        });
    // Scatterplot for athletes height vs weight
        let traceA1 = {
            x: weights,
            y: heights,
            mode: 'markers',
            type: 'scatter',
        };
        let A_data = [traceA1];
        let A_layout = {
            xaxis:{range:[25,200],title:'Weight (kg)'},
            yaxis:{range:[50,225],title:'Height (cm)'},
            title: "Height vs. Weight of Athletes Competing In " + sport
        };
        Plotly.newPlot('scatterplot',A_data, A_layout);  
    // one-dimensional scatterplot showing athlete ages
        let traceA2 = {
            x: Object.keys(countOccurrences(ages)),
            y: Object.values(countOccurrences(ages)),
            mode: 'markers',  
        };
        let A_data2 = [traceA2];
        let A_layout2 = {title: 'Ages of Athletes Competing In ' + sport,
        xaxis:{title:'Age (years)',range:[0,75]},
        yaxis:{title:'Number of Competitors'}
        };
        Plotly.newPlot('ageplot',A_data2, A_layout2);
    });
};


// var approute = "https://pro4-oly.herokuapp.com/api/v1.0/athletes"

function getInputFromBoxes() {

    var Sex = document.getElementById("Sex").value;
    // console.log("Sex");

    var NOC = document.getElementById("NOC").value;
    // console.log("NOC");

    var Age = document.getElementById("Age").value;
    // console.log("Age");
    
    var Height = document.getElementById("Height").value;
    // console.log("Height");

    var Weight = document.getElementById("Weight").value;
    // console.log("Weight");

    var stuff =JSON.stringify({Sex, Age, Height, Weight, NOC})

    console.log(stuff)

    async function postData() {
        var response = await fetch('/predict', {method:'POST',
        headers: {'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'},
        body: JSON.stringify({Sex, Age, Height, Weight, NOC})
    })
        response = response.json();
        return response
        
    };
    let goodsporps = d3.select('#goodsporps')
    let badsporps = d3.select('#badsporps')
    goodsporps.html("")
    badsporps.html("")
    postData().then(value => goodsporps.append("h5").text("Best: "+value.Top[0]+";  2nd Best: "+value.Top[1]+";  3rd Best: "+value.Top[2]) 
                            (badsporps.append("h5").text("Worst: "+value.Bottom[0]+"\n;  2nd Worst: "+value.Bottom[1]+"\n;  3rd Worst: "+value.Bottom[2])));
     
};


init();