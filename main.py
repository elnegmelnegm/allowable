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

    # Input for Mobile Phase A
    st.sidebar.subheader(f"{mobile_phases[0]} - Original Ratio (%)")
    original_ratio_a = st.sidebar.number_input(f"{mobile_phases[0]} Original Ratio (%)", min_value=0.0, max_value=100.0, step=1.0, value=50.0)

    relative_change_a = MOBILE_PHASE_A_RELATIVE_LIMIT
    absolute_change_limit_a = MOBILE_PHASE_A_ABSOLUTE_LIMIT

    # Input for Mobile Phase B
    st.sidebar.subheader(f"{mobile_phases[1]} - Original Ratio (%)")
    original_ratio_b = st.sidebar.number_input(f"{mobile_phases[1]} Original Ratio (%)", min_value=0.0, max_value=100.0, step=1.0, value=30.0)

    # Calculate allowed change for Mobile Phase B
    allowed_change_b = calculate_allowed_change(original_ratio_b, relative_change_a, absolute_change_limit_a)

    # Input for Mobile Phase C
    st.sidebar.subheader(f"{mobile_phases[2]} - Original Ratio (%)")
    original_ratio_c = 100 - original_ratio_a - original_ratio_b  # Ensure the sum is 100%

    # Calculate allowed change for Mobile Phase C
    allowed_change_c = calculate_allowed_change(original_ratio_c, relative_change_a, absolute_change_limit_a)

    # Perform calculations
    allowed_changes[mobile_phases[0]] = (original_ratio_a - calculate_allowed_change(original_ratio_a, relative_change_a, absolute_change_limit_a), original_ratio_a + calculate_allowed_change(original_ratio_a, relative_change_a, absolute_change_limit_a))
    allowed_changes[mobile_phases[1]] = (original_ratio_b - allowed_change_b, original_ratio_b + allowed_change_b)
    allowed_changes[mobile_phases[2]] = (original_ratio_c - allowed_change_c, original_ratio_c + allowed_change_c)

    # Display results
    st.subheader("Results")

    for phase, change_range in allowed_changes.items():
        lower_limit, upper_limit = change_range
        st.write(f"{phase} Allowed Change: From {lower_limit:.2f}% to {upper_limit:.2f}%")

if __name__ == "__main__":
    main()
