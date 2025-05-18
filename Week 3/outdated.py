def get_date():
    # Map month names to their respective numbers
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    while True:
        try:
            date = input("Date: ").strip()

            # Handle MM/DD/YYYY format
            if "/" in date:
                mm, dd, yyyy = map(int, date.split("/"))
            # Handle "Month Day, Year" format
            elif "," in date:
                month_str, day_year = date.split(" ", 1)
                dd, yyyy = day_year.split(", ")
                dd = int(dd)
                yyyy = int(yyyy)
                mm = months[month_str]
            else:
                continue

            # Check if the input date is valid
            if not (1 <= dd <= 31 and 1 <= mm <= 12):
                raise ValueError

            # Format the day and month as two digits
            dd_str = f"{dd:02}"
            mm_str = f"{mm:02}"
            yyyy_str = f"{yyyy:04}"

            # Create the ISO 8601 formatted date string
            formatted_date = f"{yyyy_str}-{mm_str}-{dd_str}"
            print(f"{formatted_date}")
            break
        except (ValueError, EOFError):
            pass

def main():
    get_date()

if __name__ == "__main__":
    main()
