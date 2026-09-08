from src.app import induction_progress,purchase_order_status,payroll_control
def test_induction(): assert induction_progress("operator",[])["percent"]==0
def test_po_control(): assert purchase_order_status({"amount":6000,"quotation":"q.pdf"})=="FINANCE_APPROVAL"
def test_payroll_gap(): assert payroll_control([{"employee_id":"E1","approved":True}],["E1","E2"])["missing"]==["E2"]
