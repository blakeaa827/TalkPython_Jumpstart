class Record:
    def __init__(self, street, city, zipcode, state, beds, baths, sq__ft, home_type,
                 sale_date, price, latitude, longitude, ):
        self.street = street
        self.city = city
        self.zip = zipcode
        self.state = state
        self.beds = int(beds)
        self.baths = int(baths)
        self.sq__ft = int(sq__ft)
        self.type = home_type
        self.sale_date = sale_date
        self.price = int(price)
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def create_record_from_dict(lookup):
        return Record(
            lookup['street'],
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude']),
        )
