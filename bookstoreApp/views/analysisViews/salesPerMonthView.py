#Django
from django.http import Http404
from django.db.models.functions import ExtractYear

#Django rest framework
from rest_framework.response import Response
from rest_framework import views, status

#models
from bookstoreApp.models import Invoice_Product, Invoice

class SalesPerMonthView(views.APIView):
       
    #returns a json with the number of books and magazines sold per month
    def post(self,request):
        request_year= request.data['year']
        instances = Invoice.objects.annotate(year=ExtractYear('datetime')).filter(year = request_year )
        data_result = {
            "books": {},
            "magazines": {}
        }
        for instance in instances:
            month = instance.datetime.strftime('%m')
            
            for element in instance.invoice_product.all():          
                if element.product.type == "book":
                    if month not in data_result["books"].keys():
                        data_result["books"][month] = element.quantity
                    else :
                        data_result["books"][month] += element.quantity
                elif element.product.type == "magazine":
                    if month not in data_result["magazines"].keys():
                        data_result["magazines"][month] = element.quantity
                    else :
                        data_result["magazines"][month] += element.quantity
        
        return Response(data_result, status= status.HTTP_200_OK)
    

    
    