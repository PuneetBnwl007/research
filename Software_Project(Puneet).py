# Define a class named HelpDeskTicket to represent a help desk ticket
class HelpDeskTicket:
    # Class-level variables to keep track of ticket counts and store all ticket objects
    ticket_counter = 0
    open_tickets = 0
    resolved_tickets = 0
    all_tickets = []

    # Constructor method to initialize a help desk ticket object
    def __init__(self, user_name, employee_id, email, issue):
        # Increment the ticket counter and open ticket count
        HelpDeskTicket.ticket_counter += 1
        HelpDeskTicket.open_tickets += 1
        # Assign a unique ticket number to the ticket based on the ticket counter
        self.ticket_number = HelpDeskTicket.ticket_counter + 2000
        self.user_name = user_name
        self.employee_id = employee_id
        self.email = email
        self.issue = issue
        self.response = "Not Yet Provided"  # Default response for the ticket
        self.status = "Open"  # Default status for the ticket
        # Add the ticket object to the list of all tickets
        HelpDeskTicket.all_tickets.append(self)

    # Method to provide a solution to the ticket and change its status to "Closed"
    def provide_solution(self, response):
        self.response = response
        self.status = "Closed"
        # Decrease open ticket count and increase resolved ticket count
        HelpDeskTicket.open_tickets -= 1
        HelpDeskTicket.resolved_tickets += 1

    # Method to reopen a closed ticket and change its status to "Reopened"
    def reopen(self):
        self.response = "Not Yet Provided"
        self.status = "Reopened"
        # Increase open ticket count and decrease resolved ticket count
        HelpDeskTicket.open_tickets += 1
        HelpDeskTicket.resolved_tickets -= 1

    # Method to resolve a password reset request and generate a new password
    def resolve_password_reset(self):
        if "Password reset" in self.issue:
            # Generate a new password based on user's ID and name
            new_password = self.employee_id[:2] + self.user_name[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            # Decrease open ticket count and increase resolved ticket count
            HelpDeskTicket.open_tickets -= 1
            HelpDeskTicket.resolved_tickets += 1

    # Method to display the ticket information
    def display(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"User Name: {self.user_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Email: {self.email}")
        print(f"Issue: {self.issue}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}\n")

    # Class method to display ticket statistics
    @classmethod
    def statistics(cls):
        print("\nTicket Statistics\n")
        print(f"Total Tickets: {cls.ticket_counter}")
        print(f"Resolved Tickets: {cls.resolved_tickets}")
        print(f"Open Tickets: {cls.open_tickets}\n")

    # Class method to print information for all ticket objects
    @classmethod
    def print_all_tickets(cls):
        print("\nAll Tickets\n")
        for ticket in cls.all_tickets:
            ticket.display()

# Main function to create and manipulate help desk tickets
def main():
    # Create a list of help desk ticket objects
    tickets = [
        HelpDeskTicket("Ali", "ALI123", "ali@example.com", "Network connectivity issue"),
        HelpDeskTicket("Bobby", "BOB456", "bobby@example.com", "Software installation problem"),
        HelpDeskTicket("Charlie", "CHA789", "charlie@example.com", "Password reset needed"),
        HelpDeskTicket("Daman", "DAM012", "daman@example.com", "Printer not responding"),
        HelpDeskTicket("Everton", "EVE345", "everton@example.com", "Email not sending")
    ]
    
    # Display initial ticket statistics
    HelpDeskTicket.statistics()
    HelpDeskTicket.print_all_tickets()
    
    # Resolve password reset requests for some tickets
    for ticket in tickets:
        ticket.resolve_password_reset()
    
    # Provide a solution for a specific ticket and display updated statistics
    tickets[1].provide_solution("Software successfully installed.")
    HelpDeskTicket.statistics()
    
    # Display ticket information for all tickets
    for ticket in tickets:
        ticket.display()
    
    # Display updated ticket statistics for all tickets 
    HelpDeskTicket.statistics()
    
    # Reopen a specific ticket and display the specific one
    tickets[1].reopen()
    tickets[1].display()

    # Display ticket statistics for all tickets 
    HelpDeskTicket.statistics()

# Entry point for the program
if __name__ == "__main__":
    main()
