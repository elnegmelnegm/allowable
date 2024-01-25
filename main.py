import streamlit as st

def calculate_adjustment(value, percent, absolute):
    # Calculate the allowable adjustment
    adjustment = max(value * percent, absolute)
    return adjustment

def main():
    st.title("Allowable Adjustments to European Pharmacopeia (EP) Methods")

    st.sidebar.header("Input Parameters")

    # Example input fields, you can customize based on your needs
    mobile_phase_ratio = st.sidebar.number_input("Mobile Phase Ratio (%)", min_value=0.0, max_value=100.0, step=1.0, value=50.0)
    mobile_phase_absolute_change = st.sidebar.number_input("Mobile Phase Absolute Change (%)", min_value=0.0, max_value=100.0, step=1.0, value=10.0)

    # Perform calculations
    adjusted_ratio = calculate_adjustment(mobile_phase_ratio, 0.3, mobile_phase_absolute_change)

    # Display results
    st.subheader("Results")
    st.write(f"Original Mobile Phase Ratio: {mobile_phase_ratio}%")
    st.write(f"Allowable Adjusted Mobile Phase Ratio: {adjusted_ratio}%")

if __name__ == "__main__":
    main()

