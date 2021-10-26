#Base views
from .baseViews import BaseProductView
from .baseViews import BaseIndependentView

#staff views
from .staffViews import EmployeeView
from .staffViews import WorkAreaView


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
from .customerViews import CustomerDetailView

#analysis
from .analysisView import SalesPerYearView
from .analysisView import SalesPerMonthView