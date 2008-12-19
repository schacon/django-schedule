from django.core.management.base import NoArgsCommand

from django.core.management.color import no_style

class Command(NoArgsCommand):
    help = "Load some sample data into the db"

    def handle_noargs(self, **options):
        import datetime
        from schedule.models import Calendar
        from schedule.models import Event
        from schedule.models import Rule

        print "checking for existing data ..."
        try:
            cal = Calendar.objects.get(name="Example Calendar")
            import ipdb; ipdb.set_trace()
            print "It looks like you already have loaded this sample data, quitting."
            import sys
            sys.exit(1)
        except Calendar.DoesNotExist:
            print "Sample data not found in db."
            print "Install it..."


        print "Create Example Calendar ..."
        cal = Calendar(name="Example Calendar",slug="example")
        cal.save()
        print "The Example Calendar is created."
        print "Do we need to install the most common rules?"
        try:
            rule = Rule.objects.get(name="Daily")
        except Rule.DoesNotExist:
            print "Need to install the basic rules"
            rule = Rule(frequency = "YEARLY", name = "Yearly", description = "will recur once every Year")
            rule.save()
            print "YEARLY recurrence created"
            rule = Rule(frequency = "MONTHLY", name = "Monthly", description = "will recur once every Month")
            rule.save()
            print "Monthly recurrence created"
            rule = Rule(frequency = "WEEKLY", name = "Weekly", description = "will recur once every Week")
            rule.save()
            print "Weekly recurrence created"
            rule = Rule(frequency = "DAILY", name = "Daily", description = "will recur once every Day")
            rule.save()
            print "Daily recurrence created"
        print "Rules installed."

        print "Create some events"
        rule = Rule.objects.get(frequency="WEEKLY")
        data = {
                'title': 'Exercise',
                'start': datetime.datetime(2008, 11, 3, 8, 0),
                'end': datetime.datetime(2008, 11, 3, 9, 0),
                'end_recurring_period' : datetime.datetime(2009, 6, 1, 0, 0),
                'rule': rule,
               }
        event = Event(**data)
        event.save()
        cal.events.add(event)

        data = {
                'title': 'Exercise',
                'start': datetime.datetime(2008, 11, 5, 15, 0),
                'end': datetime.datetime(2008, 11, 5, 16, 30),
                'end_recurring_period' : datetime.datetime(2009, 6, 1, 0, 0),
                'rule': rule,
               }
        event = Event(**data)
        event.save()
        cal.events.add(event)

        data = {
                'title': 'Exercise',
                'start': datetime.datetime(2008, 11, 7, 8, 0),
                'end': datetime.datetime(2008, 11, 7, 9, 30),
                'end_recurring_period' : datetime.datetime(2009, 6, 1, 0, 0),
                'rule': rule,
               }
        event = Event(**data)
        event.save()
        cal.events.add(event)

        rule = Rule.objects.get(frequency="MONTHLY")
        data = {
                'title': 'Pay Mortgage',
                'start': datetime.datetime(2008, 11, 1, 14, 0),
                'end': datetime.datetime(2008, 11, 1, 14, 30),
                'end_recurring_period' : datetime.datetime(2009, 10, 2, 0, 0),
                'rule': rule,
               }
        event = Event(**data)
        event.save()
        cal.events.add(event)

        rule = Rule.objects.get(frequency="YEARLY")
        data = {
                'title': "Rock's Birthday Party",
                'start': datetime.datetime(2008, 12, 11, 19, 0),
                'end': datetime.datetime(2008, 12, 11, 23, 59),
                'end_recurring_period' : datetime.datetime(2009, 12, 22, 0, 0),
                'rule': rule,
               }
        event = Event(**data)
        event.save()
        cal.events.add(event)

        data = {
                'title': 'Christmas Party',
                'start': datetime.datetime(2008, 12, 25, 19, 30),
                'end': datetime.datetime(2008, 12, 25, 23, 59),
                'end_recurring_period' : datetime.datetime(2010, 12, 31, 0, 0),
                'rule': rule
               }
        event = Event(**data)
        event.save()
        cal.events.add(event)

        data = {
                'title': 'New Pinax site goes live',
                'start': datetime.datetime(2009, 1, 6, 11, 0),
                'end': datetime.datetime(2009, 1, 6, 12, 00),
                'end_recurring_period' : datetime.datetime(2009, 1, 7, 0, 0),
               }
        event = Event(**data)
        event.save()
        cal.events.add(event)

