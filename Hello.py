# Importing necessary libraries
import streamlit as st

def multiply(input,number):
  return input ** number
  
# Define the main function for the app
def main():
    # Set the title of the app
    st.title("Simple Streamlit App")

    # Get user input for a number
    number = st.number_input("Enter a number:", min_value=0)

    # Display the square and cube of the input number
    square = multiply(number,2)
    cube = multiply(number,3)


    st.write(f"Square of {number}: {square}")
    st.write(f"Cube of {number}: {cube}")

# Run the app
if __name__ == "__main__":
    main()
