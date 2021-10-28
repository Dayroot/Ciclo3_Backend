#Base views
from .baseViews import BaseProductView
from .baseViews import BaseIndependentView

#user views
from .userViews import UserUpdateView
from .userViews import UserDetailView

#staff views
from .staffViews import EmployeeView
from .staffViews import WorkAreaView
from .staffViews import StaffTokenObtainPairView
from .staffViews import CustomerManagementView


#business views
from .businessViews import ShoppingCartView
from .businessViews import ShoppingCart_ProductView
from .businessViews import InvoiceView
from .businessViews import Invoice_ProductView

#product views
from .productViews import MagazineView
from .productViews import BookView

#customer views
from .customerViews import CustomerRegistrationView
from .customerViews import CustomerTokenObtainPairView
from .customerViews import CustomerDeleteAccountView

#analysis
from .analysisViews import SalesPerYearView
from .analysisViews import SalesPerMonthView
