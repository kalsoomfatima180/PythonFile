
# EVENT MANAGEMENT SYSTEM
# PIPE AND FILTER ARCHITECTURE
events = []

current_data = None

# 1. INPUT FILTER

def input_filter():

    print("\n===== INPUT FILTER =====")

    name = input("Enter customer name: ")
    event = input("Enter event type: ")
    date = input("Enter event date: ")

    guests = int(input("Enter number of guests: "))

    # Venue Options
   
    print("\n----- VENUE OPTIONS ")
    print("1. Royal Hall")
    print("2. Paradise Hall")
    print("3. Garden Hall")

    venue_choice = input("Choose venue: ")

    if venue_choice == "1":
        venue = "Royal Hall"

    elif venue_choice == "2":
        venue = "Paradise Hall"

    elif venue_choice == "3":
        venue = "Garden Hall"

    else:
        venue = "Invalid"

    # Menu Options

    print("\n----- MENU OPTIONS -----")
    print("1. Basic")
    print("2. Standard")
    print("3. Premium")

    menu_choice = input("Choose menu: ")

    if menu_choice == "1":
        menu = "Basic"

    elif menu_choice == "2":
        menu = "Standard"

    elif menu_choice == "3":
        menu = "Premium"

    else:
        menu = "Invalid"

    # Music Options

    print("\n----- MUSIC OPTIONS -----")
    print("1. DJ")
    print("2. Live Music")
    print("3. No Music")

    music_choice = input("Choose music: ")

    if music_choice == "1":
        music = "DJ"

    elif music_choice == "2":
        music = "Live Music"

    elif music_choice == "3":
        music = "No Music"

    else:
        music = "Invalid"

    # Create Event Data

    data = {
        "name": name,
        "event": event,
        "date": date,
        "guests": guests,
        "venue": venue,
        "menu": menu,
        "music": music
    }


    print("\nInput Filter Completed!")
    print("Data is ready for Validation Filter.")

    # Filter output
    return data

# 2. VALIDATION FILTER

def validation_filter(data):

    print("\n===== VALIDATION FILTER =====")

    if data is None:
        print("No data available.")
        return None

    # Check customer name
    if data["name"] == "":
        print("Name cannot be empty.")
        return None

    # Check event type
    if data["event"] == "":
        print("Event type cannot be empty.")
        return None

    # Check date
    if data["date"] == "":
        print("Date cannot be empty.")
        return None

    # Check guests
    if data["guests"] <= 0:
        print("Guests must be greater than 0.")
        return None

    # Check venue
    if data["venue"] == "Invalid":
        print("Invalid venue selected.")
        return None

    # Check menu
    if data["menu"] == "Invalid":
        print("Invalid menu selected.")
        return None

    # Check music
    if data["music"] == "Invalid":
        print("Invalid music selected.")
        return None

    print("All data is valid!")
    print("Data is ready for Cost Filter.")

    # Filter output
    return data

# 3. COST FILTER

def cost_filter(data):

    print("\n===== COST FILTER =====")

    if data is None:
        print("No valid data available.")
        return None

    # Guest Cost

    guest_cost = data["guests"] * 1000

    # Venue Cost

    if data["venue"] == "Royal Hall":
        venue_cost = 50000

    elif data["venue"] == "Paradise Hall":
        venue_cost = 40000

    else:
        venue_cost = 30000

    # Menu Cost
    
    if data["menu"] == "Basic":
        menu_cost = 10000

    elif data["menu"] == "Standard":
        menu_cost = 20000

    else:
        menu_cost = 30000

    # Music Cost
    if data["music"] == "DJ":
        music_cost = 15000

    elif data["music"] == "Live Music":
        music_cost = 25000

    else:
        music_cost = 0

    # Total Cost

    total_cost = (
        guest_cost
        + venue_cost
        + menu_cost
        + music_cost
    )

    data["total_cost"] = total_cost


    print("\nGuest Cost :", guest_cost)
    print("Venue Cost :", venue_cost)
    print("Menu Cost  :", menu_cost)
    print("Music Cost :", music_cost)
    print("------------------------")
    print("Total Cost :", total_cost)

    print("\nCost Filter Completed!")
    print("Data is ready for Booking Filter.")

    # Filter output
    return data

# 4. BOOKING FILTER

def booking_filter(data):

    print("\n===== BOOKING FILTER =====")

    if data is None:
        print("No valid data available.")
        return None


    if "total_cost" not in data:
        print("Please run Cost Filter first.")
        return None

    # Confirm booking
    data["status"] = "Confirmed"

    # Save booking
    events.append(data.copy())

    print("\nBooking Confirmed!")
    print("Customer :", data["name"])
    print("Status   :", data["status"])

    print("\nBooking Filter Completed!")
    print("Data is ready for Output Filter.")

    # Filter output
    return data

# 5. OUTPUT FILTER

def output_filter(data):

    print("\n===== OUTPUT FILTER =====")

    if data is None:
        print("No data available.")
        return None

    print("         EVENT DETAILS")

    print("Customer Name :", data["name"])
    print("Event Type    :", data["event"])
    print("Date          :", data["date"])
    print("Guests        :", data["guests"])
    print("Venue         :", data["venue"])
    print("Menu          :", data["menu"])
    print("Music         :", data["music"])

    if "total_cost" in data:
        print("Total Cost    :", data["total_cost"])

    if "status" in data:
        print("Status        :", data["status"])

    print("================================")

    # Final output
    return data

# COMPLETE PIPELINE

def run_pipeline():

    global current_data

    print(" RUNNING PIPELINE")
    

    # FILTER 1

    current_data = input_filter()

    # PIPE 1
    

    current_data = validation_filter(current_data)


    if current_data is None:
        print("\nPipeline stopped.")
        print("Data is invalid.")

        return


    # PIPE 2

    current_data = cost_filter(current_data)


    if current_data is None:
        print("\nPipeline stopped.")
        return

    # PIPE 3
    

    current_data = booking_filter(current_data)


    if current_data is None:
        print("\nPipeline stopped.")
        return
    
    # PIPE 4
    

    current_data = output_filter(current_data)

    print(" PIPELINE COMPLETED")
    

# VIEW ALL BOOKINGS
def view_events():

    print("\n===== ALL BOOKINGS =====")


    if len(events) == 0:
        print("No bookings available.")
        return


    for i, event in enumerate(events):

        print("\nBooking Number:", i + 1)

        print("Customer :", event["name"])
        print("Event    :", event["event"])
        print("Date     :", event["date"])
        print("Guests   :", event["guests"])
        print("Venue    :", event["venue"])
        print("Menu     :", event["menu"])
        print("Music    :", event["music"])
        print("Total    :", event["total_cost"])
        print("Status   :", event["status"])

        print("------------------------")
# MAIN MENU

while True:

    print("\n========================================")
    print("       EVENT MANAGEMENT SYSTEM")
    print("          PIPE AND FILTER")
    print("========================================")

    print("1. Input Filter")
    print("2. Validation Filter")
    print("3. Cost Filter")
    print("4. Booking Filter")
    print("5. Output Filter")
    print("6. Run Complete Pipeline")
    print("7. View All Bookings")
    print("8. Exit")


    choice = input("\nEnter your choice: ")


    if choice == "1":

        current_data = input_filter()

    elif choice == "2":

        current_data = validation_filter(current_data)

    
    elif choice == "3":

        current_data = cost_filter(current_data)

    elif choice == "4":

        current_data = booking_filter(current_data)


    elif choice == "5":

        current_data = output_filter(current_data)

    elif choice == "6":

        run_pipeline()

    elif choice == "7":

        view_events()

    elif choice == "8":

        print("\nProgram ended.")
        break

    else:

        print("\nInvalid choice!")