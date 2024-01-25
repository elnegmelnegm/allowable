import streamlit as st

# Constants for Mobile Phase A
MOBILE_PHASE_A_RELATIVE_LIMIT = 30.0
MOBILE_PHASE_A_ABSOLUTE_LIMIT = 10.0

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

        if phase == 'Mobile Phase A':
            relative_change = MOBILE_PHASE_A_RELATIVE_LIMIT
            absolute_change_limit = MOBILE_PHASE_A_ABSOLUTE_LIMIT
        else:
            st.sidebar.subheader(f"{phase} - Relative Change (%)")
            relative_change = st.sidebar.number_input(f"{phase} Relative Change (%)", min_value=0.0, max_value=100.0, step=1.0, value=0.0)

            st.sidebar.subheader(f"{phase} - Absolute Change Limit (%)")
            absolute_change_limit = st.sidebar.number_input(f"{phase} Absolute Change Limit (%)", min_value=0.0, max_value=100.0, step=1.0, value=10.0)

        # Perform calculations
        allowed_change = calculate_allowed_change(original_ratio, relative_change, absolute_change_limit)

        # Save result for later display
        allowed_changes[phase] = (original_ratio - allowed_change, original_ratio + allowed_change)

    # Display results
    st.subheader("Results")

    for phase, change_range in allowed_changes.items():
        lower_limit, upper_limit = change_range
        st.write(f"{phase} Allowed Change: From {lower_limit:.2f}% to {upper_limit:.2f}%")

if __name__ == "__main__":
    main()