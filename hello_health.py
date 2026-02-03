import logging
import hashlib
import sys

# Configure logging
logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger.debug("Starting application")
logger.info("Patient must write their name")
logger.warning("If temperature is above 38°C, you have a fever")

"""
Greet the person when he/she/they arrives.
"""

print("Health App Setup Complete!")

"""
A variable called name with typehint String. It is declared by an input, 
of which the person write their name. 
"""
name:str = input ("Enter your first- and lastname: ")

"""
The person is greeted with:
Hello {their name}, welcome to your health tracker!
"""

"""
Generating ID which is the same everytime for the same name
"""

patient_id = hashlib.sha256(name.encode()).hexdigest()

print (f"Hello {name}, welcome to your health tracker!")

print (f"Your ID is {patient_id}...")

"""
Ask the patient if they want to continue.
The patient answer y/Y, the program continue.
The patient answer n/N, the program stops. 
"""
while True:
    proceed: str = input ("Do you want to continue using the health tracker? (y/n) ").lower()

    if proceed == "y":
        print("Continuing...")
        break

    elif proceed == "n":
        print("Thanks for using our DEMO! The program will no stop...")
        sys.exit()

    else:
        print("Please type y or n")

"""
Register the temperature of the patient as a variable temp,
then gives a logger.info/warning/critical if the patient has 
a fever or not. If the temperature of the patient is colder 
than 36, it also gives a warning.
"""

logger.info(f"Processing patient: {patient_id}")

try:
    temp = float(input("Enter temp: "))

    if temp > 39:
        logger.critical(f"Dangerously high: {temp}°C")
    elif temp > 38:
        logger.warning(f"Fever detected: {temp}°C")
    elif temp <= 36: 
        logger.warning(f"Colder than normal: {temp}°C")
    else:
        logger.info(f"Normal temp: {temp}°C")

except ValueError:
    logger.error("Invalid temperature input")


while True:
    proceed: str = input ("Do you want to continue using the health tracker? (y/n) ").lower()

    if proceed == "y":
        print("Sorry, but that was all we have until now... " \
        "Thanks for using our DEMO! " \
        "The program will now stop...")
        sys.exit()

    elif proceed == "n":
        print("Thanks for using our DEMO! The program will now stop...")
        sys.exit()

    else:
        print("Please type y or n")