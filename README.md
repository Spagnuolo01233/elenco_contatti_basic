# Elenco_contatti Python Script

## Introduction

The "Elenco_contatti" Python script provides a simple implementation for managing a list of contacts. It includes classes for creating and managing contacts within an "Elenco_contatti" instance.

# Functionality
The script defines two classes: Contatto and Elenco_contatti.
Contatto class represents a contact with attributes: nome (name), telefono (phone number), and mail (email address).
Elenco_contatti class manages a list of contacts, providing methods to add, display, and delete contacts.

# Adding a Contact
To add a contact, create an instance of the Contatto class and then use the aggiungi_contatto method of the Elenco_contatti class to add it to the list of contacts.

# Example of adding a contact
contatto_pietro = Contatto('Pietro', 465745747457, 'pie@hotmail.it')
elenco.aggiungi_contatto(contatto_pietro)
   
# Displaying Contacts
You can use the visualizza_contatti property of the Elenco_contatti class to display the list of contacts.

# Example of displaying contacts
elenco.visualizza_contatti

# Deleting a Contact
To delete a contact, use the cancella_contatto method of the Elenco_contatti class, passing the contact you want 
to delete as an argument.

# Example of deleting a contact
elenco.cancella_contatto(contatto_pietro)

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Author
Pietro Striano
GitHub: Spagnuolo01233
