import argparse
import imaplib
import email
import sqlite3
import unittest

def get_emails(name_or_duration):
    conn = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    conn.login('moinalikhandevopser@gmail.com', 'Moin@123')
    conn.select('Inbox')
    
    if name_or_duration.isdigit():
        # Fetch emails from the past `name_or_duration` days
        search_criteria = f'(SINCE "now -{name_or_duration} days")'
    else:
        # Fetch emails related to the given name
        search_criteria = f'(FROM "{name_or_duration}")'
    
    _, email_ids = conn.search(None, search_criteria)
    
    emails = []
    for id in email_ids[0].split():
        _, msg = conn.fetch(id, '(RFC822)')
        email_data = email.message_from_bytes(msg[0][1])
        email_subject = email_data['subject']
        email_body = email_data.get_payload()
        emails.append((email_subject, email_body))
    
    conn.close()
    return emails

def store_emails_in_db(emails):
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emails
                 (subject text, body text)''')
    
    for email in emails:
        c.execute("INSERT INTO emails VALUES (?, ?)", email)
        
    conn.commit()
    conn.close()

class TestEmails(unittest.TestCase):
    def setUp(self):
        self.emails = get_emails('John Doe')
        store_emails_in_db(self.emails)
        
    def test_emails_exist(self):
        conn = sqlite3.connect('emails.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM emails")
        result = c.fetchone()[0]
        conn.close()
        self.assertGreater(result, 0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Name or duration')
    args = parser.parse_args()
    
    emails = get_emails(args.input)
    store_emails_in_db(emails)
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
