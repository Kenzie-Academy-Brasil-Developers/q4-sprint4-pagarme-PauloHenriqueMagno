from datetime import datetime, date

def format_card_number(card_number):
  return card_number[-4:]

def is_card_expired(card_expiring_date):
  card_expiring_date = datetime.strptime(str(card_expiring_date), '%Y-%m-%d').date()

  return card_expiring_date > date.today()