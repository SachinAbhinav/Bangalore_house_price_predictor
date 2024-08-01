const button = document.getElementsByClassName("submitButton")[0]

button.addEventListener("click", (e) => {
    e.preventDefault()
    predictPrice()
})


function predictPrice(){
    console.log('Estimate Button Clicked');
    var sqft = document.getElementById('uiSqft');
    var bhk = document.getElementById('uibhk');
    var balcony = document.getElementById('uibalcony');
    var bath = document.getElementById('uibath');
    var locations = document.getElementById('uilocations');

    var url = 'http://127.0.0.1:5000/predict_price';
    $.post(url, {
        total_sqft : sqft.value,
        bhk : bhk.value,
        balcony : balcony.value,
        location : locations.value,
        bath : bath.value
    }, function(data, status){
        // console.log(data.predicted_price);
        var result = document.getElementsByClassName('result')[0]
        result.innerHTML = '<h3>' + data.predicted_price.toString() + '  Lakhs INR </h3>'
        console.log(data, status);
    });

}




function onPageLoad(){
    console.log('Page Loaded');
    var url = 'http://127.0.0.1:5000/get_locations';
    $.get(url, function(data, status){
        console.log('Got  response');
        console.log(data);
        if (data){
            var locations = data.locations;
            var uilocations = document.getElementById('uilocations');
            $('#uilocations').empty();
            for (var i in locations){
                var opt = new Option(locations[i]);
                $('#uilocations').append(opt);
            }
        }
    })

}

window.onload = onPageLoad;








