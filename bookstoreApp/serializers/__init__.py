#Base serializers
from .baseSerializers import BaseProductSerializer, BaseProductListSerializer
from .baseSerializers import BaseIndepentSerializer,BaseIndepentListSerializer

#Staff serializers
from .staffSerializers import UserSerializer, UserUpdateSerializer
from .staffSerializers import EmployeeSerializer, EmployeeUpdateSerializer
from .staffSerializers import WorkAreaSerializer, WorkAreaUpdateSerializer

#Business serializers
from .businessSerializers import ShoppingCartSerializer, ShoppingCartUpdateSerializer
from .businessSerializers import ShoppingCart_ProductSerializer, ShoppingCart_ProductUpdateSerializer
from .businessSerializers import Invoice_ProductSerializer, Invoice_ProductUpdateSerializer
from .businessSerializers import InvoiceSerializer, InvoiceUpdateSerializer
# from .businessSerializers import
# from .businessSerializers import

#Products serializers
from .productSerializers import ProductSerializer, ProductUpdateSerializer
from .productSerializers import BookSerializer, BookUpdateSerializer
from .productSerializers import MagazineSerializer, MagazineUpdateSerializer

