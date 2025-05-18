def main():
#take time as input from the input
#have them seperate as 12hr and 24hr the user should be able to take both as inputs.
#set the program in such a way that the user should get the out as their meal time during the decided hrs and nothing in the rest of the hours
    time = input("what time is it? ").strip()
    hours = convert(time)
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")
    else:
        print("")


def convert(times):
#take time in such a way that the input of 7:30 change into 7.5
    times = times.lower().strip()

    # Check for AM/PM and remove it if present
    if "am" in times or "pm" in times:
        is_pm = "pm" in times
        times = times.replace("am", "").replace("pm", "").strip()

        # Split hours and minutes
        hours, minutes = map(int, times.split(":"))

        # Convert to 24-hour format if PM
        if is_pm and hours != 12:
            hours += 12
        if not is_pm and hours == 12:
            hours = 0
    else:
        # Handle 24-hour format
        hours, minutes = map(int, times.split(":"))
    return hours + minutes/60


if __name__ == "__main__":
    main()