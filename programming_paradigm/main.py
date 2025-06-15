import sys
from robust_division_calculator import safe_divide

def main():
    # Verify correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)
    
    # Get arguments and compute result
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    result = safe_divide(numerator, denominator)
    
    # Print the result or error message
    print(result)

if __name__ == "__main__":
    main()
