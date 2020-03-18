class Hotel:
    add_hotel = []
    add_room = []
    rooms = []
    
    """----Hotel class----"""
    def __init__(self):
        pass
        #self.hotel_id = hotel_id
        #self.hotel_name = hotel_name
        

    @classmethod
    def addHotel(cls, h_id, h_name, no_room):
        cls.add_hotel.append({
            "hotel_id": h_id,
            "hotel_name": h_name,
            "no_of_room": no_room
        })

    @classmethod
    def getHotels(cls):
        return Hotel.add_hotel

    @classmethod
    def prompt_input(cls):
        while True:
            print("----ADD HOTEL----")
            query = input("Do you want to add Hotel? press Y or N.")
            if query[0].lower() == 'y':
                h_id = input("Enter hotel ID: ")
                h_name = input("Enter Hotel name: ")
                no_room = input("Enter no. of room: ")
                Hotel.addHotel(h_id, h_name, no_room)
            else:
                break

        
class Room(Hotel):
    """----Room class----"""
    def __init__(self, *args, **kwargs):
        super(Room, self).__init__(*args, **kwargs)
    
    @classmethod
    def addRooms(cls,hotel_name,rooms):
        cls.rooms.append({
            hotel_name: rooms
        })
    
    def getRooms(self):
        price = input("Enter budget: ") 
        check_room = []
        for room_obj in self.addRoomToHotel():
            for k, v in room_obj.items():
                for list_value in v:
                    if list_value['price'] <= price:
                        print(list_value)
                        return check_room.append(list_value)


    
    def addRoomToHotel(self):
        hotels = self.getHotels()
        for hotel in hotels:
            count = 0
            while int(hotel['no_of_room']) > 0:
                print("ADD ROOM TO: {}".format(hotel['hotel_name']))
                query = input("Do you want to add Room? press Y or N.")
                
                if query[0].lower() == 'y':
                    amenities = input("Enter amenities: ")
                    price = input("Enter price: ") 
                    count = count + 1                   
                    Hotel.add_room.append({
                        "amenities": amenities,
                        "price": price
                    }) 
                    print(count)
                elif query[0].lower() == 'n':
                    if count < 5:
                        print("EACH ROOM have min 5 amenities")
                    else:
                        break
                hotel['no_of_room'] = int(hotel['no_of_room']) - 1

            Hotel.rooms.append({
                hotel['hotel_name']: Hotel.add_room
            })
        return Hotel.rooms           



def main():
    Hotel.prompt_input()
    obj = Room()
    #obj.addRoomToHotel()
    print(obj.getRooms())

if __name__ == '__main__':
    main()