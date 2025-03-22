# Run this program with the command: python temperature_converter.py

class Temperature:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit.upper()
        self._validate_unit()
    
    def _validate_unit(self):
        valid_units = ['C', 'F', 'K']
        if self.unit not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of: {', '.join(valid_units)}")
    
    def to_celsius(self) -> float:
        if self.unit == 'C':
            return self.value
        elif self.unit == 'F':
            return (self.value - 32) * 5/9
        else:  # K
            return self.value - 273.15
    
    def to_fahrenheit(self) -> float:
        if self.unit == 'F':
            return self.value
        elif self.unit == 'C':
            return (self.value * 9/5) + 32
        else:  # K
            return (self.value - 273.15) * 9/5 + 32
    
    def to_kelvin(self) -> float:
        if self.unit == 'K':
            return self.value
        elif self.unit == 'C':
            return self.value + 273.15
        else:  # F
            return (self.value - 32) * 5/9 + 273.15
    
    def convert_to(self, target_unit: str) -> float:
        target_unit = target_unit.upper()
        if target_unit == 'C':
            return self.to_celsius()
        elif target_unit == 'F':
            return self.to_fahrenheit()
        elif target_unit == 'K':
            return self.to_kelvin()
        else:
            raise ValueError(f"Invalid target unit: {target_unit}")
    
    def __str__(self):
        return f"{self.value}°{self.unit}"

def display_menu():
    print("\nTemperature Converter")
    print("Available conversions:")
    print("c-f: Celsius to Fahrenheit")
    print("f-c: Fahrenheit to Celsius")
    print("k-f: Kelvin to Fahrenheit")
    print("f-k: Fahrenheit to Kelvin")
    print("\nOther options:")
    print("r: Restart program")
    print("q: Quit program")

def main():
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (e.g., 'c-f') or 'q' to quit: ").lower()
            
            if choice == 'q':
                print("Goodbye!")
                break
            elif choice == 'r':
                print("\nRestarting program...")
                continue
            
            if choice not in ['c-f', 'f-c', 'k-f', 'f-k']:
                print("Please enter a valid choice (c-f, f-c, k-f, f-k)")
                continue
            
            # Parse the choice to get source and target units
            source_unit, target_unit = choice.split('-')
            
            # Get temperature value
            temp_value = float(input("Enter the temperature: "))
            
            # Create Temperature object and convert
            temp = Temperature(temp_value, source_unit)
            result = temp.convert_to(target_unit)
            
            # Print result with appropriate formatting
            print(f"{temp} = {result:.2f}°{target_unit.upper()}")
            
            # Pause to show the result
            input("\nPress Enter to continue...")
                
        except ValueError as e:
            print(f"Error: {e}")
            input("\nPress Enter to continue...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main();