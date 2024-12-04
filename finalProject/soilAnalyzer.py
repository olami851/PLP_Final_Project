# # Thia program will analyze the soil pH, tells the condition of the soil with possible recommendation,
# #  and also suggest the type of suitable crop to be planted on the soil based on the analysis.

def analyze_soil_ph(pH):

    # Analyzes the soil pH and recommends suitable crops or actions.

    # Args:
    #     pH (float): Soil pH value.

    # Returns:
    #     str: Recommendation based on pH.
   
    if 6.0 <= pH <= 7.5:
        return "The soil is neutral. Suitable for crops like: Wheat, Rice, Corn."

    elif 5.5 <= pH < 6.0:
        return "The soil is slightly acidic. Suitable for crops like: Potato, Tomato, Carrot."

    elif 7.5 < pH <= 8.5:
        return "The soil is slightly alkaline. Suitable for crops like: Beans, Cabbage, Broccoli."

    elif pH < 5.5:
        return "The soil is highly acidic. Consider adding lime to neutralize the soil pH."

    elif pH > 8.5:
        return "The soil is highly alkaline. Consider adding sulfur or organic matter to reduce the acidic content of the soil."

    else:
        return "Invalid pH value. Please enter a pH between 0 and 14."

def main():
    print("Welcome to the Soil Quality Analyzer!")
    
    try:
        # Get user input for soil pH value
        pH_value = float(input("Enter the soil pH value (0-14): "))
        
        # Get soil analysis result
        result = analyze_soil_ph(pH_value)
        
        # Display the result
        print(f"\nAnalysis Result: {result}")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value for the pH.")

# Run the program
if __name__ == "__main__":
    main()

