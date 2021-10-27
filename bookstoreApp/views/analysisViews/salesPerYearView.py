#Django
from django.http import Http404
from django.db.models.functions import ExtractYear

#Django rest framework
from rest_framework.response import Response
from rest_framework import views, status

#models
from bookstoreApp.models import Invoice_Product, Invoice

class SalesPerYearView(views.APIView):
       
    #returns a json with the number of books and magazines sold for all years
    def get(self,request):
        instances = Invoice_Product.objects.all()
        data_result = {
            "books": {},
            "magazines": {}
        }
        total = 0
        for instance in instances:
            year = instance.invoice.datetime.strftime('%Y')
            if instance.product.type == "book":
                if year not in data_result["books"].keys():
                    data_result["books"][year] = instance.quantity
                else :
                    data_result["books"][year] += instance.quantity
            elif instance.product.type == "magazine":
                if year not in data_result["magazines"].keys():
                    data_result["magazines"][year] = instance.quantity
                else :
                    data_result["magazines"][year] += instance.quantity
        for year in data_result['books'].keys():
            total = data_result["books"][year] + data_result["magazines"][year]
            data_result["books"][year] =  round( ( data_result["books"][year] / total )*100, 1)
            data_result["magazines"][year] =  round( ( data_result["magazines"][year] / total )*100, 1)
            
        return Response(data_result, status= status.HTTP_200_OK)
    
    #returns a json with the number of books and magazines sold in the requested year
    def post(self,request):
        request_year = request.data['year']
        instances = Invoice.objects.annotate(year=ExtractYear('datetime')).filter(year = request_year )
        data_result = {
            "books": 0,
            "magazines": 0
        }
        for instance in instances:
            
            for element in instance.invoice_product.all():
            
                if element.product.type == "book":
                    data_result["books"] += element.quantity
                            
                elif element.product.type == "magazine":
                    data_result["magazines"] += element.quantity
                    
        total = (data_result['books'] + data_result['magazines'])
        data_result['books'] =  round( ( data_result['books']/total )*100, 1 )
        data_result['magazines']=  round( ( data_result['magazines']/total )*100, 1 ) 
            
        return Response(data_result, status= status.HTTP_200_OK)
    