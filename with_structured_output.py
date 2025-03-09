from pydantic import BaseModel , Field
from typing import Optional 


class Insight(BaseModel):
    Customer_Account_Group : str = Field(description= "tell me if it is Sold-to Party (SP) or Ship-to Party (SH) or Bill-to Party (BP) or Payer (PY) of the customer ")
    Type_of_legal_entity : str = Field(description="tell me which organization or individual  has legal rights and responsibilities, such as entering contracts, owning assets, and being liable for debts")   
    Title : str= Field(description="what is the title name Mrs or Mr or M/S of the customer")
    Account_Name : str 
    #Name(AdditionalLine: str
    GSTN_legal_name_of_Business: str =Field(description="what is the legal name of the business")
    GSTN_Registration_trade_name : str = Field(description="tell me the registration name of the company")
    Sales_type : str =Field(description="tell me the sales type of the company")
    Transportation_Zone : str = Field(description="tell me the transportation zone of the company")
    Classification : str = Field(description="tell me the classification of the company on the basis of SBU")
    Rubix_report_id : int = Field(description="tell me the rubix report id of the company")
    Quality_Score_Percentage : float = Field(description="tell me the quality score percentage of the company")
    Distributor_product_list : list[str] = Field(description="tell me the distributor product list of the company only the names")
    DMS_Sales_invoice_headers : int = Field(description="tell me the invoice number")
    SAP_customer_number : int = Field(description="tell me the SAP customer number of the company")
    Check_list_count_All: int = Field(description="tell me the number if all the check list count of the company")
    Check_list_count_completed : int = Field(description="tell me the number of check list count of the company")
    Industry : str =Field(description="tell me to which industry the company belongs answer in one word.")
    SubIndustry :str = Field(description="tell me to which subindustry the company belongs answer in one word or one statement")
    ParentAccount :str = Field(description= "tell me the name of the parent account of the company.")
    CorporateGroup : str = Field(description="tell me to which corporate group or company belongs")
    CustomerSegment : str = Field(description="tell me the customer segment of the company")
    JSWCustomer : str = Field(description="tell me if the company is the previous customer of JSW yes or no.")
    