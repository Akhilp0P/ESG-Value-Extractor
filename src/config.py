import re

# METRIC_CONFIG defines the 'Anchors' used to find values in the text.
# Each key is the column name in the final CSV.
# Each value is a list of possible phrases that might appear in the report.
METRIC_CONFIG = {
    # --- Carbon Emissions ---
    "Total_CO2": ["total greenhouse gas emissions", "total ghg emissions", "total co2 emissions"],
    "Scope_1": ["scope 1 emissions", "scope 1 ghg", "scope 1 co2"],
    "Scope_2": ["scope 2 emissions", "scope 2 ghg", "scope 2 co2"],
    "Scope_3": ["scope 3 emissions", "scope 3 ghg", "scope 3 co2"],
    "Scope_3_Business_Travel": ["scope 3 business travel", "business travel emissions"],
    "Scope_3_Waste": ["scope 3 waste", "waste generated emissions"],
    "Scope_3_Employee_Commute": ["scope 3 employee commute", "commute emissions"],

    # --- Energy ---
    "Total_Energy": ["total energy consumption", "total energy usage", "total energy used"],
    "Energy_Electricity": ["electricity consumption", "purchased electricity", "grid electricity"],
    "Energy_Fuel": ["fuel consumption", "diesel usage", "petrol consumption"],
    "Energy_Renewable": ["renewable energy consumption", "solar energy", "wind energy", "green energy"],
    "Energy_Nuclear": ["nuclear energy consumption", "nuclear power usage"],
    "Energy_Biogas": ["biogas consumption", "biomass energy"],

    # --- Workforce ---
    "Total_Employees": ["total employees", "total workforce", "total headcount", "number of employees"],
    "Employees_Male": ["male employees", "total male", "percentage of male"],
    "Employees_Female": ["female employees", "total female", "percentage of female"],
    "TIR_Value": ["tir value", "total incident rate", "total recordable incident rate", "trir"],

    # --- Other ESG Keywords ---
    "Water_Consumption": ["total water consumption", "water withdrawal", "water usage"],
    "Waste_Generated": ["total waste generated", "total waste produced"],
    "Training_Hours": ["average training hours", "total training hours per employee"],
}

# Generic Regex for finding numbers: captures digits, commas, decimals, and optional units.
# Updated to explicitly avoid capturing percentages for emission metrics and prioritize weight units.
VALUE_REGEX = r"(\d{1,3}(?:,\d{3})*(?:\.\d+)?)\s*([a-zA-Z\s]+)?"

