# import datetime
# from carrents.models import Brand, Order 



# def check_availability(brand, booking, returnbooking):
#     avail_list=[]
#     booking_list= Order.objects.filter(brand=brand)
#     for book in booking_list:
#         if book.booking > returnbooking or book.returnbooking< booking:
#          avail_list.append(True)
#     else:
#         avail_list.append(False)

#     return all(avail_list) 
