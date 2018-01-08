

      var map;
      var prev_infowindow=false;

 function ViewModel() {
    var self = this;

    this.listOfLocations = ko.observableArray([]);
    this.searchTerm = ko.observable('');

    map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: 47.673988, lng: -122.121513},
            zoom: 13
    });

    //Making the list of Locations
    locations.forEach(function(locationItem){
        self.listOfLocations.push( new Location(locationItem));
    });

    //Searching for the Search Term from the list if search term is entered
    this.placesList= ko.computed( function() {
        var searchFilter = self.searchTerm().toLowerCase();
        if (searchFilter)
         {
            return ko.utils.arrayFilter(self.listOfLocations(), function(locationItem) {
                var str = locationItem.title.toLowerCase();
                var result = (str.search(searchFilter) >-1);
                   locationItem.visible(result);
                            return result;
                        });
        }
        //return all the locations in the listOfLocations if the search Term was not entered
        else
        {
            self.listOfLocations().forEach(function(locationItem){
                locationItem.visible(true);
            });
            return self.listOfLocations();
        }
    }, self);

    this.mapElement = document.getElementById('map');

}

      var Location=function(data){

        var self=this;

        this.title=data.title;
        this.lat=data.lat;
        this.long=data.long;
        this.URL="";
        this.street="";
        this.city="";

        this.visible=ko.observable(true);

        var fourSquare= 'https://api.foursquare.com/v2/venues/search?ll='+ this.lat + ',' + this.long + '&client_id=' + "FQI4040Q04AVLDY0XFNTW0S1BXD0BZBAQHS5LF4JLEQONFDX" + '&client_secret=' + "TJDXXWH0XLHBLUTENXRQNCQJ4HYHAPLRVE2XRQJUNAV0UZ55" + '&v=20171209' + '&query=' + this.title;

        $.getJSON(fourSquare).done(function(data) {

        if(typeof data.response.venues[0].url==='undefined')
        {
            self.URL="";
        }
        else
        {
            self.URL = data.response.venues[0].url;
          }
        self.street = data.response.venues[0].location.formattedAddress[0];
        self.city = data.response.venues[0].location.formattedAddress[1];

    }).fail(function() {
        alert('Error in importing data from FourSquare');
    });

self.infoWindow = new google.maps.InfoWindow();

         this.marker = new google.maps.Marker({
            position: new google.maps.LatLng(data.lat, data.long),
            title: this.title,
            map: map
        });

         this.markerVisible = ko.computed(function() {
            if(this.visible() != true)
            {
            this.marker.setMap(null);

            }
            else
            {
            this.marker.setMap(map);
            }
            return true;
    }, this);

         this.marker.addListener('click', function(){

        self.contentString = '<div class="info-window-content"><div class="title"><b>' + data.title + "</b></div>" +
        '<div class="content"><a href="' + self.URL +'">' + self.URL + "</a></div>" +
        '<div class="content">' + self.street + "</div>" +
        '<div class="content">' + self.city + "</div></div>" ;


        self.infoWindow.setContent(self.contentString);
        if(prev_infowindow)
            prev_infowindow.close();
        prev_infowindow=self.infoWindow;
        self.infoWindow.open(map, this);
        self.marker.setAnimation(google.maps.Animation.BOUNCE);
        setTimeout(function() {
            self.marker.setAnimation(null);
        }, 1500);
    });

    this.displayLocation = function() {

        google.maps.event.trigger(self.marker, 'click');
    };
};


function main() {
    ko.applyBindings(new ViewModel());
}


