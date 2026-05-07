from tkinter import *
import pickle

def format_value(value):
    if value>= 10000000:
        return f"{value/10000000:.2f} Cr"
    elif value>= 100000:
        return f"{value/100000:.2f} Lakhs"
    else:
        return str(value)


# Load the trained model
with open('./saved_models/RandomForestRegressor.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the scaler used during model training
with open('./saved_scaling/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Global variables to hold rodio btn values
seller_selected_value = ""
fuel_selected_value = ""
transmission_selected_value = ""

def pred_price():
    try:
        input_values = []

        # Numeric Inputs
        input_values.append(int(vehicle_age_entry.get()))
        input_values.append(int(km_driven_entry.get()))
        input_values.append(float(mileage_entry.get()))
        input_values.append(int(engine_entry.get()))
        input_values.append(float(max_power_entry.get()))
        
        seat_val = int(seats_entry.get())
        if seat_val <= 7:
            input_values.append(seat_val)
        else:
            print("Invalid seat number")
            return

        # Seller Type Encoding (3 categories)
        if seller_selected_value == "Dealer":
            input_values.extend([1, 0, 0])
        elif seller_selected_value == "Individual":
            input_values.extend([0, 1, 0])
        else:  # Trustmark Dealer
            input_values.extend([0, 0, 1])

        # Fuel Type Encoding (5 categories)
        fuel_dict = {"CNG": [1, 0, 0, 0, 0], "Diesel": [0, 1, 0, 0, 0],
                     "Electric": [0, 0, 1, 0, 0], "LPG": [0, 0, 0, 1, 0],
                     "Petrol": [0, 0, 0, 0, 1]}
        input_values.extend(fuel_dict.get(fuel_selected_value, [0, 0, 0, 0, 0]))

        # Transmission Encoding (2 categories)
        if transmission_selected_value == "Automatic":
            input_values.extend([1, 0])
        else:  # Manual
            input_values.extend([0, 1])

        # Check final input size
        if len(input_values) == 16:
            input_scaled = scaler.transform([input_values])
            prediction = model.predict(input_scaled)[0]
            prediction = format_value(prediction)
            print(input_values)
            price_label.config(text=f"Predicted Price: ₹ {prediction}")
            print(f"Predicted price: {prediction}")
        else:
            print("Missing or incorrect values")
    except Exception as e:
        print(f"Error: {e}")

# GUI Setup
root = Tk()
root.geometry("1080x720")
root.title("Car Price Predictor")
root.config(bg="black")

title_label = Label(root, text="Car Price Predictor", bg="black", fg="green", font=("Arial", 30, "bold"))
title_label.pack(pady=30)

def create_labeled_entry(parent, label_text, padx=30):
    frame = Frame(parent, bg="black")
    frame.pack()
    label = Label(frame, text=label_text, bg="black", fg="white", font=("Arial", 20, "bold"))
    label.pack(side=LEFT, padx=padx)
    entry = Entry(frame, font=("Arial", 15, "bold"), bd=5, relief=RAISED)
    entry.pack(side=LEFT)
    return entry

# Entry Widgets
car_name_entry = create_labeled_entry(root, "Car Name", 30)
vehicle_age_entry = create_labeled_entry(root, "Vehicle Age", 19)
km_driven_entry = create_labeled_entry(root, "KM Driven", 30)
mileage_entry = create_labeled_entry(root, "Mileage", 50)
engine_entry = create_labeled_entry(root, "Engine", 50)
max_power_entry = create_labeled_entry(root, "Max Power", 30)
seats_entry = create_labeled_entry(root, "Seats", 60)

# Radio Buttons: Seller Type
seller_type_frame = Frame(root, bg="black")
seller_type_frame.pack()
Label(seller_type_frame, text="Seller Type", bg="black", fg="white", font=("Arial", 20, "bold")).pack(side=LEFT, padx=60)

seller_type_values = {"Dealer": "Dealer", "Individual": "Individual", "Trustmark Dealer": "Trustmark Dealer"}
selected_seller = StringVar(root, value="Dealer")

def on_seller_selected():
    global seller_selected_value
    seller_selected_value = selected_seller.get()
    print(f"Seller: {seller_selected_value}")

for (text, value) in seller_type_values.items():
    Radiobutton(seller_type_frame, text=text, variable=selected_seller, value=value,
                font=("Arial", 10, "bold"), command=on_seller_selected).pack(side=LEFT, ipady=5)

# Radio Buttons: Fuel Type
fuel_type_frame = Frame(root, bg="black")
fuel_type_frame.pack()
Label(fuel_type_frame, text="Fuel Type", bg="black", fg="white", font=("Arial", 20, "bold")).pack(side=LEFT, padx=80)

fuel_type_values = {"CNG": "CNG", "Diesel": "Diesel", "Electric": "Electric", "LPG": "LPG", "Petrol": "Petrol"}
selected_fuel = StringVar(root, value="Petrol")

def on_fuel_selected():
    global fuel_selected_value
    fuel_selected_value = selected_fuel.get()
    print(f"Fuel: {fuel_selected_value}")

for (text, value) in fuel_type_values.items():
    Radiobutton(fuel_type_frame, text=text, variable=selected_fuel, value=value,
                font=("Arial", 10, "bold"), command=on_fuel_selected).pack(side=LEFT, ipady=5)

# Radio Buttons: Transmission Type
transmission_frame = Frame(root, bg="black")
transmission_frame.pack()
Label(transmission_frame, text="Transmission Type", bg="black", fg="white", font=("Arial", 20, "bold")).pack(side=LEFT, padx=10)

transmission_type_values = {"Automatic": "Automatic", "Manual": "Manual"}
selected_transmission = StringVar(root, value="Manual")

def on_transmission_selected():
    global transmission_selected_value
    transmission_selected_value = selected_transmission.get()
    print(f"Transmission: {transmission_selected_value}")

for (text, value) in transmission_type_values.items():
    Radiobutton(transmission_frame, text=text, variable=selected_transmission, value=value,
                font=("Arial", 10, "bold"), command=on_transmission_selected).pack(side=LEFT, ipady=5)

# Predict Button
pred_btn = Button(root, text="Predict Price", command=pred_price,
                  bg="green", fg="white", font=("Arial", 20, "bold"))
pred_btn.pack(pady=30)

# Price Output Label
price_label = Label(root, text="Predicted Price: ₹ 0", bg="black", fg="white", font=("Arial", 20, "bold"))
price_label.pack()

# Start with default values selected
on_seller_selected()
on_fuel_selected()
on_transmission_selected()

root.mainloop()
