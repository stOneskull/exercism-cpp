from datetime import datetime, timedelta


def delivery_date(start, description):
    delivery = datetime.fromisoformat(start)

    if description.startswith('Q'):
        delivery = quarters(description, delivery)

    elif description.endswith('M'):
        delivery = months(description, delivery)

    else:
        functions = {
            'NOW': now,
            'ASAP': asap,
            'EOW': eow,
        }
        delivery = functions[description](delivery)
        
    return delivery.isoformat()

    
def now(delivery):
    return delivery + timedelta(hours=2)


def asap(delivery):
    if delivery.hour < 13:
        delivery = delivery.replace(hour=17, minute=0)
        return delivery
    delivery = delivery.replace(hour=13, minute=0)
    return delivery + timedelta(days=1)


def eow(delivery):
    if (day := delivery.isoweekday()) in (1, 2, 3):
        delivery = delivery.replace(hour=17, minute=0)
        return delivery + timedelta(days=5-day)
    day = delivery.isoweekday()
    delivery = delivery.replace(hour=20, minute=0)
    return delivery + timedelta(7-day)


def quarters(description, delivery):
    delivery = delivery.replace(hour=8, minute=0)
    quarter = int(description.lstrip('Q'))
    current_q = (delivery.month - 1) // 3 + 1
    if current_q > quarter:
        delivery += timedelta(days=365)
    return end_quarter(delivery, quarter)


def end_quarter(delivery, quarter):
    match quarter:
        case 1:
            month, day = 3, 31
        case 2:
            month, day = 6, 30
        case 3:
            month, day = 9, 30
        case 4:
            month, day = 12, 31

    delivery = delivery.replace(month=month, day=day)
    if delivery.isoweekday() == 6:
        delivery -= timedelta(days=1)
    if delivery.isoweekday() == 7:
        delivery -= timedelta(days=2)
    return delivery


def months(description, delivery):
    delivery = delivery.replace(hour=8, minute=0)
    month = int(description.rstrip('M'))
    if delivery.month >= month:
        delivery += timedelta(days=365)
    delivery = delivery.replace(day=1, month=month)
    if delivery.isoweekday() == 6:
        delivery += timedelta(days=2)
    if delivery.isoweekday() == 7:
        delivery += timedelta(days=1)
    return delivery
