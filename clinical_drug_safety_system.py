# Initial State
patients = [
    {"Name": "Ali", "Conditions": ["Kidney Disease"], "Allergies": ["Penicillin"], "Current_Drugs": []},
    {"Name": "Sara", "Conditions": [], "Allergies": [], "Current_Drugs": []}
]

# Safety Rules Function
def is_safe(patient, drug):
    """Check if giving drug to patient is safe"""
    # Rule 1: Drug + Kidney Disease = Unsafe
    if drug == "DrugA" and "Kidney Disease" in patient["Conditions"]:
        return False, "Unsafe: DrugA not allowed for Kidney Disease"
    
    # Rule 2: Drug + Allergy = Unsafe
    if drug in patient["Allergies"]:
        return False, f"Unsafe: {drug} causes allergy for patient"
    
    return True, "Safe to administer"

# Function to give drug
def give_drug(patient_name, drug):
    # Find patient
    patient = next((p for p in patients if p["Name"] == patient_name), None)
    if not patient:
        print(f"Patient {patient_name} not found!")
        return
    
    safe, message = is_safe(patient, drug)
    if safe:
        patient["Current_Drugs"].append(drug)
        print(f"{drug} given to {patient_name}. ✅ {message}")
    else:
        print(f"Error! Cannot give {drug} to {patient_name}. ❌ {message}")

# Example Usage
give_drug("Ali", "DrugA")      # Should be unsafe due to kidney disease
give_drug("Ali", "Penicillin") # Should be unsafe due to allergy
give_drug("Sara", "DrugA")     # Safe
give_drug("Sara", "Penicillin")# Safe
