import streamlit as st
from add import add
from subtract import subtract
from multiplly import multiply
from divide import divide

def main():
    st.title("Simple Calculator")

    # Input fields
    num1 = st.number_input("Enter the first number", format="%.2f")
    num2 = st.number_input("Enter the second number", format="%.2f")
    operator = st.selectbox("Choose an operator", options=["+", "-", "*", "/"])

    # Calculation based on selected operator
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            st.error(f"Error: {e}")
            result = None

    # Display result
    if result is not None:
        st.write(f"The result is: {result}")

    # Option to quit
    if st.button('Quit'):
        st.write("Goodbye!")
        st.stop()  # This stops the Streamlit app

if __name__ == "__main__":
    main()