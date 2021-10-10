#Base serializers
from .baseSerializers import BaseProductSerializer, BaseProductListSerializer

from .baseSerializers import BaseIndepentSerializer,BaseIndepentListSerializer

#User serializers
from .userSerializer import UserSerializer, UserUpdateSerializer
from .employeeSerializer import EmployeeSerializer, EmployeeUpdateSerializer

#Business serializers
from .saleSerializer import SaleSerializer
from .reservationSerializer import ReservationSerializer
from .workAreaSerializer import WorkAreaSerializer

#Products serializers
from .productSerializers import ProductSerializer, ProductUpdateSerializer
from .productSerializers import BookSerializer, BookUpdateSerializer
from .productSerializers import MagazineSerializer, MagazineUpdateSerializer