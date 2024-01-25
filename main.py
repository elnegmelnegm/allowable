import streamlit as st

def calculate_allowed_change(original_ratio, relative_change, absolute_change_limit):
    # Calculate the allowable adjustment
    relative_adjustment = original_ratio * relative_change
    allowed_change = min(relative_adjustment, absolute_change_limit)
    return allowed_change

def main():
    st.title("Allowable Adjustments to European Pharmacopeia (EP) Methods")

    st.sidebar.header("Input Parameters")

    mobile_phases = ['Mobile Phase A', 'Mobile Phase B', 'Mobile Phase C']

    allowed_changes = {}

    for phase in mobile_phases:
        st.sidebar.subheader(f"{phase} - Original Ratio (%)")
        original_ratio = st.sidebar.number_input(f"{phase} Original Ratio (%)", min_value=0.0, max_value=100.0, step=1.0, value=50.0)

        st.sidebar.subheader(f"{phase} - Relative Change (%)")
        relative_change = st.sidebar.number_input(f"{phase} Relative Change (%)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)

        st.sidebar.subheader(f"{phase} - Absolute Change Limit (%)")
        absolute_change_limit = st.sidebar.number_input(f"{phase} Absolute Change Limit (%)", min_value=0.0, max_value=100.0, step=1.0, value=10.0)

        # Perform calculations
        allowed_change = calculate_allowed_change(original_ratio, relative_change, absolute_change_limit)

        # Save result for later display
        allowed_changes[phase] = allowed_change

    # Display results
    st.subheader("Results")

    for phase, change in allowed_changes.items():
        st.write(f"{phase} Allowed Change: {change:.2f}%")

if __name__ == "__main__":
    main()
