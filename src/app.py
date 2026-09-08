from datetime import date

REQUIRED={"operator":["welcome_email","ppe","locker","site_tour","system_access","iso_train"],"technician":["welcome_email","ppe","locker","site_tour","system_access","iso_train","lab_access"]}
def induction_progress(role, completed):
    required=REQUIRED[role]; missing=[x for x in required if x not in completed]
    return {"completed":len(required)-len(missing),"total":len(required),"percent":round(100*(len(required)-len(missing))/len(required)),"missing":missing}
def purchase_order_status(request):
    if not request.get("quotation"): return "WAITING_FOR_QUOTATION"
    if request["amount"]>=5000 and not request.get("finance_approval"): return "FINANCE_APPROVAL"
    return "READY_FOR_PO"
def payroll_control(timesheets, expected_people):
    submitted={x["employee_id"] for x in timesheets if x.get("approved")}
    return {"ready":len(submitted)==len(expected_people),"missing":sorted(set(expected_people)-submitted),"checked_on":date.today().isoformat()}
