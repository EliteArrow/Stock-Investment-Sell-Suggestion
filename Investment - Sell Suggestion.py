# Buying of Stock
buying_price = 993 
quantity = 188
buying_data = "1 jul 2021"
# Selling of Stock
selling_price = 1150
selling_data = "31 sep 2021"


annual_diposite_interest = 6
total_investment = quantity * buying_price



def Days(buying_data, selling_data):
    month_dict = {"jan" : 0,"feb" : 1,"mar" : 2,"apr" : 3,"may" : 4,"jun" : 5,"jul" : 6,"aug" : 7,"sep" : 8,"oct" : 9,"nov" : 10, "dec" : 11}
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    buying_data = buying_data.split(' ')
    selling_data = selling_data.split(' ')
    days = month_days[month_dict[buying_data[1]]] - int(buying_data[0])
    for x in range(month_dict[buying_data[1]]+1, month_dict[selling_data[1]]):
        days = days + month_days[x]
    days = days + int(selling_data[0])
    return days

def Diposite_Interest():
    Interest = (total_investment * (annual_diposite_interest/100)) * (Days(buying_data, selling_data)/365)
    return Interest


# Taxes and Statutory Charges
def Tax():
    Brokerage = 20 # Brokerage = 20Rs or 0.05%
    STT_charges = (total_investment * 0.001) # Securies Transaction Tax(STT) = 0.1%
    Stamp_Duty = (total_investment * 0.00015) # Stamp Duty = 0.015%
    Exchange_Charges = (total_investment * 0.0000345) # Exchange Transaction Charges = 0.00345%
    SEBI_Charges = (total_investment * 0.000001) # SEBI Turnover Charges = 0.0001%
    GST_charges = (Brokerage + Exchange_Charges) * 0.18 # 18% GST on DP charges, Exchange, Brokerage
    DP_Charges = 13.5 # DP charges = 13Rs per company per trading Day

    Tax = (2 * Brokerage) + (2 * STT_charges) + Stamp_Duty + (2 * Exchange_Charges) + (2 * SEBI_Charges) + (2 * GST_charges) + (2 * DP_Charges)
    return Tax

def sell_quantity():
    s_quantity = quantity - int(((quantity * (selling_price - buying_price)) - Diposite_Interest() + Tax())/selling_price)
    return s_quantity

# ============================= Final Outputs ===================================== #
print(" =======# ORDER DETAILS #======= ")
print("Buying Price :", buying_price)
print("Buying Date :", buying_data)
print("Selling Price :", selling_price)
print("Selling Date :", selling_data)
print("Invested :", total_investment)
print("RoI :", quantity * (selling_price - buying_price), "[", int(((selling_price-buying_price) * 100)/buying_price), "% ]")
print("Days :", Days(buying_data, selling_data))
print("Tax :", int(Tax()))
print("FD Interest :", int(Diposite_Interest()), "[", int((Days(buying_data, selling_data) * annual_diposite_interest)/ 365), "% ]")
print("--------------------------------------")
print("Suggested Quantities to Sell :", sell_quantity())
print("Release amount :", sell_quantity() * selling_price)
print("Profit on Exit : ", int(sell_quantity() * selling_price - total_investment - Tax()))
print("Still Invested :", (quantity - sell_quantity()) * selling_price)