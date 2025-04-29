# Industrial-Grade ERP System for Manufacturing Company
# Modules:
# Authentication & Authorization (Users, Roles, Permissions)

# Employee Management -------------

# Employee onboarding, transfers, and leaves

# Attendance tracking

# Salary generation

# Inventory Management -------------

# Raw material stock

# Finished goods stock

# Warehouse transfers

# Stock auditing

# Procurement Management --------------

# Vendor registration

# Purchase requisitions

# Purchase orders

# Invoice management

# Production Planning and Control ----------

# BOM (Bill of Materials) Management

# Work Orders

# Machine scheduling

# Resource allocation

# Quality Control -----------------

# Incoming material inspection

# In-process quality checks

# Final product testing

# Sales and Distribution -------------

# Customer registration

# Sales order management

# Shipment and delivery tracking

# Finance and Accounting --------------------

# Accounts receivable and payable

# Bank transactions

# Budgeting

# Reporting & Analytics --------------

# Daily production reports

# Stock status reports

# Sales and revenue reports

# Notification & Alerts ------------------

# Email, SMS, or App notifications for approvals, rejections, stock alerts, etc.


# Fields for Raw Material Purchase


# purchase_order_id	UUID / Auto ID	Unique ID of the purchase order
# supplier_id	Foreign Key	Link to the supplier/vendor
# warehouse_id	Foreign Key	Warehouse where raw materials will be received
# order_date	Date	Date when the PO was created
# expected_delivery_date	Date	When the supplier is expected to deliver
# payment_terms	Text	Payment agreement (e.g., 30 days credit)
# item_id	Foreign Key	Raw material item to be purchased
# item_description	Text	Description of the raw material
# quantity_ordered	Decimal	Quantity to order (in UOM like kg, liters)
# unit_of_measure	String	Unit (e.g., Kg, Liters, Pieces)
# rate_per_unit	Decimal	Price per unit of the raw material
# total_amount	Decimal	quantity_ordered × rate_per_unit
# taxes	Decimal	Applicable taxes (optional)
# discount	Decimal	Discount on order (optional)
# grand_total	Decimal	Final total after taxes and discounts
# order_status	Enum (Draft / Submitted / Completed / Cancelled)	Status of the PO
# created_by	User ID	User who created the PO
# approved_by	User ID	(If needed) Approver of the PO
# received_quantity	Decimal	Quantity actually received (for partial delivery)
# remarks	Text	Any additional notes



# warehouses Table — Fields & Structure

# Field Name	Type	Description
# id	UUID / Auto ID	Unique identifier for each warehouse
# name	String	Name of the warehouse (e.g., "Main Warehouse", "Raw Material Store")
# code	String	Short code/alias (e.g., WH-01, RM-WH)
# location	Text	Full address or location description
# type	Enum	Type of warehouse: raw_material, finished_goods, general, quarantine
# capacity	Decimal / Float	Max storage capacity (optional)
# unit_of_capacity	String	Unit (e.g., kg, cubic meters)
# is_active	Boolean	Whether the warehouse is active/in use
# created_at	Timestamp	When the warehouse was created
# updated_at	Timestamp	When the warehouse details were last updated
# created_by	Foreign Key (User)	User who created the warehouse record


# vendors Table — Fields & Structure

# Field Name	Type	Description
# id	UUID / Auto ID	Unique identifier for each vendor
# name	String	Name of the vendor (e.g., "Bhutan Trading Co.")
# code	String	Short code/alias (e.g., VEND-01, SUP-123)
# vendor_type	Enum	Type of vendor: raw_material, service, logistics, etc.
# contact_person	String	Name of the person to contact at the vendor
# phone	String	Contact phone number
# email	String	Contact email address
# address	Text	Full address of the vendor
# gst_number	String	Tax registration number (optional)
# is_active	Boolean	Whether the vendor is currently active/in use
# created_at	Timestamp	When the vendor was added to the system
# updated_at	Timestamp	When the vendor information was last updated
# created_by	Foreign Key (User)	User who created the vendor record