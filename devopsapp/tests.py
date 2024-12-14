from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Ticket, TicketStatus

class TicketModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_ticket_creation(self):
        ticket = Ticket.objects.create(
            title='Test Ticket',
            assignee=self.user,
            status=TicketStatus.TO_DO,
            description='This is a test ticket'
        )
        self.assertTrue(isinstance(ticket, Ticket))
        self.assertEqual(ticket.__str__(), 'Test Ticket')
        
    def test_ticket_status_choices(self):
        ticket = Ticket.objects.create(
            title='Status Test',
            assignee=self.user,
            status=TicketStatus.TO_DO,
            description='Testing status choices'
        )
        self.assertIn(ticket.status, [choice.value for choice in TicketStatus])
        
    def test_ticket_fields(self):
        ticket = Ticket.objects.create(
            title='Fields Test',
            assignee=self.user,
            status=TicketStatus.IN_PROGRESS,
            description='Testing fields'
        )
        self.assertEqual(len(ticket.title) <= 100, True)
        self.assertIsNotNone(ticket.created_at)
        self.assertIsNotNone(ticket.updated_at)
        
    def test_ticket_assignee_relationship(self):
        ticket = Ticket.objects.create(
            title='Relationship Test',
            assignee=self.user,
            status=TicketStatus.TO_DO,
            description='Testing relationships'
        )
        self.assertEqual(ticket.assignee, self.user)
        
    def test_ticket_status_invalid_choice(self):
        with self.assertRaises(ValidationError):
            ticket = Ticket.objects.create(
                title='Invalid Status',
                assignee=self.user,
                status='Invalid Status',
                description='Testing invalid status'
            )
            ticket.full_clean()
